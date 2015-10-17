import RPi.GPIO as GPIO
import time
import picamera
import twitterpost
import random


def capture_loop():
    quotes = ["Happy Hacking!", "Pumpkin Pi?", "Boilermake? Try Pumpkinmake!", "Look ma, I'm famous!"]

    camera = picamera.PiCamera()

    GPIO.setmode(GPIO.BCM)

    # Set the GPIO input pins
    pad0 = 22
    led = 17

    GPIO.setup(pad0, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)

    pad0alreadyPressed = False
    GPIO.output(led, False)

    while True:
        pad0pressed = not GPIO.input(pad0)

        if pad0pressed and not pad0alreadyPressed:
            GPIO.output(led, True)
            print("Starting countdown")
            time.sleep(2)
            GPIO.output(led, False)
            print("Smile!")
            time.sleep(0.5)
            GPIO.output(led, True)
            camera.vflip =True
            camera.capture("image.jpg")
            time.sleep(0.5)
            GPIO.output(led, False)
            # upload_to_server("image.jpg")
            twitterpost.push_post("image.jpg", quotes[random.randrange(0, quotes.length + 1)])

        pad0alreadyPressed = pad0pressed

        time.sleep(0.1)

capture_loop()
