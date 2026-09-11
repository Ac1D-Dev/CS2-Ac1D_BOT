import discord

def setup(bot):

    @bot.tree.command(name="ping", description="Detection Test for development")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f"Connection Established {bot.user} !")