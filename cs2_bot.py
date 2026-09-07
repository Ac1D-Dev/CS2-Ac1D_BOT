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
    await bot.tree.sync()
    print(f"Connect as {bot.user}")

@bot.tree.command(name="ping", description="Detection Test for development")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Connection Established {bot.user} !")

@bot.tree.command(name="faceit", description="Display player FaceIt stats")
async def faceit(interaction: discord.Interaction, pseudo: str):

    try:

        api_data = {"Authorization": "Bearer " + FACEIT_KEY }
        reponse = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pseudo}", headers=api_data)
        player_info = reponse.json()

        player_id = player_info["player_id"]
        
        api_data_2 = {"Authorization": "Bearer " + FACEIT_KEY }
        player_stats = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/cs2", headers=api_data_2)
        info_stats = player_stats.json()


        level = player_info["games"]["cs2"]["skill_level"]
        elo = player_info["games"]["cs2"]["faceit_elo"]
        matchs = info_stats["lifetime"]["Matches"]
        winrate = info_stats["lifetime"]["Win Rate %"]
        avgkd = info_stats["lifetime"]["Average K/D Ratio"]
        adr = info_stats["lifetime"]["ADR"]


        embed = discord.Embed(title= f"- FaceIt Stats {pseudo} -", color=discord.Color.green())
        embed.add_field(name= "​​Level", value= level, inline=True)
        embed.add_field(name= "Elo", value= elo, inline=True)
        embed.add_field(name= "Matches", value= matchs, inline=True)
        embed.add_field(name= "WinRate %", value= winrate, inline=True)
        embed.add_field(name= "​Avg K/D", value= avgkd, inline=True)
        embed.add_field(name= "ADR", value= adr, inline=True)
        await interaction.response.send_message(embed=embed)
    except KeyError:
        embed = discord.Embed(title= "- UNKOWN PLAYER -", color=discord.Color.red())
        embed.add_field(name= f"{pseudo}",value= "is not a valid pseudo", inline=True)
        await interaction.response.send_message(embed=embed)

bot.run(TOKEN)