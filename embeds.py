import discord
import datetime


from utils import color_per_level

def on_app_command_error_embed(error, ms):
    embed = discord.Embed(title= "",description=f"❌ ​**⏱️ Active CoolDown ** ❌​\n"
                                                f"\n➡️ ** Retry in {error.retry_after:.1f} secondes ** ⬅️​",
                                                color= color_per_level[1])
    
    embed.set_footer(text= f"Ac1D - TrackerBot | CS2 |  ~ {ms} ms")
    embed.timestamp = datetime.datetime.now()
    return embed

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