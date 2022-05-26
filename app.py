import RPi.GPIO as GPIO
import time
import uuid
# Required imports

from firebase_admin import db, credentials, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred, {
        'databaseURL':'https://smartchair-41e3e-default-rtdb.firebaseio.com/'
        })
ref = db.reference("/user/123/")

BUTTON_PIN = 16

GPIO.setmode(GPIO.BCM)

def button_callback(channel):

    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        try:
            ref.set({'sit' : False})
        except Exception as e:
            return f"An Error Occurred: {e}"
        print("Button has just been released")
    else:
        try:
            ref.set({'sit' : True})
        except Exception as e:
            return f"An Error Occurred: {e}"
        print("Button has just been pressed")

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime = 50)

try:
   while True:
       time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()