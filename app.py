import pyowm
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

OWM_API_KEY = "fb73a0711f6108aa9ebf5046d4851139"

owm = pyowm.OWM(OWM_API_KEY)

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
        obs = owm.weather_at_coords(lat,lon)
        w = obs.get_weather()
        temp = w.get_temperature('celsius')
        status = str(w.get_detailed_status())
        resp.message("Current Temperature: " + str(temp['temp']) + "`C\n" + status)
    else:
        resp.message("Couldn't get your location. Please send your current location.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)