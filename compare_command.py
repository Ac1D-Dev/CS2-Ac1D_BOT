import discord
import faceit_api
import embeds




def setup(bot, FACEIT_KEY):

    @bot.tree.command(name="compare", description="Compare 2 players FaceIt stats")
    @discord.app_commands.describe(pseudo_1= "First Player")
    @discord.app_commands.rename(pseudo_1= "account_name_1")
    @discord.app_commands.describe(pseudo_2= "Second Player")
    @discord.app_commands.rename(pseudo_2= "account_name_2")

    async def compare(interaction : discord.Interaction, pseudo_1: str, pseudo_2: str):

        stats1 = await faceit_api.faceit_key(bot, pseudo_1, FACEIT_KEY, interaction)
        if not isinstance(stats1, dict):
            return  
        
        stats2 = await faceit_api.faceit_key(bot, pseudo_2, FACEIT_KEY, interaction)
        if not isinstance(stats2, dict):
            return
        
        embed = embeds.compare_embed(stats1, stats2)

        await interaction.response.send_message(embed= embed)