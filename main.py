import discord
import os
from keep_alive import keep_alive
import random

tod_questions = [
    "I cant think of tod tod questions",
]

client = discord.Client()

@client.event
async def on_ready():
  print ("we have logged in as {0.user}"
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!ping'):
    await message.channel.send('pong')
    print ("pong")
    
  if message.content.startswith('!tod'):
    print ("tod command used")
    await message.channel.send(random.choice(tod_questions))

keep_alive()
client.run(os.getenv('TOKEN'))
