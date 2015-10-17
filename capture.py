import RPi.GPIO as GPIO
import time
import picamera
import post

def capture_loop():

    camera = picamera.PiCamera()
    
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO input pins
    pad0 = 22
    
    GPIO.setup(pad0, GPIO.IN)
    
    pad0alreadyPressed = False
    
     
    while True:
        pad0pressed = not GPIO.input(pad0)
        
        if pad0pressed and not pad0alreadyPressed:
            print("Starting countdown")
            time.sleep(3)
            print("Smile!")
            camera.capture("image.jpg")
            # upload_to_server("image.jpg")
            post.push_post("image.jpg", "Test")

        pad0alreadyPressed = pad0pressed
        
        time.sleep(0.1)

capture_loop()