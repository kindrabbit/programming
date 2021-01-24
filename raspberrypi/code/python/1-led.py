import RPi.GPIO as GPIO
import time
colors=[0xFF00,0x00FF,0x0FF0,0xF00F]
makerobo_pins=(11,12)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(makerobo_pins,GPIO.OUT)
GPIO.output(makerobo_pins,GPIO.LOW)
p_R=GPIO.PWM(makerobo_pins[0],2000)
p_G=GPIO.PWM(makerobo_pins[1],2000)

p_R.start(0)
p_G.start(0)
def makerobo_pwm_map(x,in_min,in_max,out_min,out_max):
    return(x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min
def makerobo_set_Color(col):
    R_val=col>>8
    G_val=col&0x00FF
    R_val=makerobo_pwm_map(R_val,0,255,0,100)
    G_val=makerobo_pwm_map(G_val,0,255,0,100)
    
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)

def makerobo_loop():
    while True:
        for col in colors:
            makerobo_set_Color(col)
            time.sleep(0.5)
        
def makerobo_destroy():
    p_G.stop()
    p_R.stop()
    GPIO.output(makerobo_pins,GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == "__main__":
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destory()

