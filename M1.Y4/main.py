import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def psw(ctx, count_heh = 5):
    await ctx.send( gen_pass(10))

@bot.command()
async def calculator(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)



bot.run("MTE2NTE5MzQ0OTQ2MTUxODMzNg.GTEIDu.CON0I7tmDYXcN0CV7u1syj9rrctWJ7cPD0a39w")