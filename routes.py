from flask import request, jsonify
from app import app
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from twilio.twiml.messaging_response import MessagingResponse
from src.apiTwilio import subscribe_sms_alert,call_user, new_subscribe_sms_alert 
from sql import *
import re
from datetime import datetime

@app.route('/')
def home():
    return {'hi':'hello'}

@app.route('/api/get_channels', methods=['POST','GET'])
def get_channels():

    db = SQL()
    
    a = db.getChannels()
    temp = db.convertChannelToJson(a)

    print(temp)
    db.close()
    return {'data': temp}

@app.route('/api/get_content', methods=['POST','GET'])
def get_content():

    data = request.get_json()

    id = data['id']

    db = SQL()
    
    a = db.getContent(str(id))
    temp = db.convertContentToJson(a)

    print(temp)
    db.close()
    return {'data': temp}

@app.route('/api/get_data', methods=['POST'])
def get_data():
    db = SQL()

    data = request.get_json()
    category = data['category'][0]
    text = data['text'][0]
    channel_id = data['channel'][0]
    title = data['title'][0]
    
    now = datetime.now()
    date = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date)
    
    print(db.getLatestContentID(channel_id))
    new_content_id = int(db.getLatestContentID(channel_id)) + 1
    
    db.addContent(new_content_id, channel_id, title, text, date)
    notify_subscribers(channel_id)
    db.close()
    return {'hi':'done'}

def notify_subscribers(channel_id):
    #when new content is added, notify all subscribers using text
    db = SQL()
    numbers = db.getSubscribers(channel_id)
    channel_name = db.getChannelName(channel_id)
    
    for number in numbers:
        subscribe_sms_alert(number[1],channel_id, channel_name)
    
    db.close()

@app.route('/api/unsubscribe_sms', methods=['POST','GET'])
def unsubscribe_sms():
    response = MessagingResponse()
    print(response)
    number = request.form['From']
    body = request.form['Body']
    body = str(body).lower()
    print(body)

    reg = re.search("unsubscribe[' ']?[0-9]+[' ']?$", body)
    if reg:
        ID = re.search("[0-9]+", reg[0])
        db = SQL()
        try:
            db.removeSubscription(str(ID.group(0)), str(number))
        except:
            pass
        db.close()
    return str(response)

@app.route('/api/subscribe_user', methods=['POST'])
def subscribe_user():
    db = SQL()

    data = request.get_json()
    number = str(data['phone_number'])
    number = number[:3] + number[4:]
    ID = str(data['channel_id'][0])
    db.addSubscription(ID, number)

    name = db.getChannelName(ID)

    new_subscribe_sms_alert(number, ID, name)

    db.close()
    return {'hi':'done'}

@app.route('/api/unsubscribe_user_web', methods=['POST'])
def unsubscribe_user():
    db = SQL()

    data = request.get_json()
    number = str(data['phone_number'])
    number = number[:3] + number[4:]
    ID = str(data['channel_id'][0])

    try:
        db.removeSubscription(ID, number)
    except:
        pass

    db.close()
    return {'hi':'done'}

@app.route('/api/play_lecture', methods=['POST'])
def play_lecture():
    
    db = SQL()

    data = request.get_json()
    number = str(data['phone_number'])
    number = number[:3] + number[4:]
    channelID = str(data['channel_id'][0])
    contentID = str(data['lecture_id'][0])
    
    tup = db.getContentText(channelID,contentID)
    call_user(number, tup[0], channelID)

    print(data)
    return {'hi':'done'}

@app.route('/api/voice', methods=['POST','GET'])
def voice():
    response = VoiceResponse()
    gather = Gather(action='/api/speechText', finishOnKey="#" , method="GET", timeout="10")
    gather.say("Hello Welcome to Sandbox, please wait for speech options. For numpad options, press a following number then the hash key")
    gather.say("Press 1 to directly search a channel I D")
    gather.say("Press 2 to browse categories")
    gather.say("Press 3 to record to a channel")
    gather.say("Press 4 to hear the options again")
    gather.say("Please wait for speech options.")
    response.append(gather)

    gather = Gather(action='/api/speechOptions', input='speech', method="GET", hint="YES")
    gather.say("For speech options, please say YES in the next 6 seconds")
    response.append(gather) 

    response.say("No response... or wrong ID")
    response.redirect('/api/voice', method="GET")
    return str(response)

