import RPi.GPIO as GPIO
import time
import picamera
import twitterpost
import text_pool_selector
import combine_images


def capture_loop():

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
            camera.hflip = True
            camera.capture("image.jpg")
            time.sleep(0.5)
            GPIO.output(led, False)
            combine_images.addSticker()
            twitterpost.push_post("blended.jpg", text_pool_selector.getRandomQuote())


        pad0alreadyPressed = pad0pressed

        time.sleep(0.1)

capture_loop()
