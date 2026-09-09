import discord 

from utils import color_per_level

async def handle_error_status(response, pseudo, interaction):
    if response.status_code == 401:
        embed = discord.Embed(title= "**- Error 401 : Unauthorized -**", color=color_per_level[1])
    
        embed.add_field(name= f"401 :",value= " invalid Bot config", inline=True)
        await interaction.response.send_message(embed=embed)
        return True
            
    elif response.status_code == 404:
        embed = discord.Embed(title= "**- Error 404 : Not Found -**", color=color_per_level[1])
    
        embed.add_field(name= f"**404 :{pseudo} -**",value= " invalid pseudo", inline=True)
        await interaction.response.send_message(embed=embed)
        return True

    elif response.status_code == 429:
        embed = discord.Embed(title= "**- Error 429 : Too Many Requests -**", color=color_per_level[1])
        
        embed.add_field(name= f"**429 :**",value= " Too Many Requests", inline=True)
        await interaction.response.send_message(embed=embed)
        return True


    elif response.status_code >= 500:
        embed = discord.Embed(title= "**- Error 5xx (500-599) : FaceIt Server Failed -**", color=color_per_level[1])
        
        embed.add_field(name= f"**5xx :**",value= " Server Failed\n (Server Error / Bad Gateway / Service Unavailable)", inline=True)
        await interaction.response.send_message(embed=embed)
        return True
    
    return None