import discord
import datetime
import faceit_api

def setup(bot):

    latency = bot.latency * 1000
    ms = round(latency, 2)

    @bot.tree.command(name="ping", description="Detection Test for development")
    async def ping(interaction: discord.Interaction):
        embed = discord.Embed(title=f"- Ping Test -")
        
        embed.add_field(name=f"**Ping : {ms} ms\n**")
        embed.add_field(name=f"**\nCS2 Bot Tracker is Connected**")
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed= embed)