#! /bin/python3

# discord dependancies
import discord
import asyncio

# servo dependancies
import RPi.GPIO as GPIO
from time import sleep

#initialize servos
#https://www.electronicwings.com/raspberry-pi/raspberry-pi-pwm-generation-using-python-and-c
ledpin = 33				# PWM pin connected to LED
ledpin2 = 32				# PWM pin connected to LED
#GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(ledpin2,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,255)		#create PWM instance with frequency
pi_pwm2 = GPIO.PWM(ledpin2,255)		#create PWM instance with frequency
pi_pwm.start(50)				#start PWM of required Duty Cycle 
pi_pwm2.start(50)				#start PWM of required Duty Cycle 


botChannelId=803765954138996777 #bot channel id

print("starting bot...")
mazeAngle = [0.0,0.0]

class MyClient(discord.Client):

    mazeAngle = [0.0,0.0]
    deltaCommands=[]

    async def updateLoop(self):
        botChannel=self.get_channel(botChannelId)
        while True:

            duty1=(mazeAngle[0]+1)*50
            duty2=(mazeAngle[1]+1)*50
            pi_pwm.ChangeDutyCycle(duty1) #provide duty cycle in the range 0-100
            pi_pwm2.ChangeDutyCycle(duty2) #provide duty cycle in the range 0-100

            #delay
            await asyncio.sleep(1)

            #do calculation 
            totalRequests = len(self.deltaCommands)

            #temporary vars
            deltaMazeAngle = [0.0,0.0]
            xRequests=0
            yRequests=0

            #get sum
            # TODO: restrict players to one command per cycle
            # FIXME: surely there must be an easier way to get the sums.
            if len(self.deltaCommands)>0:
                for request in self.deltaCommands[0:totalRequests]:
                    request = request[1]
                    if request == "w":
                        yRequests+=1
                        deltaMazeAngle[1]+=1
                    elif request == "s":
                        yRequests+=1
                        deltaMazeAngle[1]-=1

                    elif request == "a":
                        xRequests+=1
                        deltaMazeAngle[0]-=1
                    elif request == "d":
                        xRequests+=1
                        deltaMazeAngle[0]+=1

            #get average
            if xRequests > 0:
                deltaMazeAngle[0]=deltaMazeAngle[0]/xRequests
            if yRequests > 0:
                deltaMazeAngle[1]=deltaMazeAngle[1]/yRequests


            #calculate new angle
            self.mazeAngle[0]+=deltaMazeAngle[0]
            self.mazeAngle[1]+=deltaMazeAngle[1]

            #make sure angle never goes above 1 or below -1
            #https://www.tutorialspoint.com/How-to-clamp-floating-numbers-in-Python
            self.mazeAngle[0] = max(min(self.mazeAngle[0], 1), -1)
            self.mazeAngle[1] = max(min(self.mazeAngle[1], 1), -1)


            #debug: send deltaMazeAngle
            await botChannel.send(self.mazeAngle)


            #remove processed requests. save unprocessed requests for next cycle.
            del self.deltaCommands[0:totalRequests]




    async def on_ready(self):
        print('Logged on as', self.user)
        await self.get_channel(botChannelId).send('Hello World!')

        self.deltaCommands = []
        await self.updateLoop()

    async def on_message(self, message):
        botChannel=self.get_channel(botChannelId)

        if message.channel != botChannel:
            return

        if message.author == self.user:
            return

        if message.content == "hello there":
            await botChannel.send('General Kenobi!')

        if message.content == "w":
            self.deltaCommands.append([message.author.id,"w"])
        if message.content == "a":
            self.deltaCommands.append([message.author.id,"a"])
        if message.content == "s":
            self.deltaCommands.append([message.author.id,"s"])
        if message.content == "d":
            self.deltaCommands.append([message.author.id,"d"])


    
        
    

#start bot
client = MyClient()
client.run(open("token.txt","r").readline())


while True:
    duty1=(mazeAngle[0]+1)*50
    duty2=(mazeAngle[1]+1)*50
    pi_pwm.ChangeDutyCycle(duty1) #provide duty cycle in the range 0-100
    pi_pwm2.ChangeDutyCycle(duty2) #provide duty cycle in the range 0-100
    sleep(0.1)

    #for duty in range(20,80):
     #   pi_pwm.ChangeDutyCycle(100-duty) #provide duty cycle in the range 0-100
      #  pi_pwm2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100        
       # sleep(0.01)
    
