import discord
import datetime

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
        options= [discord.SelectOption(label="Default"),
                discord.SelectOption(label="Global"),
                discord.SelectOption(label="Competitive"),
                discord.SelectOption(label="Performance")]
    )

    async def preset_select(self, interaction: discord.Interaction, select: discord.ui.Select):

        select_preset = select.values[0]

        if select_preset == "Default":
            embed = default_embed(self.player_infos)

        elif select_preset == "Global":
            embed = discord.Embed(title=f"Global Stats", color= color_per_level[self.player_infos["level"]])

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="", value= f"**Level**\n{self.player_infos['level']}\n"
                                            f"\n**Wins**\n{self.player_infos['wins']}", inline=True)
            embed.add_field(name="", value= f"**Elo**\n{self.player_infos['elo']}\n"
                                            f"\n**Win Rate %**\n{self.player_infos['winrate']} %", inline=True)
            embed.add_field(name="", value= f"**Matches**\n{self.player_infos['matches']}\n", inline=True)
            embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {self.player_infos['ms']} ms")
            embed.timestamp = datetime.datetime.now()
            
        elif select_preset == "Performance":
            embed = discord.Embed(title=f"Performance Stats", color= color_per_level[self.player_infos["level"]])

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="", value= f"**Average K/D**\n{self.player_infos['avgkd']}\n"
                                            f"\n**ADR**\n{self.player_infos['adr']}", inline=True)
            embed.add_field(name="", value= f"**Average Headshot %**\n{self.player_infos['hsavg']} %\n"
                                            f"\n**Winrate**\n{self.player_infos['winrate']} %", inline=True)
            embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {self.player_infos['ms']} ms")
            embed.timestamp = datetime.datetime.now()

        elif select_preset == "Competitive":
            embed = discord.Embed(title=f"Competitive Stats", color= color_per_level[self.player_infos["level"]])

            embed.set_thumbnail(url=self.player_infos["avatar"])
            embed.add_field(name="", value= f"**Average Headshot % **\n{self.player_infos['hsavg']} %\n"
                                            f"\n**Win Rate %**\n{self.player_infos['winrate']} %", inline=True)
            embed.add_field(name="", value= f"**Average K/D**\n{self.player_infos['avgkd']}\n"
                                            f"\n**Current Winstreak**\n{self.player_infos['cwinstreak']}", inline=True)
            embed.add_field(name="", value= f"**Wins**\n{self.player_infos['wins']}"
                                            f"\n**Longest Winstreak**\n{self.player_infos['lwinstreak']}", inline=True)
            embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {self.player_infos['ms']} ms")            
            embed.timestamp = datetime.datetime.now()
        await interaction.response.edit_message(embed=embed)

def default_embed(stats):
    embed = discord.Embed(title= f"- FaceIt Stats {stats['pseudo']} -", color= color_per_level[stats["level"]])
    
    embed.set_thumbnail(url=stats["avatar"])
    embed.add_field(name="", value= f"**Level**\n{stats['level']}\n"
                                    f"\n**Average K/D**\n{stats['avgkd']}"
                                    f"\n**Average Headshot %**\n{stats['hsavg']} %", inline=True)
    embed.add_field(name="", value= f"**Elo**\n{stats['elo']}\n"
                                    f"\n**Current Winstreak**\n{stats['cwinstreak']}"
                                    f"\n**Longest Winstreak**\n{stats['lwinstreak']}"
                                    f"\n**ADR**\n{stats['adr']}", inline=True)
    embed.add_field(name="", value= f"**Matches**\n{stats['matches']}\n"
                                    f"\n**Wins**\n{stats['wins']}"
                                    f"\n**Win Rate %**\n{stats['winrate']} %", inline=True)
    
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed