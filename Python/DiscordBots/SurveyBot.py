import discord
from discord.ext import commands
import configparser

config = configparser.RawConfigParser()
config.read('surveyBotConfig.properties')

token = config.get('BotTokenSection','bot.token')

client = discord.Client()
print (discord.__version__)

surveyResults = []

table = dict()

def checkKeys(id, message):

    for x in table.keys():
        if id == x:
            value = int(table.get(id))
            
            if value == 2:
                return "Sorry You Cannot Vote Anymore This Week (Max Of 3 Votes Per Week!)"

            value += 1
            entry = {id : value}
            table.update(entry)
            surveyResults.append(message)
            print(table)
            response = "You Voted For: " + str(message) + " This was your: " + str(value + 1) + " vote!"
            return response
    else:
        entry = {id : 0}
        table.update(entry)
        surveyResults.append(message)
        print(table)
        response ="You Voted For: " + str(message) + " This was your 1st Vote!"
        return response

@client.event
async def on_read():
    print('Bot is ready')

@client.event
async def on_message(message):

    if(message.author == client.user):
        return

    if(message.content == '!results'):
        await message.channel.send("Here are the results from the survey:")
        for x in surveyResults:
            await message.channel.send(x)
        return 
    else:
        response = checkKeys(message.author.id, message.content)
        await message.channel.send(response)

client.run(token)

