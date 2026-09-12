# Imports
import os
import discord
import embeds
import faceit_command
import ping_command
import compare_command

# Imports spécifiques
from discord.ext import commands
from dotenv import load_dotenv


#ouverture .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
FACEIT_KEY= os.getenv("FACEIT_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "!", intents=intents)

ping_command.setup(bot)
faceit_command.setup(bot, FACEIT_KEY)
compare_command.setup(bot, FACEIT_KEY)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Connect as {bot.user}")

@bot.tree.error
async def on_app_command_error(interaction, error):
    latency = bot.latency * 1000
    ms = round(latency, 2)

    if isinstance(error, discord.app_commands.CommandOnCooldown):
        embed = embeds.on_app_command_error_embed(error, ms)
        await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(TOKEN)