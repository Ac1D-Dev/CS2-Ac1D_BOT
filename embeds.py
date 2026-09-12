########################
#       Imports        #
########################

import discord
import datetime


from utils import color_per_level

##############################
#      Expired Function      #
##############################

def expired_embed(ms):
    embed = discord.Embed(title="", description="**⌛ Expired: ⌛\n**"
                                                "\n**Due to inactivity for 180 seconds.**",
                                                color= color_per_level[10])

    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {ms} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def on_app_command_error_embed(error, ms):
    embed = discord.Embed(title= "",description=f"❌ ​**⏱️ Active CoolDown ** ❌​\n"
                                                f"\n➡️ ** Retry in {error.retry_after:.1f} secondes ** ⬅️​",
                                                color= color_per_level[1])
    
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {ms} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

########################################
#       Menu Deroulant /faceit         #
########################################

def default_embed(stats):
    embed = discord.Embed(title=f"- Default Stats -", description=  f"Level {stats['level']} •"
                                                                    f" {stats['elo']} Elo •"
                                                                    f" {stats['matches']} Matchs\n",  
                                                                    color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**🎖️ Level**\n{stats['level']}\n"
                                    f"\n**🎯 Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**💥 Average Headshot %**\n{stats['hsavg']} %", inline=True)
    embed.add_field(name="", value= f"**📈 Elo**\n{stats['elo']}\n"
                                    f"\n**🔥 Current Winstreak**\n{stats['cwinstreak']}\n"
                                    f"\n**👑 Longest Winstreak**\n{stats['lwinstreak']}\n"
                                    f"\n**💣 ADR**\n{stats['adr']}", inline=True)
    embed.add_field(name="", value= f"**🎮 Matches**\n{stats['matches']}\n"
                                    f"\n**🏆 Wins**\n{stats['wins']}\n"
                                    f"\n**📊 Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def global_embed(stats):
    embed = discord.Embed(title=f"- Global Stats -",description=f"{stats['elo']} Elo •" 
                                                                f" {stats['wins']} Wins •"
                                                                f" {stats['winrate']} % WinRate\n",
                                                                color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**🎖️ Level**\n{stats['level']}\n"
                                    f"\n**🏆 Wins**\n{stats['wins']}", inline=True)
    embed.add_field(name="", value= f"**📈 Elo**\n{stats['elo']}\n"
                                    f"\n**📊 Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.add_field(name="", value= f"**🎮 Matches**\n{stats['matches']}\n", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def performance_embed(stats):
    embed = discord.Embed(title=f"- Performance Stats -", description=  f"Average K/D {stats['avgkd']} •" 
                                                                        f" {stats['adr']} ADR\n",
                                                                        color= color_per_level[stats["level"]])

    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**🎯 Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**💣 ADR**\n{stats['adr']}", inline=True)
    embed.add_field(name="", value= f"**💥 Average Headshot %**\n{stats['hsavg']} %\n"
                                    f"\n**📊 Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

def competitive_embed(stats):
    embed = discord.Embed(title=f"- Competitive Stats -",description=   f"Current Win Streak {stats['cwinstreak']} •" 
                                                                        f" Longest Win Streak {stats['lwinstreak']}\n",
                                                                        color= color_per_level[stats["level"]])
    
    embed.set_author(name=stats["pseudo"], icon_url=stats["avatar"])
    embed.add_field(name="", value= f"**💥 Average Headshot %**\n{stats['hsavg']} %\n"
                                    f"\n**📊 Win Rate %**\n{stats['winrate']} %", inline=True)
    embed.add_field(name="", value= f"**🎯 Average K/D**\n{stats['avgkd']}\n"
                                    f"\n**🔥 Current Winstreak**\n{stats['cwinstreak']}", inline=True)
    embed.add_field(name="", value= f"**🏆 Wins**\n{stats['wins']}\n"
                                    f"\n**👑 Longest Winstreak**\n{stats['lwinstreak']}", inline=True)
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats['ms']} ms")            
    embed.timestamp = datetime.datetime.now()
    return embed

############################################
#             Compare Command              #               
############################################

def comparator(stats1, stats2):
    stats1 = float(stats1)
    stats2 = float(stats2)

    difference = abs(stats1 - stats2)

    if stats1 > stats2:
        return f" 🔺** {difference:.1f} **"
    elif stats1 < stats2:
        return f" 🔻** {difference:.1f} **"
    else:
        return "🟰"

def compare_embed(stats1, stats2):
    level_comparator = comparator(stats1["level"], stats2["level"])
    avgkd_comparator = comparator(stats1["avgkd"], stats2["avgkd"])
    hsavg_comparator = comparator(stats1["hsavg"], stats2["hsavg"])
    elo_comparator = comparator(stats1['elo'], stats2["elo"])
    winrate_comparator = comparator(stats1["winrate"], stats2["winrate"])

    embed = discord.Embed(title=" - Comparison - ")
    embed.set_author(name=stats1["pseudo"], icon_url=stats1["avatar"])
    embed.add_field(name=stats1['pseudo'], value= f"**🎖️ Level**\n{stats1['level']}\n"
                                                f"\n**🎯 Average K/D**\n{stats1['avgkd']}\n"
                                                f"\n**💥 Average Headshot %**\n{stats1['hsavg']} %\n"
                                                f"\n**📈 Elo**\n{stats1['elo']}\n"
                                                f"\n**📊 Win Rate %**\n{stats1['winrate']} %", inline=True)

    embed.add_field(name="Comparator",value=f" **{level_comparator}**\n "      #Ce sont les stats du joueur1 qui sont comparés au joueur2 donc
                                            f"\n\n**{avgkd_comparator}**\n"    #si le joueur1 a une meilleure stats on verra 🔺 vert et a l'inverse un 🔻, avec          🔺
                                            f"\n\n**{hsavg_comparator}**\n"    #en dessous la valeur de difference par ex(kd joueur1 = 2 et kd joueur2 = 1.5 alors mettre 0.5)
                                            f"\n\n**{elo_comparator}**\n"
                                            f"\n\n**{winrate_comparator}**\n", inline=True)

    embed.add_field(name=stats2["pseudo"],value=f"**🎖️ Level**\n{stats2['level']}\n"
                                                f"\n**🎯 Average K/D**\n{stats2['avgkd']}\n"
                                                f"\n**💥 Average Headshot %**\n{stats2['hsavg']} %\n"
                                                f"\n**📈 Elo**\n{stats2['elo']}\n"
                                                f"\n**📊 Win Rate %**\n{stats2['winrate']} %", inline=True)

    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {stats1['ms']} ms")
    embed.timestamp = datetime.datetime.now()

    return embed