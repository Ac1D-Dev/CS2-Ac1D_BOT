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

        if select_preset == "Global":

            embed = discord.Embed(title=f"Global Stats")

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="Level", value=self.player_infos["level"], inline=True)
            embed.add_field(name="Elo", value=self.player_infos["elo"], inline=True)
            embed.add_field(name="Matches", value=self.player_infos["matches"], inline=True)
            embed.add_field(name="Wins", value=self.player_infos["wins"], inline=True)
            embed.add_field(name="Winrate", value=self.player_infos["winrate"], inline=True)
            

        elif select_preset == "Performance":

            embed = discord.Embed(title=f"Performance Stats")

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="Average K/D", value=self.player_infos["avgkd"], inline=True)
            embed.add_field(name="Winrate", value=self.player_infos["winrate"], inline=True)
            embed.add_field(name="Average Headshot %", value=self.player_infos["hsavg"], inline=True)
            embed.add_field(name="ADR", value=self.player_infos["adr"], inline=True)
            

        elif select_preset == "Competitive":

            embed = discord.Embed(title=f"Competitive Stats")

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="Average Headshot %", value=self.player_infos["hsavg"], inline=True)
            embed.add_field(name="Average K/D", value=self.player_infos["avgkd"], inline=True)
            embed.add_field(name="Wins", value=self.player_infos["wins"], inline=True)
            embed.add_field(name="Winrate", value=self.player_infos["winrate"], inline=True)
            embed.add_field(name="Current Win Streak", value=self.player_infos["cwinstreak"], inline=True)
            embed.add_field(name="Longest Win Streak", value=self.player_infos["lwinstreak"], inline=True)
            
        await interaction.response.edit_message(embed=embed)