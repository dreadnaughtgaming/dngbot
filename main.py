import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])

token = os.environ.get("Y8RKSjqFDS2hQ4sccnY1_vmQP8mGwSm2")
client.run(token)
