import discord
import services.faceit_api as faceit_api
import ui.embeds as embeds
import core.player_resolver as player_resolver

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

        player_1_pseudo = await player_resolver.get_faceit_pseudo(member_1, pseudo_1, interaction)
        if player_1_pseudo is None:
            return

        player_2_pseudo = await player_resolver.get_faceit_pseudo(member_2, pseudo_2, interaction)
        if player_2_pseudo is None:
            return

        if player_1_pseudo == player_2_pseudo:
            embed = discord.Embed(title=" - Invalid Comparison - ")

            embed.add_field(name="Error : ", value="** Invalid Comparison due to Same Account Name **")

            await interaction.response.send_message(embed=embed)
            return

        stats1 = await faceit_api.faceit_key(bot, player_1_pseudo, FACEIT_KEY, interaction)
        if not isinstance(stats1, dict):
            return  
        
        stats2 = await faceit_api.faceit_key(bot, player_2_pseudo, FACEIT_KEY, interaction)
        if not isinstance(stats2, dict):
            return
        
        embed = embeds.compare_embed(stats1, stats2)

        await interaction.response.send_message(embed= embed)