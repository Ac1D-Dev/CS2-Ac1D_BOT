import discord
import services.faceit_api as faceit_api
import ui.embeds as embeds
import core.utils as utils
import core.nicknames as nicknames




def setup(bot, FACEIT_KEY):

    @bot.tree.command(name="compare", description="Compare 2 players FaceIt stats")
    @discord.app_commands.checks.cooldown(1, 10)

    @discord.app_commands.describe(player_1= "First Player")
    @discord.app_commands.rename(player_1= "player_1")
    @discord.app_commands.describe(player_2= "Second Player")
    @discord.app_commands.rename(player_2= "player_2")

    @discord.app_commands.describe(pseudo_1= "First Player")
    @discord.app_commands.rename(pseudo_1= "pseudo_1")
    @discord.app_commands.describe(pseudo_2= "Second Player")
    @discord.app_commands.rename(pseudo_2= "pseudo_2")

    async def compare(interaction : discord.Interaction,pseudo_1: str = None, pseudo_2: str = None, player_1: discord.Member = None, player_2: discord.Member = None):

        if player_1 is not None:
            discord_id = str(player_1.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                player_1 = data[discord_id]
            else:
                embed= discord.Embed(title="-> Player 1 <- No Account Linked -", color=utils.color_per_level[1])
                embed.add_field(name="No Account Link With /setnick",value= "", inline=True)
                await interaction.response.send_message(embed=embed)
                return

        elif pseudo_1 is not None:
            player_1 = pseudo_1

        else:
            discord_id = str(interaction.user.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                player_1 = data[discord_id]
            else:
                embed= discord.Embed(title="-> Player 1 <- No Account Linked -", color=utils.color_per_level[1])
                embed.add_field(name="No Account Link With /setnick",value= "", inline=True)
                await interaction.response.send_message(embed=embed)
                return

        if player_2 is not None:
            discord_id = str(player_2.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                player_2 = data[discord_id]
            else:
                embed= discord.Embed(title="-> Player 2 <- No Account Linked -", color=utils.color_per_level[1])
                embed.add_field(name="No Account Link With /setnick",value= "", inline=True)
                await interaction.response.send_message(embed=embed)
                return


        elif pseudo_2 is not None:
            player_2 = pseudo_2

        else:
            discord_id = str(interaction.user.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                player_2 = data[discord_id]
            else:
                embed= discord.Embed(title="-> Player 2 <- No Account Linked -", color=utils.color_per_level[1])
                embed.add_field(name="No Account Link With /setnick",value= "", inline=True)
                await interaction.response.send_message(embed=embed)
                return  



        if player_1 == player_2:
            embed = discord.Embed(title=" - Invalid Comparison - ")

            embed.add_field(name="Error : ", value="** Invalid Comparison due to Same Account Name **")

            await interaction.response.send_message(embed=embed)
            return

        stats1 = await faceit_api.faceit_key(bot, player_1, FACEIT_KEY, interaction)
        if not isinstance(stats1, dict):
            return  
        
        stats2 = await faceit_api.faceit_key(bot, player_2, FACEIT_KEY, interaction)
        if not isinstance(stats2, dict):
            return
        
        embed = embeds.compare_embed(stats1, stats2)

        await interaction.response.send_message(embed= embed)