import requests
import discord
import utils
import embeds
import views
import faceit_api

def setup(bot, FACEIT_KEY):

    @discord.app_commands.checks.cooldown(1, 10)

    @bot.tree.command(name="faceit", description="Display player FaceIt stats")
    async def faceit(interaction: discord.Interaction, pseudo: str):

        try:
            stats = await faceit_api.faceit_key(bot, pseudo, FACEIT_KEY, interaction)

            if not isinstance(stats, dict):
                return
            
            embed = embeds.default_embed(stats)
            my_view = views.ViewMode(stats= stats)
            await interaction.response.send_message(embed=embed, view=my_view)
            my_view.message = await interaction.original_response()

        except requests.exceptions.ConnectionError:
            embed = discord.Embed(title= "- FaceIt Server Unjoinable -", color=utils.color_per_level[1])


            await interaction.response.send_message(embed=embed)

        except KeyError:
            embed = discord.Embed(title= "- UNKNOWN PLAYER -", color=utils.color_per_level[1])

            embed.add_field(name= f"{pseudo}",value= " is not a valid pseudo", inline=True)
            await interaction.response.send_message(embed=embed)