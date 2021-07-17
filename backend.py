import sqlite3

connection = sqlite3.connect("file.db")

def initialiseDb():
  #table for channel with english related content
  connection.execute(''' CREATE TABLE english (ID INT PRIMARY KEY NOT NULL, FILENAME STRING NOT NULL)''')

  connection.commit()

  #table for channel with maths related content
  connection.execute(''' CREATE TABLE maths (ID INT PRIMARY KEY  NOT NULL, FILENAME STRING NOT NULL)''')

  connection.commit()

  #table for channel to keep track of people that have registered
  connection.execute('''CREATE TABLE users (NUMBER INT PRIMARY KEY NOT NULL)''')

  connection.commit()

  #table to keep track of people subscribed to english
  connection.execute('''CREATE TABLE englishsubscriptions (NUMBER INT PRIMARY KEY NOT NULL)''')

  connection.commit()

  #table to keep track of people subscribed to maths channel
  connection.execute(''' CREATE TABLE mathssubscriptions (NUMBER INT PRIMARY KEY NOT NULL)''')

  connection.commit()

#add the data to the appropriate database
def addDataToEnglish(database, file):
  # iterate through table and find the next
  cursor = connection.execute(f"SELECT ID from {database}")
  newId = int(len(cursor.fetchall()) + 1)

  #add the new filename in the database
  connection.execute("INSERT INTO english VALUES (?,?)", (newId, file))
  connection.commit()

#two different methods are needed to do the same thing because for some reason 
# sqlite does not let you string format INSERT statements 
def addDataToMaths(database, file):
  # iterate through table and find the next
  cursor = connection.execute(f"SELECT ID from {database}")
  newId = int(len(cursor.fetchall()) + 1)

  #add the new filename in the database
  connection.execute("INSERT INTO maths VALUES (?,?)", (newId, file))
  connection.commit()

def printDatabase():
  cursor = connection.execute('''SELECT ID, FILENAME FROM english''')
  for row in cursor:
    print(f"Id: {row[0]}")
    print(f"File name: {row[1]}")
  
  cursor = connection.execute('''SELECT ID, FILENAME FROM maths''')
  for row in cursor:
    print(f"Id: {row[0]}")
    print(f"File name: {row[1]}")

def main():
  initialiseDb()
  addDataToEnglish("english", "generic filename")
  printDatabase()
  connection.close()

if __name__== "__main__":
  main()

