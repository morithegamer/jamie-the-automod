
# Ultimate AutoMod Bot (Enhanced) 🚀

A powerful, modular AutoMod Discord bot with advanced moderation features.

## 🚀 Features
- Advanced AutoMod with Banned Words and Regex Filtering.
- Phishing Detection (Regex and URL Control).
- Rich Embed Logging System.
- Dynamic Settings Control (Admin Command Panel).

## ✅ Commands
- `!addregex <pattern>` - Add a custom regex filter.
- `!removeregex <pattern>` - Remove a regex filter.
- `!setlog <#channel>` - Set the logging channel.
- `!settings` - View current settings.

## 🚀 Deployment (Local)
1. Install dependencies:
   ```bash
   pip install discord.py
   ```
2. Set your bot token in an `.env` file:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

## 🌐 Deployment (Docker)
1. Build the Docker image:
   ```bash
   docker build -t automod-bot .
   ```
2. Run the Docker container:
   ```bash
   docker run -d --name automod-bot -e DISCORD_TOKEN=your_bot_token automod-bot
   ```
