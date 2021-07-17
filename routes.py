from flask import request, jsonify
from app import app
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from src.twilio import subscribe_sms_alert,call_user

@app.route('/')
def home():
    return {'hi':'hello'}


@app.route('/api/call_user', methods=['POST','GET'])
def call_user():
    #Get user info from front_end
    #call_user()
    pass

@app.route('/api/get_data', methods=['POST'])
def get_data():

    data = request.get_json()
    print(data)
    return {'hi':'done'}

@app.route('/api/voice', methods=['POST','GET'])
def voice():
    response = VoiceResponse()
    #subscribe_sms_alert('+61468615313', '1', 'English')

    gather = Gather(action='/api/speechText', finishOnKey="#" , method="GET", timeout="10")
    gather.say("Hello Welcome to Sandbox, please wait for speech options or press a number followed by the hash key")
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
    
    try:
        ID = request.args.get('ID')
        option = requestion.args.get('Digits')
        curr_lec_id = 0 #You gotta get this
    except:
        ID = request.args.get('Digits')
        curr_lec_id = 0 #max number

    response = VoiceResponse()
    response.say("hello you reached this point")

    if str(option) == '1':
        #Select the current one to listen to
        pass
    elif str(option) == '2':
        #Go next
        pass
    elif str(option) == '3':
        #Go back
        pass
    else:
        pass

    #Search for if the channel exists 
    #Channel 
    #If it does, ask them which one of them they wanna play
    #If it doesn't try again
    return 'a'



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

        gather = Gather(action='/api/speechSpeak', input='speech dtmf', method="GET")
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

@app.route('/api/speechSpeak', methods=['POST','GET'])
def speechSpeak():

    data = request.args.get('SpeechResult')
    print(data)
    said = "You said " + str(data)

    response = VoiceResponse()
    response.say(said)

    if str(data) == '1':
        pass
       #ask for channel name
    elif str(data) == '2':
        pass
        #ask for category
    elif str(data) == '3':
        pass
        #ask for channel name, then record 
    elif str(data) == '4':
        response.redirect('/api/speechOptions', method="GET")
    else:
        response.say("No response... or wrong I D")
        response.redirect('/api/speechOptions', method="GET")

    return str(response)






