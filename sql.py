import sqlite3

class SQL():

    def __init__(self):

        self.conn = sqlite3.connect("sandbox.db")
        self.curr = self.conn.cursor()


    def initialiseDb(self):
        self.curr.execute(''' CREATE TABLE content (CONTENTID INT NOT NULL, CHANNELID INT NOT NULL, TITLE TEXT NOT NULL, FILENAME TEXT NOT NULL, DATE TEXT NOT NULL, PRIMARY KEY(CONTENTID,CHANNELID))''')
        self.conn.commit()

        self.curr.execute(''' CREATE TABLE channels (CHANNELID INT PRIMARY KEY NOT NULL, CHANNELNAME TEXT NOT NULL, CATEGORY TEXT NOT NULL)''')
        self.conn.commit()

        #create array to keep track of subscriptions
        self.curr.execute(''' CREATE TABLE subscriptions (CHANNELID INT NOT NULL, PHONENUMBER TEXT NOT NULL)''')
        self.conn.commit()

        #Hard code the different channels here 
        self.curr.execute("INSERT INTO channels VALUES (?,?,?)", (1,"mrbeast", "maths"))
        self.curr.execute("INSERT INTO channels VALUES (?,?,?)", (2,"pewdiepie", "biology"))
        self.conn.commit()

    #JSON
    """
    {
    "CONTENT":{
        [
            "CONTENTID":1,
            "CHANNELID":1,
            "FILENAME":"Hello.mp3",
            "DATE": "2021-01-01 10:20:05.123"
        ]
    },
    "CHANNELS":{
        [
            "CHANNELID":1,
            "CHANNELNAME":"Eddie Woo Teaches Math"
            "CATEGORY":"MATHS"
        ],
        [
            "CHANNELID":2,
            "CHANNELNAME":"Shrek but it gets faster each time he says Donkey"
            "CATEGORY":"COMEDY"
        ]
    },
    "SUBSCRIPTIONS":{
        [
            "CHANNELID":1,
            "PHONENUMBER":123456789
        ],
        [
            "CHANNELID":1,
            "PHONENUMBER":987654632
        ],
        [
            "CHANNELID":2,
            "PHONENUMBER":515155151
        ]
    }
    }
    """
    #add the data to the appropriate database
    def addContent(self, contentId, channelId, title, file, date):

        """
        # code for finding row number + 1
        cursor = connection.execute(f"SELECT ID from {database}")
        newId = int(len(cursor.fetchall()) + 1)
        """

        #add the new filename in the database
        #if statements are needed to do the same thing because for some reason 
        #sqlite does not let you string format INSERT statements 
        self.curr.execute("INSERT INTO content VALUES (?,?,?,?,?)", (contentId, channelId, title, file, date))
        self.conn.commit()


    def addSubscription(self, channelId, phoneNumber):
        self.curr.execute("INSERT INTO subscriptions VALUES (?,?)", (channelId, phoneNumber))
        self.conn.commit()

    def removeSubscription(self, channelId, phoneNumber):
        self.curr.execute("DELETE FROM subscriptions where channelId=? and phoneNumber=?", (channelId, phoneNumber))
        self.conn.commit()

    def addChannel(self, channelId, channelname, category):
        self.curr.execute("INSERT INTO channels VALUES (?,?,?)", (channelId, channelname, category))
        self.conn.commit()

    def deleteChannel(self, channelId):
        self.curr.execute("DELETE FROM channels where channelid = "+ str(channelId))
        self.conn.commit()

    def deleteContent(self, CONTENTID, CHANNELID):
        self.curr.execute("DELETE FROM content where CHANNELID = "+ str(CHANNELID) + " and " + "CONTENTID = " + str(CONTENTID))
        self.conn.commit()

    def getContent(self, CHANNELID):
        cursor = self.curr.execute("SELECT * FROM content where CHANNELID = "+ str(CHANNELID))
        return cursor

    def getContentText(self, CHANNELID, CONTENTID):
        cursor = self.curr.execute("SELECT filename FROM content where CHANNELID = "+ str(CHANNELID) + " and " + "CONTENTID = " + str(CONTENTID))
        for i in cursor:   
            tup = i
        return tup

    def getContentIDTitleOnly(self, CHANNELID):
        cursor = self.curr.execute("SELECT contentid, title FROM content where CHANNELID = "+ str(CHANNELID) + " order by contentid DESC")
        temp = []
        for i in cursor:
            temp.append(i)
        return temp

    def getLatestContentID(self,CHANNELID):
        
        cursor = self.curr.execute("SELECT max(contentid) FROM content where CHANNELID = "+ str(CHANNELID))
        max = 0
        for i in cursor:
            max = i[0]
        return max

    def getSubscribers(self, CHANNELID):
        cursor = self.curr.execute("SELECT * FROM subscriptions where CHANNELID = "+ str(CHANNELID))
        temp = []
        for i in cursor:
            temp.append(i)
        return temp

    def getChannels(self):
        cursor = self.curr.execute("SELECT * FROM channels")
        return cursor

    def convertChannelToJson(self, cursor):
        temp = []
        for i in cursor:
            tempCon = {}
            tempCon['id'] = i[0] 
            tempCon['channel_name'] = i[1] 

            temp.append(tempCon)

        return temp

    def convertContentToJson(self, cursor):
        temp = []
        for i in cursor:
            tempCon = {}

            tempCon['id'] = i[0] 
            tempCon['channel_id'] = i[1] 
            tempCon['lecture_name'] = i[2] 
            tempCon['content'] = i[3]
            tempCon['time_uploaded'] = i[4] 
             
            temp.append(tempCon)
        print(temp)
        return temp

    def getChannelName(self, CHANNELID):
        cursor = self.curr.execute("SELECT channelname FROM channels where channelid=" + str(CHANNELID))
        for i in cursor:   
            tup = i
        return tup[0]

    def channelExist(self, CHANNELID):
        print(CHANNELID)
        cursor = self.curr.execute("SELECT * FROM channels where CHANNELID =" + str(CHANNELID))
        if cursor:
            return 1
        else:
            return 0

    def close(self):
        self.conn.close()


    def printDatabase(self):
        cursor = self.conn.execute('''SELECT * FROM content''')
        print("Content Table Details:")
        for row in cursor:
            print(f"Content: {row[0]} Channel: {row[1]} File: {row[2]} Date: {row[3]}")

        print("")

        print("Channel Table Details")
        cursor = self.conn.execute('''SELECT *FROM channels''')
        for row in cursor:
            print(f"Channel Id: {row[0]} Channel Name: {row[1]} Category: {row[2]}")

        print("")
        
        print("Subscription Table Details")
        cursor = self.conn.execute('''SELECT * FROM subscriptions''')
        for row in cursor:
            print(f"Channel Id: {row[0]} Phone Number: {row[1]}")

