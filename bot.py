#! /bin/python3
import discord

botChannelId=803765954138996777

print("starting bot...")

class MyClient(discord.Client):

    

    async def on_ready(self):
        print('Logged on as', self.user)
        await self.get_channel(botChannelId).send('Hello World!')

    async def on_message(self, message):
        botChannel=self.get_channel(botChannelId)

        if message.channel != botChannel:
            return

        if message.author == self.user:
            return

        if message.content == "hello there":
            await botChannel.send('General Kenobi!')

client = MyClient()
client.run(open("token.txt","r").readline())