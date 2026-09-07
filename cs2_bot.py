import requests
import os
import discord

from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
FACEIT_KEY= os.getenv("FACEIT_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connect as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Connection Established !")

@bot.command()
async def faceit(ctx, pseudo):

    data = {"Authorization": "Bearer " + FACEIT_KEY }
    reponse = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pseudo}", headers=data)
    donnee = reponse.json()

    level = donnee["games"]["cs2"]["skill_level"]
    elo = donnee["games"]["cs2"]["faceit_elo"]

    embed = discord.Embed(title= "- FaceIt Stats {pseudo} -", color=discord.Color.green())
    embed.add_field(name= "Level", value= level, inline=True)
    embed.add_field(name= "Elo", value= elo, inline=True)

    await ctx.send(embed=embed)

bot.run(TOKEN)