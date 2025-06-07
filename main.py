import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio
from collections import deque
from flask import Flask
from threading import Thread


from keep_alive import keep_alive 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
   await bot.tree.sync()
   print(f'{bot.user} has connected to Discord!')
   print(f'Bot is online!')
   print(f'Bot is ready!')

   @bot.event
   async def on_message(message):
       if message.author == bot.user:
           return

       if message.content.startswith('hello'):
           await message.channel.send(f'Hello {message.author.name}!')

@bot.tree.command(name='ping', description='Replies with Pong!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! {round(bot.latency * 1000)}ms')

@bot.tree.command(name='hello', description='Replies with Hello!')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.name}!')

@bot.tree.command(name='add', description='Adds two numbers together!')
async def add(interaction: discord.Interaction, num1: int, num2: int):
    await interaction.response.send_message(f'{num1} + {num2} = {num1 + num2}')








