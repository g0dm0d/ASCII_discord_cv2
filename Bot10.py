import discord
import os
import sys
from discord import message
from discord.ext import commands
client = commands.Bot(command_prefix = '!')

@client.event
async def on_message(ctx):
	if ctx.author.id == 279311290688602112:
		await ctx.channel.send('<@!277490621264953345> https://youtu.be/w1bz5PlvOMc')
client.run('ODQzMjE1Mzk1ODk1NzcxMTY2.YKAniA.gY7C0dGm_RqGDOaEdeurYdHH9fE')