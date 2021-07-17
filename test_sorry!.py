from sql import *
from src.apiTwilio import subscribe_sms_alert, call_user
import sys

# add dummy data here
def main():
    db = SQL()
    # a = db.getChannels()

    # for i in a:
    #   print(i)
    # call_user(1, "DEEZ NUTS DEEZ NUTS DEEZ NUTS", "funny meme", "100")
    # Only need to do this once
    db.initialiseDb()
    #db.deleteContent(1,1)

    for i in range(1,10):
      for j in range(1,10):
        db.addContent(i, j, "title " + str(i),  "generic filename", "2021-01-01 10:20:05.123")

    for i in range(3,10):
      db.addChannel(i, "Fundamentals " + str(i), "Chemistry")

    db.addSubscription(1, "+61422111578")
    db.printDatabase()
    db.close()

if __name__== "__main__":
  main()