import sqlite3

class SQL():

    def __init__(self):

        self.conn = sqlite3.connect("sandbox.db")
        self.curr = self.conn.cursor()


    def initialiseDb(self):
        self.curr.execute(''' CREATE TABLE content (CONTENTID INT PRIMARY KEY NOT NULL, CHANNELID INT NOT NULL, FILENAME TEXT NOT NULL, DATE TEXT NOT NULL)''')
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
    def addContent(self, contentId, channelId, file, date):

        """
        # code for finding row number + 1
        cursor = connection.execute(f"SELECT ID from {database}")
        newId = int(len(cursor.fetchall()) + 1)
        """

        #add the new filename in the database
        #if statements are needed to do the same thing because for some reason 
        #sqlite does not let you string format INSERT statements 
        self.curr.execute("INSERT INTO content VALUES (?,?,?,?)", (contentId, channelId, file, date))
        self.conn.commit()


    def addSubscription(self, channelId, phoneNumber):
        self.curr.execute("INSERT INTO subscriptions VALUES (?,?)", (channelId, phoneNumber))
        self.conn.commit()

    def addChannel(self, channelId, channelname, category):
        self.curr.execute("INSERT INTO channels VALUES (?,?)", (channelId, channelname, category))
        self.conn.commit()

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

