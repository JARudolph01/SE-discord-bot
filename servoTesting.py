#https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c
import RPi.GPIO as GPIO
from time import sleep
print("i think it's working")
ledpin = 33				# PWM pin connected to LED
ledpin2 = 32				# PWM pin connected to LED
#GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(ledpin2,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,255)		#create PWM instance with frequency
pi_pwm2 = GPIO.PWM(ledpin2,255)		#create PWM instance with frequency
pi_pwm.start(20)				#start PWM of required Duty Cycle 
pi_pwm2.start(20)				#start PWM of required Duty Cycle 
#while True:
#    for duty in range(0,21):
#        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#        pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#        sleep(0.01)
#    
#    sleep(.3)
#
#    for duty in range(0,21):
#        pi_pwm.ChangeDutyCycle(20-duty)
#        pi_pwm2.ChangeDutyCycle(20-duty)
#        sleep(0.01)
#    
#
#    #for duty in range(20,80):
     #   pi_pwm.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
      #  pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100        
       # sleep(0.01)
#    
while True:
    for duty in range(0,21):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.5)
    
    sleep(.3)

    for duty in range(0,21):
        pi_pwm.ChangeDutyCycle(20-duty)
        pi_pwm2.ChangeDutyCycle(20-duty)
        sleep(0.5)
    

    #for duty in range(20,80):
     #   pi_pwm.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
      #  pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100        
       # sleep(0.01)
    