@app.route('/api/speechText', methods=['POST','GET'])
def speechText():
    response = VoiceResponse()

    data = request.args.get('Digits')
    print(data)
    # said = "You wrote " + str(data)
    # response.say(said)

    if str(data) == '1':
        gather = Gather(action='/api/confirmChannel', finishOnKey="#" , method="GET", timeout="10")
        gather.say("Please write a channel I D followed by the hash key to begin listening")
        response.append(gather)
        response.redirect('/api/speechText?Digits=1', method="GET")
       #ask for channel name
    elif str(data) == '2':
        pass
        #ask for category
    elif str(data) == '3':
        pass
        #ask for channel name, then record 
    elif str(data) == '4':
        response.redirect('/api/voice', method="GET")
    else:
        response.say("No response... or wrong ID")
        response.redirect('/api/voice', method="GET")

    return str(response)

@app.route('/api/confirmChannel', methods=['POST','GET'])
def confirmChannel():

    response = VoiceResponse()

    ID = request.args.get('Digits')
    actionID = '/api/selectChannel?Digits=' + str(ID)

    IDGiven = "You gave us ID " + str(ID) +  ". Press any key followed by a hash key to confirm, Press nothing to go back"
    gather = Gather(action=actionID, finishOnKey="#" , method="GET", timeout="10")
    gather.say(IDGiven)
    response.append(gather)

    response.redirect('/api/speechText?Digits=1', method="GET")
    return str(response)

@app.route('/api/selectChannel', methods=['POST','GET'])
def selectChannel():
    
    db = SQL()
    response = VoiceResponse()
    index = 0
    try:
        ID = request.args.get('ID')
        index = request.args.get('Index')
    except:
        ID = request.args.get('Digits')
    
    if ID == None:
        ID = request.args.get('Digits')
        index=0

    print(ID)
    check = db.channelExist(str(ID))
    if check == 0:
        response.say('Channel ID does not exist')
        response.redirect('/api/speechText?Digits=1', method="GET")
    else:
        contentList = db.getContentIDTitleOnly(str(ID))

        maxLen = len(contentList) 

        currentTitle = contentList[int(index)][1]
        currContentID = contentList[int(index)][0]

        actionText = '/api/selectChannelOptions?ID=' + str(ID) + '&Index=' + str(index) + '&maxLen=' + str(maxLen) + '&currContentID='  + str(currContentID)

        gather = Gather(action=actionText, finishOnKey="#" , method="GET", timeout="10")
        gather.say('Current Content is ' + currentTitle)
        gather.say('Press 1 to select it')
        gather.say('Press 2 to go to a previous entry in time')
        gather.say('Press 3 to go to the following entry in time')
        response.append(gather)
        
        db.close()
        return str(response)

@app.route('/api/selectChannelOptions', methods=['POST','GET'])
def selectChannelOptions():
    response = VoiceResponse()
    ID = request.args.get('ID')
    index = request.args.get('Index')
    option = request.args.get('Digits')
    contentID = request.args.get('currContentID')
    maxLen = request.args.get('maxLen')

    if str(option) == '1':
        db = SQL()
        tup = db.getContentText(str(ID), str(contentID))
        db.close()
        response.say(tup[0])
        response.say("Thank you for listening")
    elif str(option) == '2':
        if int(index) + 1 <= int(maxLen):
            index = int(index) + 1

        redirect = '/api/selectChannel?ID=' + str(ID) + '&Index=' + str(index)
        response.redirect(redirect, method="GET")  
    elif str(option) == '3':
        if int(index) - 1 > 0:
            index = int(index) - 1
        redirect = '/api/selectChannel?ID=' + str(ID) + '&Index=' + str(index)
        response.redirect(redirect, method="GET")  
    else:
        redirect = '/api/selectChannel?ID=' + str(ID) + '&Index=' + str(index)
        response.redirect(redirect, method="GET")

    return str(response)



