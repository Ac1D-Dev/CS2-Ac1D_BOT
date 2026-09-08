import discord

###################################################################################


######################################> DICO <#####################################


####################################################################################

# Dictionnaires couleur par niveau faceit (1 -> 10) (Gris -> Rouge) 
color_per_level = {
    1: discord.Color.greyple(),
    2: discord.Color.green(), 3: discord.Color.green(),
    4: discord.Color.yellow(), 5: discord.Color.yellow(), 6: discord.Color.yellow(), 7: discord.Color.yellow(),
    8: discord.Color.orange(), 9: discord.Color.orange(),
    10: discord.Color.red()
    }





###################################################################################


#####################################> CLASS <#####################################


####################################################################################

class ViewMode(discord.ui.View):
    def __init__(self, player_infos):
        super().__init__()
        self.player_infos = player_infos

    @discord.ui.select(
        placeholder="Select a Preset",
        options= [discord.SelectOption(label="Global"),
                discord.SelectOption(label="Competitive"),
                discord.SelectOption(label="Performance")]
    )

    async def preset_select(self, interaction: discord.Interaction, select: discord.ui.Select):
        select_preset = select.values[0]
        embed = discord.Embed(title=f"{self.player_infos} select : {select_preset}")
        await interaction.response.edit_message(embed=embed)