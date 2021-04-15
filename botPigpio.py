#! /bin/python3
import discord
import asyncio

import pigpio
from time import sleep

#pin1 = 13                             # PWM pin connected to LED
#pin2 = 12                            # PWM pin connected to LED
pi = pigpio.pi()



botChannelId=803765954138996777 #bot channel id

print("starting bot...")

#pi.set_mode(pin1, pigpio.OUTPUT)

class MyClient(discord.Client):
    mazeAngle = [0.0,0.0]
    xAxis = 0
    yAxis = 0
    xRequests = 0
    yRequests = 0
    #pigpio.start()

    async def updateLoop(self):
        botChannel=self.get_channel(botChannelId)
        while True:

            pi.set_servo_pulsewidth(12, ((self.mazeAngle[0]+1)*1000)+500)
            pi.set_servo_pulsewidth(13, ((self.mazeAngle[1]+1)*1000)+500)

            #sleep(1)
            await asyncio.sleep(1)

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
            #await botChannel.send(self.mazeAngle)

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
        if message.content == "w" or message.content == "W":
           self.yAxis+=1
           self.yRequests+=1
        if message.content == "a" or message.content == "A":
           self.xAxis-=1
           self.xRequests+=1
        if message.content == "s" or message.content == "S":
           self.yAxis-=1
           self.yRequests+=1
        if message.content == "d" or message.content == "D":
           self.xAxis+=1
           self.xRequests+=1

    #pigpio.stop()

#start bot
client = MyClient()
client.run(open("token.txt","r").readline())
