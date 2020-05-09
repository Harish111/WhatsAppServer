from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    print(incoming_msg)
    sendResponse("Hello")
    return "Hey man"


def sendResponse(msg):
    account_sid = 'your sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello there!',
        from_='whatsapp:source number',
        to='whatsapp:destination number'
    )
    print(message.sid)


if __name__ == '__main__':
    app.run()