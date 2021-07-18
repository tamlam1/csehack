from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

account_sid = 'AC4ac9e7a735105238e024d5d53a1a7d44'
auth_token = ''
client = Client(account_sid, auth_token)

def subscribe_sms_alert(number, channel_no, channel_name):
    text = "Sandbox: " + str(channel_name) + " has just been updated. Call us back on +61480093161 and let us know the channel ID: " + str(channel_no) + " to start listening! Reply 'Unsubscribe " + str(channel_no) + "' to stop."

    message = client.messages \
                .create(
                    body=text,
                    from_='+61480093161',
                    to=number
                 )

def new_subscribe_sms_alert(number, channel_no, channel_name):
    text = "Sandbox: You've just subscribed to " + str(channel_name) + "! Call us back on +61480093161 and let us know the channel ID: " + str(channel_no) + " to listen now! Reply 'Unsubscribe " + str(channel_no) + "' to stop."

    message = client.messages \
                .create(
                    body=text,
                    from_='+61480093161',
                    to=number
                 )

def call_user(number, content, channel_ID):
    
    response = VoiceResponse()
    response.say("Listening to..channel I D " + str(channel_ID))
    response.say(content)
    print(response)

    call = client.calls.create(
                        twiml=response,
                        from_='+61480093161',
                        to=number
                        )

