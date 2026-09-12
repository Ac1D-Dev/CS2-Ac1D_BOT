import discord 
import embeds
import nicknames
import faceit_api
import utils

class ViewStats(discord.ui.View):
    def __init__(self, stats):
        super().__init__()
        self.stats = stats

    async def on_timeout(self):
        embed = embeds.expired_embed(self.stats["ms"])

        await self.message.edit(embed = embed, view=None)
        await super().on_timeout()
        


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
            embed = embeds.default_embed(self.stats)

        elif select_preset == "Global":
            embed = embeds.global_embed(self.stats)
            
        elif select_preset == "Performance":
            embed = embeds.performance_embed(self.stats)

        elif select_preset == "Competitive":
            embed = embeds.competitive_embed(self.stats)
        await interaction.response.edit_message(embed=embed)







NICKNAME_FILE = "nicknames.json"
class ViewProfile(discord.ui.View):
    def __init__(self, pseudo_faceit):
        super().__init__()
        self.pseudo_faceit = pseudo_faceit


    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)

    async def confirm(self, interaction, button):
        discord_id = str(interaction.user.id)

        data = nicknames.load_data(NICKNAME_FILE)
        data[discord_id] = self.pseudo_faceit['pseudo']
        nicknames.save_data(NICKNAME_FILE, data)

        embed = discord.Embed(title= "** - Confirmed - **", color= utils.color_per_level[4])
        embed.add_field(name=f"** Discord User Account -> {interaction.user} <- Linked to : **", value=f"** {self.pseudo_faceit['pseudo']} **", inline=True)
        
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.red)

    async def deny(self,  interaction: discord.Interaction, button: discord.ui.Button):
    
        
        embed = discord.Embed(title= "** - Denied - **", color= utils.color_per_level[10])
        embed.add_field(name=f"** Interruption: **", value=f"** Link Process Denied **", inline=True)
        
        
                
        await interaction.response.edit_message(embed=embed, view=None)
