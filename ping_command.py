import discord
import datetime
import utils

def setup(bot):

    @bot.tree.command(name="ping", description="Detection Test for development")
    async def ping(interaction: discord.Interaction):
        latency = bot.latency * 1000
        ms = round(latency, 2)

        embed = discord.Embed(title=f"- Ping Test -" ,color= utils.color_per_level[8])
        embed.add_field(name= "", value=f"**Ping : {ms} ms\n**"
                                        f"**CS2 Bot Tracker is Connected**", inline=True)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed= embed)