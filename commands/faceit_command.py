import requests
import discord
import core.utils as utils
import ui.embeds as embeds
import ui.views as views
import services.faceit_api as faceit_api
import core.nicknames as nicknames

def setup(bot, FACEIT_KEY):

    @discord.app_commands.checks.cooldown(1, 10)

    @bot.tree.command(name="faceit", description="Display player FaceIt stats")
    async def faceit(interaction: discord.Interaction, pseudo: str = None):

        try:
            if pseudo is None:
                data = nicknames.load_data(nicknames.NICKNAME_FILE)
                discord_id = str(interaction.user.id)

                if discord_id not in data:
                    embed= discord.Embed(title="- No Account Linked -", color=utils.color_per_level[1])
                    embed.add_field(name="You need to enter a nickname or use /setnick first.",value= "", inline=True)
                    await interaction.response.send_message(embed=embed)
                    return  
                pseudo = data[discord_id]


            stats = await faceit_api.faceit_key(bot, pseudo, FACEIT_KEY, interaction)

            if not isinstance(stats, dict):
                return
            
            embed = embeds.default_embed(stats)
            stats_view = views.ViewStats(stats= stats)
            await interaction.response.send_message(embed=embed, view=stats_view)
            stats_view.message = await interaction.original_response()

        except requests.exceptions.ConnectionError:
            embed = discord.Embed(title= "- FaceIt Server Unjoinable -", color=utils.color_per_level[1])


            await interaction.response.send_message(embed=embed)

        except KeyError:
            embed = discord.Embed(title= "- UNKNOWN PLAYER -", color=utils.color_per_level[1])

            embed.add_field(name= f"{pseudo}",value= " is not a valid pseudo", inline=True)
            await interaction.response.send_message(embed=embed)