import discord
import ui.views as views
import ui.embeds as embeds

def setup(bot):

    @bot.tree.command(name="menu", description="Open menu with all commands and theme list")
    async def menu(interaction: discord.Interaction):
        latency = bot.latency * 1000
        ms = round(latency, 2)

        embed = embeds.menu_embed(ms)
        menu_view = views.ViewMenu()
        await interaction.response.send_message(embed=embed, view=menu_view)
        menu_view.message = await interaction.original_response()

