import discord
import datetime

def setup(bot):

    latency = bot.latency * 1000
    ms = round(latency, 2)

    @bot.tree.command(name="ping", description="Detection Test for development")
    async def ping(interaction: discord.Interaction):
        latency = bot.latency * 1000
        ms = round(latency, 2)

        embed = discord.Embed(title=f"- Ping Test -")
        embed.add_field(name= "", value=f"**Ping : {ms} ms\n**", inline=True)
        embed.add_field(name="", value=f"**\nCS2 Bot Tracker is Connected**")
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed= embed)