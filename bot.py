#! /bin/python3
#allen testing branch
#http://32x8.com/
import discord
import asyncio

botChannelId=803765954138996777 #bot channel id

print("starting bot...")


class MyClient(discord.Client):

    mazeAngle = [0.0,0.0]
    deltaCommands=[]

    async def updateLoop(self):
        botChannel=self.get_channel(botChannelId)
        while True:

            #delay
            await asyncio.sleep(1)

            #do calculation 
            totalRequests = len(self.deltaCommands)

            #temporary vars
            deltaMazeAngle = [0.0,0.0]
            xRequests=0
            yRequests=0
            participatingUsers=[]

            #get sum
            # FIXME: surely there must be an easier way to get the sums.
            if len(self.deltaCommands)>0:
                for request in self.deltaCommands[0:totalRequests]:

                    if request[0] not in participatingUsers:
                        participatingUsers.append(request[0])

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