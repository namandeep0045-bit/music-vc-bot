# Music VC Bot 🎵🤖

Telegram के लिए एक Voice Chat Music Bot - YouTube से music play करता है!

## Features
- ✅ YouTube से music search और download
- ✅ Voice chat में music play करना
- ✅ Play, Pause, Resume, Stop controls
- ✅ Queue support
- ✅ Simple और easy to use

## Requirements
- Python 3.8+
- FFmpeg
- Telegram Bot Token

## Installation

### 1. FFmpeg Install करें

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
- Download करें: https://ffmpeg.org/download.html
- या: `choco install ffmpeg`

### 2. Repository clone करें
```bash
git clone https://github.com/namandeep0045-bit/music-vc-bot.git
cd music-vc-bot
```

### 3. Dependencies install करें
```bash
pip install -r requirements.txt
```

### 4. Config setup करें

`config.py` file में अपना **Bot Token** add करें:
```python
BOT_TOKEN = "आपका_token_यहाँ"
```

### 5. Bot चलाएं
```bash
python main.py
```

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Bot को शुरू करता है |
| `/play <song>` | गाना search करके play करता है |
| `/pause` | Music को pause करता है |
| `/resume` | Music को फिर से शुरू करता है |
| `/stop` | Music को stop करता है |
| `/queue` | Queue में songs देखता है |
| `/skip` | अगला गाना play करता है |
| `/help` | सभी commands देखता है |

## Usage Example

```
/play Bollywood songs
/play Let it be Beatles
/pause
/resume
/skip
/stop
```

## Project Structure

```
music-vc-bot/
├── main.py              # Main bot file
├── config.py            # Configuration
├── handlers.py          # Command handlers
├── music_player.py      # Music playing logic
├── youtube_utils.py     # YouTube search & download
├── requirements.txt     # Dependencies
└── README.md            # This file
```

## Support

अगर कोई समस्या आए तो issues create करें या मुझसे contact करें!

## License

MIT License

---

**Made with ❤️ by namandeep0045-bit**
