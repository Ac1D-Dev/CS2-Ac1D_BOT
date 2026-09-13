# Cs2 Bot Tracker

A Discord bot that displays a player's **FACEIT** stats for **Counter-Strike 2** directly in Discord, with an interactive dropdown to switch between different stat presets.

## Features

- `/faceit [pseudo]` — fetches a player's FACEIT profile and CS2 lifetime stats, then displays them in a color-coded embed (color changes with the player's FACEIT skill level). Omit `pseudo` to use your own linked account (see `/setnick`).
- `/setnick <pseudo>` — links your Discord account to a FACEIT nickname, with a Confirm/Deny step before saving. Once linked, `/faceit` and `/compare` can use it automatically.
- `/compare` — compares two players' FACEIT stats side by side. For each player, either mention a Discord member (`member_1`/`member_2`) whose account is linked, or type a FACEIT nickname directly (`pseudo_1`/`pseudo_2`); if neither is given, defaults to your own linked account.
- Interactive preset dropdown under the `/faceit` embed to switch the view without re-running the command:
  - **Default** — full overview (level, elo, matches, K/D, headshot %, ADR, win streaks, win rate...)
  - **Global** — level, elo, matches, wins, win rate
  - **Performance** — K/D, ADR, headshot %, win rate
  - **Competitive** — headshot %, K/D, wins, win rate, win streaks
- Footer showing the bot's live ping and a timestamp on every embed.
- Clear error messages for common failure cases: invalid pseudo (404), bad/expired API key (401), rate limiting (429), FACEIT API outages (5xx), and unlinked accounts — instead of a generic crash.
- `/ping` — simple connectivity check.

## Tech stack

- Python 3
- [discord.py](https://discordpy.readthedocs.io/) 2.7.1 — Discord bot framework
- [requests](https://requests.readthedocs.io/) — HTTP calls to the FACEIT API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — loading secrets from a `.env` file

## Project structure

```
cs2_bot.py              # entry point: bot setup, command registration

commands/
    faceit_command.py    # /faceit
    compare_command.py   # /compare
    setnick_command.py   # /setnick
    ping_command.py      # /ping

ui/
    embeds.py            # builds embeds for stat presets, comparisons, and errors
    views.py             # dropdown UI for /faceit presets + confirm/deny buttons for /setnick

services/
    faceit_api.py        # FACEIT API calls

core/
    nicknames.py         # JSON persistence linking a Discord ID to a FACEIT pseudo
    utils.py              # shared constants (embed color per FACEIT level)
    errors.py              # maps FACEIT API error status codes to Discord messages
```

## Setup

1. Clone the repository and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a Discord application and bot at the [Discord Developer Portal](https://discord.com/developers/applications), and get a [FACEIT API key](https://developers.faceit.com/).

3. Create a `.env` file at the root of the project with:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   FACEIT_API_KEY=your_faceit_api_key
   ```

4. Run the bot:
   ```bash
   python cs2_bot.py
   ```

## Roadmap

- CS2 Premier mode stats via the Leetify API (no official Valve API exists for Premier rating).
- Tracking pro CS2 matches/teams, with notifications posted to a configurable channel.

## Author

Built by **Ac1D** as a personal project to learn Python and Discord bot development.
