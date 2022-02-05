import discord
import os
from keep_alive import keep_alive
import random
import time

client = discord.Client()


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

#ping command

    if message.content.startswith('.ping'):
        await message.channel.send('pong')
        print("pong")

#tod command

    tod_questions = [
        "Post an embarrassing picture of yourself",
        "Dm the first person in your dms I love you",
        "Who do you admire?",
        "Do you sleep with a stuffed animal?",
        "What's your favorite song?",
    ]

    if message.content.startswith('.tod'):
        await message.channel.send(random.choice(tod_questions))
        print("tod command used")


#8ball

    _8ball_awnsers = [
        "It is certain.",
        "It is decidedly.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As i see it,yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy,try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]

    if message.content.startswith('.8ball'):
        await message.channel.send(random.choice(_8ball_awnsers))
        print("8ball command used")

#anime commands

#show me rock

    if message.content.startswith('.rock'):
        await message.channel.send("SHOW ME ROCK!")
        time.sleep(1)
        await message.channel.send("https://tenor.com/view/gon-hunter-x-hunter-anime-rock-paper-scissors-attack-gif-17309978")
        print("rock command used")

keep_alive()
client.run(os.getenv('TOKEN'))
