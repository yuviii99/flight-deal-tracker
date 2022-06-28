from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_NUMBER = "TWILIO_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_NUMBER"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)