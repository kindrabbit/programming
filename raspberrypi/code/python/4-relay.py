import RPi.GPIO as GPIO
import time
makerobo_RelayPin = 11

def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(makerobo_RelayPin,GPIO.OUT)
    GPIO.output(makerobo_RelayPin,GPIO.LOW)

def makerobo_loop():
    while True:
        GPIO.output(makerobo_RelayPin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(makerobo_RelayPin,GPIO.LOW)
        time.sleep(0.5)
        
def makerobo_destory():
    GPIO.output(makerobo_RelayPin,GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destory()