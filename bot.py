#! /bin/python3
import discord
import asyncio


import RPi.GPIO as GPIO
from time import sleep

ledpin = 33                             # PWM pin connected to LED
ledpin2 = 32                            # PWM pin connected to LED
GPIO.setwarnings(False)                 #disable warnings
GPIO.setmode(GPIO.BOARD)                #set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(ledpin2,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,255)           #create PWM instance with frequency
pi_pwm2 = GPIO.PWM(ledpin2,255)         #create PWM instance with frequency
pi_pwm.start(0)                         #start PWM of required Duty Cycle
pi_pwm2.start(0)                                #start PWM of required Duty Cycle




botChannelId=803765954138996777 #bot channel id

print("starting bot...")


class MyClient(discord.Client):
    mazeAngle = [0.0,0.0]
    xAxis = 0
    yAxis = 0
    xRequests = 0
    yRequests = 0

    async def updateLoop(self):
        botChannel=self.get_channel(botChannelId)
        while True:

            for covid in range(0,100):
                 duty = (self.mazeAngle[0]+1)*50
                 duty2 = (self.mazeAngle[1]+1)*50
                 pi_pwm.ChangeDutyCycle(duty)
                 pi_pwm2.ChangeDutyCycle(duty2)
                 sleep(.01)

            #reset tilt
            self.mazeAngle[0] = 0
            self.mazeAngle[1] = 0

            #get average
            if self.xRequests > 0:
                self.xAxis=self.xAxis/self.xRequests
            if self.yRequests > 0:
                self.yAxis=self.yAxis/self.yRequests

            #calculate new angle
            self.mazeAngle[0]+=self.xAxis
            self.mazeAngle[1]+=self.yAxis

            #reset variables
            self.xAxis=0
            self.yAxis=0
            self.yRequests=0
            self.xRequests=0

            #debug: send deltaMazeAngle
            await botChannel.send(self.mazeAngle)

    async def on_ready(self):
        print('Logged on as', self.user)
        await self.get_channel(botChannelId).send('Hello World!')
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
           self.yAxis+=1
           self.yRequests+=1
        if message.content == "a":
           self.xAxis-=1
           self.xRequests+=1
        if message.content == "s":
           self.yAxis-=1
           self.yRequests+=1
        if message.content == "d":
           self.xAxis+=1
           self.xRequests+=1

#start bot
client = MyClient()
client.run(open("token.txt","r").readline())
