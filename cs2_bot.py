# Imports
import requests
import os
import discord
import utils
import embeds
import errors
import views

# Imports spécifiques
from discord.ext import commands
from dotenv import load_dotenv



#ouverture .env
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

        api_pseudo = {"Authorization": "Bearer " + FACEIT_KEY }
        player_pseudo = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pseudo}", headers=api_pseudo)
        player_infos = player_pseudo.json()

        error = await errors.handle_error_status(player_pseudo, pseudo, interaction)
        if error:
            return error

        player_id = player_infos["player_id"]

        api_stats = {"Authorization": "Bearer " + FACEIT_KEY }
        player_stats = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}/stats/cs2", headers=api_stats)
        info_stats = player_stats.json()

        error = await errors.handle_error_status(player_stats, pseudo, interaction)
        if error:
            return error

        avatar = player_infos["avatar"]
        level = player_infos["games"]["cs2"]["skill_level"]
        elo = player_infos["games"]["cs2"]["faceit_elo"]

        matches = info_stats["lifetime"]["Matches"]
        winrate = info_stats["lifetime"]["Win Rate %"]
        avgkd = info_stats["lifetime"]["Average K/D Ratio"]
        adr = info_stats["lifetime"]["ADR"]
        hsavg = info_stats["lifetime"]["Average Headshots %"]
        wins = info_stats["lifetime"]["Wins"]
        cwinstreak = info_stats["lifetime"]["Current Win Streak"]
        lwinstreak = info_stats["lifetime"]["Longest Win Streak"]

        latency = bot.latency * 1000
        ms = round(latency, 2)

        stats = {
            "ms": ms, "pseudo": pseudo, "avatar": avatar,"level": level, "elo": elo, "matches": matches, "avgkd": avgkd,
            "cwinstreak": cwinstreak, "wins": wins, "hsavg": hsavg, "lwinstreak": lwinstreak,
            "winrate": winrate, "adr": adr 
        }

        embed = embeds.default_embed(stats)
        my_view = views.ViewMode(stats= stats)
        await interaction.response.send_message(embed=embed, view=my_view)

    except requests.exceptions.ConnectionError:
        embed = discord.Embed(title= "- FaceIt Server Unjoinable -", color=utils.color_per_level[1])

        
        await interaction.response.send_message(embed=embed)

    except KeyError:
        embed = discord.Embed(title= "- UNKNOWN PLAYER -", color=utils.color_per_level[1])

        embed.add_field(name= f"{pseudo}",value= " is not a valid pseudo", inline=True)
        await interaction.response.send_message(embed=embed)

bot.run(TOKEN)