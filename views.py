import discord 
import embeds

class ViewMode(discord.ui.View):
    def __init__(self, stats):
        super().__init__()
        self.stats = stats

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