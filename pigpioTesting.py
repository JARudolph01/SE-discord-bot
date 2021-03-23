#https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c
import pigpio
from time import sleep
pi = pigpio.pi()
#print("i think it's working")
#ledpin = 33				# PWM pin connected to LED
#ledpin2 = 32				# PWM pin connected to LED
#GPIO.setwarnings(False)			#disable warnings
#GPIO.setmode(GPIO.BOARD)		#set pin numbering system
#GPIO.setup(ledpin,GPIO.OUT)
#GPIO.setup(ledpin2,GPIO.OUT)
#pi_pwm = GPIO.PWM(ledpin,255)		#create PWM instance with frequency
#pi_pwm2 = GPIO.PWM(ledpin2,255)		#create PWM instance with frequency
#pi_pwm.start(0)				#start PWM of required Duty Cycle 
#pi_pwm2.start(0)
#pigpio.start()				#start PWM of required Duty Cycle 
random = 1
for applesauce in range(1,100):
     pi.write(12,1)
     pi.write(13,1)
     sleep(.01)
while True:
     sleep(.05)
     duty = 50
     pi.write(12,0)
     pi.write(13,0)
     if(random == 1):
          print("this sucks")
          random= random+1
    
#pigpio.stop()
#    for duty in range(20,80):
#     pi_pwm.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
#     pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100        
#     sleep(0.01)
#    
#while True:
#    duty=100
#    pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#    pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#    sleep(.02)

#    duty=0
#    pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#    pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100

#    sleep(.02)
    #for duty in range(20,80):
     #   pi_pwm.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
      #  pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100        
       # sleep(0.01)
  
