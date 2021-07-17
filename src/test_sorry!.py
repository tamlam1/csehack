from sql import *


# add dummy data here
def main():
    db = SQL()

    # Only need to do this once
    # db.initialiseDb()
    db.addContent(1, 1, "generic filename", "2021-01-01 10:20:05.123")
    db.addSubscription(1, 123456789)
    db.printDatabase()
    db.close()

if __name__== "__main__":
  main()