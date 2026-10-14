import discord
import core.nicknames as nicknames
import ui.embeds as embeds 

def setup(bot):

    @discord.app_commands.checks.cooldown(1, 10)

    @bot.tree.command(name="unlink", description="Unlink your Discord account from Faceit Pseudo")
    async def unlink(interaction: discord.Interaction):
        discord_id = str(interaction.user.id)
        data = nicknames.load_data(nicknames.NICKNAME_FILE)

        if discord_id not in data:
            embed = embeds.not_linked()
            return await interaction.response.send_message(embed= embed)
        else: 
            nicknames.del_data(nicknames.NICKNAME_FILE, discord_id)
            embed = embeds.succ_del()
            return await interaction.response.send_message(embed= embed)