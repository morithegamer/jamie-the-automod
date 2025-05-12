
# 🚀 Jamie - Your Favorite AutoMod Bot in the World! 💙

Hi, my name is **Jamie**, and I'm your favorite AutoMod in the world! I'm a powerful, customizable AutoMod bot for Discord, designed to keep your server safe and friendly with minimal effort.

### ✨ Features:
- **Advanced AutoMod:** Detect and block bad words, phishing links, and more.
- **Dynamic Settings Control:** Admins can easily customize settings without touching the code.
- **Rich Embed Logging:** Clean, stylish logs for deleted messages and warnings.
- **Custom Regex Filtering:** Block malicious URLs or any custom pattern.
- **Phishing Protection:** Secure your server from dangerous links.
- **Modular Design:** Each feature is in its own Cog, making it easy to extend.

---

### 🚀 How to Set Up Jamie:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Ultimate-AutoMod-Bot.git
   cd Ultimate-AutoMod-Bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Discord Token:**
   - Create a `.env` file with your bot token:
     ```env
     DISCORD_TOKEN=your_discord_bot_token_here
     ```

4. **Run the Bot:**
   ```bash
   python main.py
   ```

---

### 🌐 Deployment with Docker:
1. **Build the Docker Image:**
   ```bash
   docker build -t jamie-automod .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -d --name jamie-automod -e DISCORD_TOKEN=your_discord_bot_token jamie-automod
   ```

---

### 💡 Command List:
- `!addregex <pattern>` - Add a custom regex filter.
- `!removeregex <pattern>` - Remove a regex filter.
- `!setlog <#channel>` - Set the logging channel.
- `!settings` - View current settings.

---

### 💙 About Jamie:
Jamie is a friendly, cute, and reliable AutoMod designed to make server moderation effortless. Whether you're dealing with bad words, spam, or phishing links, Jamie has you covered.

---

### ⚡ Contribute and Support:
- Feel free to open issues or pull requests if you have suggestions.
- Share Jamie with others who need a strong AutoMod bot.

---

### ✅ MIT License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
