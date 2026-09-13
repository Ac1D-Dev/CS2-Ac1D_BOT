
import discord
import services.faceit_api as faceit_api
import core.nicknames as nicknames
import core.utils as utils
import ui.views as views


def setup(bot, FACEIT_KEY):
    @bot.tree.command(name="setnick", description="Link a discord account to FaceIt Nickname")

    async def setnick( interaction: discord.Interaction, pseudo: str):
        pseudo_faceit = await faceit_api.faceit_key(bot, pseudo, FACEIT_KEY, interaction)

        if not isinstance(pseudo_faceit, dict):
            return 

        embed = discord.Embed(title= "setnick", color= utils.color_per_level[4])
        embed.add_field(name=f"Tu es sur le point de lier ton compte à {pseudo_faceit['pseudo']}, confirmer ?", value="", inline=True)
        
        profile_view = views.ViewProfile(pseudo_faceit= pseudo_faceit)
        await interaction.response.send_message(embed=embed, view=profile_view)
        profile_view.message = await interaction.original_response()