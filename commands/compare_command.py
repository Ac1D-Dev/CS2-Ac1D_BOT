import discord
import services.faceit_api as faceit_api
import ui.embeds as embeds
import core.utils as utils
import core.nicknames as nicknames




def setup(bot, FACEIT_KEY):

    @bot.tree.command(name="compare", description="Compare 2 players FaceIt stats")
    @discord.app_commands.checks.cooldown(1, 10)

    @discord.app_commands.describe(member_1= "Mention the 1st player (linked Discord account)")
    @discord.app_commands.rename(member_1= "member_1")
    @discord.app_commands.describe(member_2= "Mention the 2nd player (linked Discord account)")
    @discord.app_commands.rename(member_2= "member_2")

    @discord.app_commands.describe(pseudo_1= "Or type the 1st player's FaceIt nickname directly")
    @discord.app_commands.rename(pseudo_1= "pseudo_1")
    @discord.app_commands.describe(pseudo_2= "Or type the 2nd player's FaceIt nickname directly")
    @discord.app_commands.rename(pseudo_2= "pseudo_2")

    async def compare(interaction : discord.Interaction,pseudo_1: str = None, pseudo_2: str = None, member_1: discord.Member = None, member_2: discord.Member = None):

        if member_1 is not None:
            faceit_id = str(member_1.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if faceit_id in data:
                member_1 = data[faceit_id]
            else:
                embed = discord.Embed(  title="❌ Account Not Linked",
                                        description=f"{member_1} doesn't have a FaceIt account linked."
                                                    " Use `/setnick` to link one,"
                                                    " or type a nickname directly.",
                                        color=utils.color_per_level[1])
                await interaction.response.send_message(embed=embed)
                return

        elif pseudo_1 is not None:
            member_1 = pseudo_1

        else:
            discord_id = str(interaction.user.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                member_1 = data[discord_id]
            else:
                embed = discord.Embed(  title="❌ Account Not Linked",
                                        description=f"You don't have a FaceIt account linked."
                                                    " Use `/setnick` to link one,"
                                                    " or type a nickname directly.",
                                        color=utils.color_per_level[1])
                await interaction.response.send_message(embed=embed)
                return

        if member_2 is not None:
            faceit_id = str(member_2.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if faceit_id in data:
                member_2 = data[faceit_id]
            else:
                embed = discord.Embed(  title="❌ Account Not Linked",
                                        description=f"{member_2} doesn't have a FaceIt account linked."
                                                    " Use `/setnick` to link one,"
                                                    " or type a nickname directly.",
                                        color=utils.color_per_level[1])
                await interaction.response.send_message(embed=embed)
                return


        elif pseudo_2 is not None:
            member_2 = pseudo_2

        else:
            discord_id = str(interaction.user.id)
            data = nicknames.load_data(nicknames.NICKNAME_FILE)

            if discord_id in data:
                member_2 = data[discord_id]
            else:
                embed = discord.Embed(  title="❌ Account Not Linked",
                                        description=f"You don't have a FaceIt account linked."
                                                    " Use `/setnick` to link one,"
                                                    " or type a nickname directly.",
                                        color=utils.color_per_level[1])
                await interaction.response.send_message(embed=embed)
                return  



        if member_1 == member_2:
            embed = discord.Embed(title=" - Invalid Comparison - ")

            embed.add_field(name="Error : ", value="** Invalid Comparison due to Same Account Name **")

            await interaction.response.send_message(embed=embed)
            return

        stats1 = await faceit_api.faceit_key(bot, member_1, FACEIT_KEY, interaction)
        if not isinstance(stats1, dict):
            return  
        
        stats2 = await faceit_api.faceit_key(bot, member_2, FACEIT_KEY, interaction)
        if not isinstance(stats2, dict):
            return
        
        embed = embeds.compare_embed(stats1, stats2)

        await interaction.response.send_message(embed= embed)