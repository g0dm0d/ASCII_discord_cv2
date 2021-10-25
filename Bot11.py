import discord
import os
import sys
import cv2
from PIL import Image
from discord import message
from discord.ext import commands
import time

ASCII_CHARS = ["@", "#", "/", "%", "?", "*", "+", ";", ":", ",", ".", "Z", "-", "_"]
def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = 20
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generate_frame(image,new_width=90):
	new_image_data = pix2chars(resized_gray_image(image,new_width=new_width))
	total_pixels = len(new_image_data)
	print(total_pixels)
	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])
	return "`"+ascii_image+"`"

client = commands.Bot(command_prefix = '.')

i = 11
@client.event
async def on_message(ctx):
	if ctx.author.id == 843215395895771166:
		global i
		isCreated = False
		msg = None
		img = Image.open(f"BadApple/frame{i}.jpg")
		frame = generate_frame(img,80)
		#time.sleep(0.03)
		if frame:
			if not isCreated:
				msg = await ctx.channel.send(frame)
			if isCreated:
				await msg.send(content=frame)
		i += 15
client.run('token')
