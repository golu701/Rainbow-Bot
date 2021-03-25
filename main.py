import discord
import json
import sys
import asyncio
import traceback
from discord.ext import commands
import discord.utils

bot = commands.Bot(command_prefix=",")
bot.guild_id = "your_guild_id_remove_quotes"


@bot.event
async def on_ready():
    bot.loop.create_task(rainbowrole(rainbowrolename))
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Activity(type=discord.ActivityType.playing, name="With Colors"))
    print("The bot is {0.user}".format(bot))


rainbowrolename = "Rainbow"
delay = 30


async def rainbowrole(role):
    for role in bot.get_guild(bot.guild_id).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not bot.is_closed():
                try:
                    await role.edit(color=discord.Color.random())
                except Exception:
                    print(
                        "can't edit role, make sure the bot role is above the rainbow role and that is have the perms "
                        "to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename + '" not found')
    print("creating the role...")
    try:
        await bot.get_guild(bot.guild_id).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        bot.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        bot.loop.create_task(rainbowrole(rainbowrolename))


with open("./token.json", "r")as tokenjsonFile:
    configData = json.load(tokenjsonFile)
    TOKEN = configData["Discord_token"]
bot.run(TOKEN)
