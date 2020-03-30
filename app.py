from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    if request.values.get('Latitude'):
        lat = float(request.values.get('Latitude', None))
        lon = float(request.values.get('Longitude', None))
        resp.message("Got your location Latitude:" + str(lat) + "Longitude:" + str(lon))
    else:
        resp.message("Couldn't get your location. Please send your current location.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)