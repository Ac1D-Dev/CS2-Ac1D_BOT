import discord 
import ui.embeds as embeds
import core.nicknames as nicknames
import core.utils as utils
import core.commands_info as commands_info

class ViewMenu(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.select(
        placeholder="Choose a command",
        options= commands_info.option_objects
        )

    async def menu_select(self, interaction: discord.Interaction, select: discord.ui.Select):
        latency = interaction.client.latency * 1000
        ms = round(latency, 2)

        command = commands_info.get_command(select.values[0])
        embed = embeds.command_detail_embed(command, ms)


        await interaction.response.edit_message(embed=embed)

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

class ViewProfile(discord.ui.View):
    def __init__(self, pseudo_faceit):
        super().__init__()
        self.pseudo_faceit = pseudo_faceit


    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)

    async def confirm(self, interaction, button):
        discord_id = str(interaction.user.id)

        data = nicknames.load_data(nicknames.NICKNAME_FILE)
        data[discord_id] = self.pseudo_faceit['pseudo']
        nicknames.save_data(nicknames.NICKNAME_FILE, data)

        embed = discord.Embed(title= "** - Confirmed - **", color= utils.color_per_level[self.pseudo_faceit['level']])
        embed.add_field(name=f"** Discord User Account **", value=f"** \n {interaction.user} **", inline=True)
        embed.add_field(name="FaceIt Account",value=f"\n {self.pseudo_faceit['pseudo']} \n"
                                                    f"\n🎖️ Level : {self.pseudo_faceit['level']} \n"
                                                    f"\n📈 Elo : {self.pseudo_faceit['elo']} ",inline=True)
        
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.red)

    async def deny(self,  interaction: discord.Interaction, button: discord.ui.Button):
    
        
        embed = discord.Embed(title= "** - Denied - **", color= utils.color_per_level[10])
        embed.add_field(name=f"** Interruption: **", value=f"** Link Process Denied **", inline=True)
        
        
                
        await interaction.response.edit_message(embed=embed, view=None)
