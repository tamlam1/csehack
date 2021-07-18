from sql import *
from src.apiTwilio import subscribe_sms_alert, call_user
import sys

# add dummy data here
def main():
    db = SQL()
    

    #print(db.getLatestContentID(1))
    # call_user('+610468615313', "DEEZ NUTS DEEZ NUTS DEEZ NUTS", "funny meme", "100")
    # Only need to do this once
    #db.initialiseDb()
    #db.deleteContent(1,1)

    # for i in range(1,10):
    #   for j in range(1,10):
    #     db.addContent(i, j, "title " + str(i),  "generic filename", "2021-01-01 10:20:05.123")

    for i in range(10,12):
      db.addChannel(i, "Fundamentals " + str(i), "Chemistry")

    # db.addSubscription(1, "+61422111578")
    #db.removeSubscription("1", "+61422111578")

    # a = db.getChannels()
    # print(db.convertChannelToJson(a))

    print(db.getSubscribers(1))
    #db.addContent('1', '11', "Minecraft", 'Minecraft is a sandbox video game developed by the Swedish video game developer Mojang Studios. The game was created by Markus "Notch" Persson in the Java programming language. Following several early private testing versions, it was first made public in May 2009 before fully releasing in November 2011, with Jens Bergensten then taking over development. Minecraft has since been ported to several other platforms and is the best-selling video game of all time, with 200 million copies sold and 126 million monthly active users as of 2020. In Minecraft, players explore a blocky, procedurally-generated 3D world with virtually infinite terrain, and may discover and extract raw materials, craft tools and items, and build structures or earthworks. Depending on game mode, players can fight computer-controlled "mobs", as well as cooperate with or compete against other players in the same world. Game modes include a survival mode, in which players must acquire resources to build the world and maintain health', "18/07/21")
    db.printDatabase()
    db.close()

if __name__== "__main__":
  main()