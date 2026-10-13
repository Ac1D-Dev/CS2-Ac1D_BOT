import core.nicknames as nicknames
import ui.embeds as embeds

async def get_faceit_pseudo(member_1, pseudo_1, interaction):
    if member_1 is not None:
        faceit_id = str(member_1.id)
        data = nicknames.load_data(nicknames.NICKNAME_FILE)
    
        if faceit_id in data:
            return data[faceit_id]
        else:
            embed = embeds.not_linked()
            await interaction.response.send_message(embed=embed)
            return None
    
    elif pseudo_1 is not None:
        return pseudo_1
    
    else:
        discord_id = str(interaction.user.id)
        data = nicknames.load_data(nicknames.NICKNAME_FILE)
    
        if discord_id in data:
            member_1 = data[discord_id]
            return member_1
        else:
            embed = embeds.not_linked()
            await interaction.response.send_message(embed=embed)
            return None