@app.route('/api/speechOptions', methods=['POST','GET'])
def speechOptions():

    #If coming from original call, if confidence level below 0.5, go back to original call
    #If looping from this route, auto ask again 
    response = VoiceResponse()
    data = 0
    try :
        data = request.args.get('Confidence')
        data = float(data)
    except:
        data = 0.5

    print(data)
    if data >= 0.5:

        gather = Gather(action='/api/speechOptionsConfirm', input='speech dtmf', method="GET")
        gather.say("Hello Welcome to Sandbox Speech Options, please say one of the following numbers followed by a hash")
        gather.say("Say 1 to directly search a channel I D")
        gather.say("Say 2 to browse categories")
        gather.say("Say 3 to record")
        gather.say("Press 4 to hear the options again")
        response.append(gather)

        response.say("No response... or wrong ID")
        response.redirect('/api/speechOptions', method="GET")
    else:
        response.say("Sorry, we didn't get that")
        response.redirect('/api/voice', method="GET")

    return str(response)

@app.route('/api/speechOptionsConfirm', methods=['POST','GET'])
def speechOptionsConfirm():
    response = VoiceResponse()

    data = request.args.get('Digits')
    print(data)

    if str(data) == '1':
        gather = Gather(action='/api/confirmChannelSpeech', input='speech dtmf' , method="GET", timeout="10")
        gather.say("Please say a channel I D to begin listening")
        response.append(gather)
        response.redirect('/api/speechText?Digits=1', method="GET")
    elif str(data) == '2':
        pass
        #ask for category
    elif str(data) == '3':
        pass
        #ask for channel name, then record 
    elif str(data) == '4':
        response.redirect('/api/speechOptions', method="GET")
    else:
        response.say("No response... or wrong ID")
        response.redirect('/api/speechOptions', method="GET")

    return str(response)

@app.route('/api/confirmChannelSpeech', methods=['POST','GET'])
def confirmChannelSpeech():

    response = VoiceResponse()

    ID = request.args.get('Digits')
    actionID = '/api/selectSpeechChannel?Digits=' + str(ID)

    IDGiven = "You gave us ID " + str(ID) +  ". Please say anything to confirm, Say nothing to go back"
    gather = Gather(action=actionID, input='speech dtmf' , method="GET", timeout="10")
    gather.say(IDGiven)
    response.append(gather)

    response.redirect('/api/speechOptionsConfirm?Digits=1', method="GET")
    return str(response)

@app.route('/api/selectSpeechChannel', methods=['POST','GET'])
def selectSpeechChannel():
    
    db = SQL()
    response = VoiceResponse()
    index = 0
    try:
        ID = request.args.get('ID')
        index = request.args.get('Index')
    except:
        ID = request.args.get('Digits')
    
    if ID == None:
        ID = request.args.get('Digits')
        index=0

    print(ID)
    check = db.channelExist(str(ID))
    if check == 0:
        response.say('Channel ID does not exist')
        response.redirect('/api/speechOptionsConfirm?Digits=1', method="GET")
    else:
        contentList = db.getContentIDTitleOnly(str(ID))

        maxLen = len(contentList) 

        currentTitle = contentList[int(index)][1]
        currContentID = contentList[int(index)][0]

        actionText = '/api/selectChannelOptions?ID=' + str(ID) + '&Index=' + str(index) + '&maxLen=' + str(maxLen) + '&currContentID='  + str(currContentID)

        gather = Gather(action=actionText, input='speech dtmf' , method="GET", timeout="10")
        gather.say('Current Content is ' + currentTitle)
        gather.say('Say 1 to select it')
        gather.say('Say 2 to go to a previous entry in time')
        gather.say('Say 3 to go to the following entry in time')
        response.append(gather)
        
        db.close()
        return str(response)



