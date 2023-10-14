import discord
from discord.ext import commands

# Replace this with your token
TOKEN = 'YOUR_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Responds with Hello!')
async def hello(ctx):
    await ctx.send('Hello!')

bot.run(TOKEN)
