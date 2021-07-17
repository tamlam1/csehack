import sqlite3

connection = sqlite3.connect("file.db")


def initialiseDb():
  connection.execute(''' CREATE TABLE content (CHANNELID INT NOT NULL, FILENAME STRING NOT NULL, CATEGORY STRING NOT NULL)''')
  connection.commit()

  connection.execute(''' CREATE TABLE channels (CHANNELID INT PRIMARY KEY NOT NULL, CHANNELNAME STRING NOT NULL)''')
  connection.commit()

  #Hard code the different channels here
  connection.execute("INSERT INTO channels VALUES (?,?)", (1,"english"))
  connection.execute("INSERT INTO channels VALUES (?,?)", (2,"maths"))

  #create array to keep track of subscriptions
  connection.execute(''' CREATE TABLE subscriptions (CHANNELID INT NOT NULL, PHONENUMBER STRING NOT NULL)''')
  connection.commit()

#JSON
"""
{
   "CONTENT":{
      [
         "CHANNELID":1,
         "FILENAME":"Hello.mp3",
         "CATEGORY":"COMEDY"
      ]
   },
   "CHANNELS":{
      [
         "CHANNELID":1,
         "CHANNELNAME":"english"
      ],
      [
         "CHANNELID":2,
         "CHANNELNAME":"maths"
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
def addData(channelId, file, category):

  """
  # code for finding row number + 1
  cursor = connection.execute(f"SELECT ID from {database}")
  newId = int(len(cursor.fetchall()) + 1)
  """

  #add the new filename in the database
  #if statements are needed to do the same thing because for some reason 
  #sqlite does not let you string format INSERT statements 
  connection.execute("INSERT INTO content VALUES (?,?,?)", (channelId, file, category))
  connection.commit()


def addSubscription(channelId, phoneNumber):
    connection.execute("INSERT INTO subscriptions VALUES (?,?)",(channelId, phoneNumber))
    connection.commit()


def printDatabase():
  cursor = connection.execute('''SELECT * FROM content''')
  print("Content Table Details:")
  for row in cursor:
    print(f"Id: {row[0]} File name: {row[1]} Category: {row[2]}")

  print("")

  print("Channel Table Details")
  cursor = connection.execute('''SELECT *FROM channels''')
  for row in cursor:
    print(f"Channel Id: {row[0]} Channel Name: {row[1]}")

  print("")
  
  print("Subscription Table Details")
  cursor = connection.execute('''SELECT * FROM subscriptions''')
  for row in cursor:
    print(f"Channel Id: {row[0]} Phone Number: {row[1]}")

# add dummy data here
def main():
  initialiseDb()
  addData("english", "generic filename", "comedy")
  addSubscription(1, 123456789)
  printDatabase()
  connection.close()

if __name__== "__main__":
  main()

