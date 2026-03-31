# ScriptarwBot

A Twitch chat bot built with TwitchIO v2.

## Setup

### 1. Clone the repo
git clone https://github.com/yourname/twitch_bot.git
cd twitch_bot

### 2. Install dependencies
pip install twitchio python-dotenv

### 3. Configure credentials
Copy the example env file and fill in your own values:
cp .env.example .env

Then edit `.env` with:
- `BOT_USERNAME` — your bot's Twitch username
- `CHANNEL_NAME` — your Twitch channel name
- `OAUTH_TOKEN` — get it from https://twitchtokengenerator.com (prefix with `oauth:`)
- `CLIENT_ID` — from https://dev.twitch.tv/console
- `CLIENT_SECRET` — from https://dev.twitch.tv/console

## 4. Project Structure

Your repository should be organized like this:

```bash
twitch_bot/
├── bot.py
├── .env            # never committed (blocked by .gitignore)
├── .env.example    # committed, with placeholder values only
├── .gitignore      # committed
└── README.md       # committed
