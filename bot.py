import discord
import os
import random
import pkg_resources
from discord.ext import commands
import asyncio
import aiml

STARTUP_FILE = "std-startup.xml"
BOT_PREFIX = ('!')



channel_name = 'CHANNELNAME'
token = 'BOT TOKEN'

aiml_kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    aiml_kernel.bootstrap(brainFile="bot_brain.brn")
else:
    aiml_kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    aiml_kernel.saveBrain("bot_brain.brn")

bot = commands.Bot(command_prefix=BOT_PREFIX)




@bot.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))

@bot.event
async def on_message(message):
    if message.author.bot or str(message.channel) != channel_name:
        return

    if message.content is None:
        print("Empty message received.")
        return

    print("Message: " + str(message.content))

    if message.content.startswith(BOT_PREFIX):
        return
    elif 'shutdown' in message.content and message.author.id == 173450781784145921:
        await bot.logout()
    else:
        aiml_response = aiml_kernel.respond(message.content)
        if aiml_response == '':
            await message.channel.send("I don't have a response for that, sorry.")
        else:
            print(aiml_response)
            await message.channel.send(aiml_response)

bot.run(token)