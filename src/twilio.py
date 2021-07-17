from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

account_sid = 'AC4ac9e7a735105238e024d5d53a1a7d44'
auth_token = 'b13eaa7598a39252ddd9c89c40ae0f4a'
client = Client(account_sid, auth_token)

# <Play>http://demo.twilio.com/docs/classic.mp3</Play>
def subscribe_sms_alert(number, channel_no, channel_name):
    number= '+61468615313'
    text = "Sandbox: " + str(channel_name) + " has just been updated. Call us back on +61480093161 and let us know the channel ID: " + str(channel_no) + " to start listening!"

    message = client.messages \
                .create(
                    body=text,
                    from_='+61480093161',
                    to=number
                 )


def call_user(number, content):

    response = VoiceResponse()
    gather = Gather(input='speech dtmf', timeout=3, num_digits=1)
    gather.say('dasdsa')
    response.append(gather)

    print(response)

    call = client.calls.create(
                        twiml=response,
                        from_='+61480093161',
                        to='+61468615313'
                        )

    pass
