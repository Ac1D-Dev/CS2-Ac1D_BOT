import discord

COMMANDS = {
    "Stats": [
        {"name": "/faceit", "description": "📊 Look up a player's FaceIt stats — level, Elo, K/D and more",
                            "usage": "/faceit pseudo: faceit_pseudo",
                            "details": "Show stats from current selected player \n"
                            "You can mention linked Discord accounts or type FaceIt nicknames directly."},
        {"name": "/compare","description": "⚖️ Compare two players' FaceIt stats side by side",
                            "usage":"/compare member_1:@user member_2:@user",
                            "details":"Compares Elo, K/D, headshot % and win rate between two players. \n"
                            "You can mention linked Discord accounts or type FaceIt nicknames directly."},
        {"name": "/history", "description": "📜 Browse a player's recent matches: wins, losses and Elo changes",
                                "usage": "/history player: @user",
                                "details": "Explore more precise stats, recent matches: win / loss and Elo changes \n"
                                "You can mention linked Discord accounts or type FaceIt nicknames directly."},
        {"name": "/session", "description": "⏱️ Track your stats for the current play session",
                            "usage": "/session @user",
                            "details": "track current session stats \n"
                            "You can mention linked Discord accounts or type FaceIt nicknames directly."},
        {"name": "/maps", "description": "🗺️ See a player's win rate on each map",
                            "usage": "/maps @user",
                            "details": "See Player win rate on map \n"
                            "You can mention linked Discord accounts or type FaceIt nicknames directly."},
    ],
    "Social": [
        {"name": "/setnick", "description": "🔗 Link your Discord account to your FaceIt nickname",
                                "usage": "/setnick faceit_pseudo",
                                "details": "Link your Discord account to FaceIt Nickname, to simplify other commands. \n"
                                "You can mention linked Discord accounts or type FaceIt nicknames directly."},
        {"name": "/leaderboard", "description": "🏆 Rank server members by FaceIt Elo or level",
                                "usage": "/leaderboard",
                                "details": " Show Leaderboard by FaceIt Elo or Level for linked player"},
        {"name": "/profile", "description": "🪪 Check which FaceIt account a member is associated with.",
                                "usage": "/profile pseudo_faceit / @user",
                                "details": "Shows which FaceIt account this Discord account is connected to "},
    ],
    "Pro CS2": [
        {"name": "/matches", "description": "📅 See upcoming professional CS2 matches",
                            "usage": "/matches",
                            "details": "Show upcoming professional CS2 matches"},
        {"name": "/team", "description": "👥 Look up a pro team's roster and stats",
                            "usage": "/team",
                            "details": "Check pro team's roster and stats"},
        {"name": "/setchannelmatches", "description": "🔔 Choose the channel for automatic match notifications",
                                "usage":"/setchannel channel_ID",
                                "details":"Set a channel for automatic match notifications"},
    ],
    "Utils": [
        {"name": "/ping", "description": "📶 Check if the bot is online and responsive",
                            "usage": "/ping",
                            "details":"Test connectivity and stability"},
        {"name": "/veto", "description": "🗳️ Run a map ban/pick veto for your scrim",
                            "usage":"/veto",
                            "details":"Run a map ban/pick veto for your scrim"},
    ],
}

all_commands = []
for category, commands in COMMANDS.items():
    for command in commands:
        all_commands.append(command)

option_objects = []
for command in all_commands:
    option_objects.append(discord.SelectOption(label=command["name"], description=command["description"]))

def get_command(name):
    for command in all_commands:
        if command["name"] == name:
            return command
    return None