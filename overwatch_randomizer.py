#!/usr/bin/envython3
import discord
import random

# Role Lists
tank = ["D.VA", "Orisa", "Reinhardt", "Roadhog", "Sigma", 
        "Winston", "Wrecking Ball", "Zarya"]

damage = ["Ashe", "Bastion", "Doomfist", "Echo", "Genji", "Hanzo", 
        "Junkrat", "McCree", "Mei", "Pharah", "Reaper", "Soldier: 76", 
        "Sombra", "Symmetra", "Torbjorn", "Tracer", "Widowmaker"]

support = ["Ana", "Baptiste", "Brigitte", "Lucio", "Mercy", "Moira", "Zenyatta"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$tank'):
        choice = random.choice(tank)
        await message.channel.send(choice)
    elif message.content.startswith('$damage'):
        choice = random.choice(damage)
        await message.channel.send(choice)
    elif message.content.startswith('$support'):
        choice = random.choice(support)
        await message.channel.send(choice)

# Change out the X's with your own generated bot token.
client.run('XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
