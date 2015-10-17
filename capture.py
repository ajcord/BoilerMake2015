import RPi.GPIO as GPIO
import time
import picamera
import post

def capture_loop():

    camera = picamera.PiCamera()
    
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO input pins
    pad0 = 22
    led = 17
    
    GPIO.setup(pad0, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)
    
    pad0alreadyPressed = False
    
     
    while True:
        pad0pressed = not GPIO.input(pad0)
        
        if pad0pressed and not pad0alreadyPressed:
            GPIO.out(led, True)
            print("Starting countdown")
            time.sleep(2)
            GPIO.out(led, False)
            print("Smile!")
            time.sleep(0.5)
            GPIO.out(led, True)
            camera.capture("image.jpg")
            time.sleep(0.5)
            GPIO.out(led, False)
            # upload_to_server("image.jpg")
            post.push_post("image.jpg", "Test")

        pad0alreadyPressed = pad0pressed
        
        time.sleep(0.1)

capture_loop()