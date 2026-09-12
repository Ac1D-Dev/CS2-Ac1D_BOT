import discord
import faceit_api
import embeds
import utils
import nicknames




def setup(bot, FACEIT_KEY):

    @bot.tree.command(name="compare", description="Compare 2 players FaceIt stats")
    @discord.app_commands.checks.cooldown(1, 10)
    @discord.app_commands.describe(player_1= "First Player")
    @discord.app_commands.rename(player_1= "player_1")
    @discord.app_commands.describe(player_2= "Second Player")
    @discord.app_commands.rename(player_2= "player_2")

    async def compare(interaction : discord.Interaction, player_1: discord.Member = None, player_2: discord.Member = None):

        if player_1 is None:
            discord_id = str(interaction.user.id)
        else:
            discord_id = player_1.id

        key = str(discord_id)
        data = nicknames.load_data(nicknames.NICKNAME_FILE)

        if key not in data:
            embed= discord.Embed(title="-> Player 1 <- No Account Linked -", color=utils.color_per_level[1])
            embed.add_field(name=f"{player_1} need to enter a nickname or use /setnick first.",value= "", inline=True)
            await interaction.response.send_message(embed=embed)
            return  
        player_1 = data[key]

        if player_2 is None:
            discord_id = str(interaction.user.id)
        else:
            discord_id = player_2.id

        key = str(discord_id)
        data = nicknames.load_data(nicknames.NICKNAME_FILE)
        if key not in data:
            embed= discord.Embed(title="-> Player 2 <- No Account Linked -", color=utils.color_per_level[1])
            embed.add_field(name=f"{player_2} need to enter a nickname or use /setnick first.",value= "", inline=True)
            await interaction.response.send_message(embed=embed)
            return  
        player_2 = data[key]




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