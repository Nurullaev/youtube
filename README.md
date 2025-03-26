# YouTube-DL Bot 🚀

A Telegram bot for downloading videos from YouTube, Instagram, TikTok, and X (Twitter) directly in your chats.

## Prerequisites 📋
- FFmpeg
```bash
$ sudo apt install ffmpeg
```

## Installation & Setup 🛠️

### 1. Install
```bash
$ git clone https://github.com/Nurullaev/youtube.git
$ cd youtube/bot
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -U get-video-properties
$ deactivate
$ sudo chmod -R 755 /opt/youtube/
$ nano /etc/systemd/system/youtube_bot.service
$ sudo systemctl enable youtube_bot.service
$ sudo systemctl daemon-reload
$ sudo systemctl start youtube_bot.service
$ sudo systemctl restart youtube_bot.service
```

### 2. Configure environment
Create a `.env` file with your Telegram bot token:
`TOKEN=your_telegram_bot_token_here`

### 3. Run the bot
```bash
$ python main.py
```
