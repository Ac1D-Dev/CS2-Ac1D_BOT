import discord
import datetime

from utils import color_per_level

def default_embed(stats):
    embed = discord.Embed(title= f"- FaceIt Stats {stats['pseudo']} -", color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**Level**\n{stats['level']}\n"
                                    f"\n**Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**Average Headshot %**\n{stats['hsavg']} %", inline=True)
    embed.add_field(name="", value= f"**Elo**\n{stats['elo']}\n"
                                    f"\n**Current Winstreak**\n{stats['cwinstreak']}\n"
                                    f"\n**Longest Winstreak**\n{stats['lwinstreak']}\n"
                                    f"\n**ADR**\n{stats['adr']}", inline=True)
    embed.add_field(name="", value= f"**Matches**\n{stats['matches']}\n"
                                    f"\n**Wins**\n{stats['wins']}\n"
                                    f"\n**Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def global_embed(stats):
    embed = discord.Embed(title=f"- Global Stats -", color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**Level**\n{stats['level']}\n"
                                    f"\n**Wins**\n{stats['wins']}", inline=True)
    embed.add_field(name="", value= f"**Elo**\n{stats['elo']}\n"
                                    f"\n**Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.add_field(name="", value= f"**Matches**\n{stats['matches']}\n", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def performance_embed(stats):
    embed = discord.Embed(title=f"- Performance Stats -", color= color_per_level[stats["level"]])

    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**ADR**\n{stats['adr']}", inline=True)
    embed.add_field(name="", value= f"**Average Headshot %**\n{stats['hsavg']} %\n"
                                    f"\n**Winrate**\n{stats['winrate']} %", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def competitive_embed(stats):
    embed = discord.Embed(title=f"- Competitive Stats -", color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**Average Headshot % **\n{stats['hsavg']} %\n"
                                    f"\n**Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.add_field(name="", value= f"**Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**Current Winstreak**\n{stats['cwinstreak']}", inline=True)
    embed.add_field(name="", value= f"**Wins**\n{stats['wins']}\n"
                                    f"\n**Longest Winstreak**\n{stats['lwinstreak']}", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")            
    embed.timestamp = datetime.datetime.now()
    return embed