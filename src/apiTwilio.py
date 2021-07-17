from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

account_sid = 'AC4ac9e7a735105238e024d5d53a1a7d44'
auth_token = ''
client = Client(account_sid, auth_token)

# <Play>http://demo.twilio.com/docs/classic.mp3</Play>
def subscribe_sms_alert(number, channel_no, channel_name):
    text = "Sandbox: " + str(channel_name) + " has just been updated. Call us back on +61480093161 and let us know the channel ID: " + str(channel_no) + " to start listening!"

    message = client.messages \
                .create(
                    body=text,
                    from_='+61480093161',
                    to=number
                 )


def call_user(number, content, channel_name, channel_ID):
    
    response = VoiceResponse()
    response.say("Listening to..channel I D " + str(channel_ID) + " : " + str(channel_name))
    response.say(content)
    print(response)

    call = client.calls.create(
                        twiml=response,
                        from_='+61480093161',
                        to=number
                        )

