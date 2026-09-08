# Imports
import requests
import os
import discord
import datetime

# Imports spécifiques
from discord.ext import commands
from dotenv import load_dotenv


#ouverture .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
FACEIT_KEY= os.getenv("FACEIT_API_KEY")

# Dictionnaires couleur par niveau faceit (1 -> 10) (Gris -> Rouge) 
color_per_level = {
    1: discord.Color.greyple(),
    2: discord.Color.green(), 3: discord.Color.green(),
    4: discord.Color.yellow(), 5: discord.Color.yellow(), 6: discord.Color.yellow(), 7: discord.Color.yellow(),
    8: discord.Color.orange(), 9: discord.Color.orange(),
    10: discord.Color.red()
    }

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
        player_pseudo = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pseudo}", headers=api_data)
        player_info = player_pseudo.json()
        print(player_info)

        player_id = player_info["player_id"]
        avatar = player_info["avatar"]
        
        api_data_2 = {"Authorization": "Bearer " + FACEIT_KEY }
        player_stats = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/cs2", headers=api_data_2)
        info_stats = player_stats.json()

        level = player_info["games"]["cs2"]["skill_level"]
        elo = player_info["games"]["cs2"]["faceit_elo"]


        matchs = info_stats["lifetime"]["Matches"]
        winrate = info_stats["lifetime"]["Win Rate %"]
        avgkd = info_stats["lifetime"]["Average K/D Ratio"]
        adr = info_stats["lifetime"]["ADR"]
        hsavg = info_stats["lifetime"]["Average Headshots %"]
        wins = info_stats["lifetime"]["Wins"]
        cwinstreak = info_stats["lifetime"]["Current Win Streak"]
        lwinstreak = info_stats["lifetime"]["Longest Win Streak"]

        latency = bot.latency * 1000
        ms = round(latency, 2)

        embed = discord.Embed(title= f"- FaceIt Stats {pseudo} -", color= color_per_level[level])
        embed.set_thumbnail(url=avatar)
        embed.add_field(name= "​​Level", value= level, inline=True)
        embed.add_field(name= "Elo", value= elo, inline=True)
        embed.add_field(name= "Matches", value= matchs, inline=True)
        embed.add_field(name= "Avg K/D", value= avgkd, inline=True)
        embed.add_field(name= "Current Win Streak", value= cwinstreak, inline=True)
        embed.add_field(name= "Wins", value= wins, inline=True)
        embed.add_field(name= "Average Headshot %", value= hsavg, inline=True)
        embed.add_field(name= "ADR", value= adr, inline=True)
        embed.add_field(name= "WinRate %", value= winrate, inline=True)
        embed.add_field(name= "Longest Win Streak", value= lwinstreak, inline=True)
        embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {ms} ms")
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed=embed)

    except KeyError:

        embed = discord.Embed(title= "- UNKNOWN PLAYER -", color=color_per_level[1])
        embed.add_field(name= f"​❓{pseudo}​❓",value= " is not a valid pseudo", inline=True)
        await interaction.response.send_message(embed=embed)

bot.run(TOKEN)