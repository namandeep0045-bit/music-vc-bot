# 🎵 Music VC Bot - Setup Guide

## Hindi में Setup

### Step 1️⃣ : Requirements Install करें

**Windows/Mac/Linux के लिए:**

```bash
# 1. Repository clone करें
git clone https://github.com/namandeep0045-bit/music-vc-bot.git
cd music-vc-bot

# 2. Virtual Environment बनाएं (optional but recommended)
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 3. Dependencies install करें
pip install -r requirements.txt
```

### Step 2️⃣ : FFmpeg Install करें

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
- Download: https://ffmpeg.org/download.html
- या PowerShell में:
```powershell
choco install ffmpeg
```

**FFmpeg को verify करें:**
```bash
ffmpeg -version
```

### Step 3️⃣ : Bot Token Setup करें

`config.py` में अपना **Bot Token** डालें:

```python
# config.py में यह line को update करें:
BOT_TOKEN = "8736223294:AAHJKOu_g4dpnnTq_O4LKrsO1r6TZ04VPhI"
```

### Step 4️⃣ : Bot को Run करें

```bash
python main.py
```

✅ अगर सब कुछ ठीक है तो यह message दिखेगा:
```
🤖 Music VC Bot शुरू हो रहा है...
Description: YouTube से Voice Chat में music play करता है!
```

### Step 5️⃣ : Telegram में Bot को Test करें

Telegram खोलें और:
1. अपने Bot को search करें (उदाहरण: @your_bot_name)
2. `/start` भेजें
3. `/play Bollywood songs` भेजकर test करें

---

## ❌ अगर Error आए तो:

### Error: "FFmpeg not found"
```bash
# FFmpeg install करें (ऊपर देखें)
# या
pip install ffmpeg-python
```

### Error: "No module named 'telegram'"
```bash
pip install -r requirements.txt
```

### Error: "Token invalid"
- @BotFather से नया token लें
- config.py में सही token डालें

### Error: "yt-dlp not found"
```bash
pip install yt-dlp
```

---

## 📝 Troubleshooting

**Bot respond नहीं कर रहा?**
- Check करें कि Telegram Internet connection है
- Proxy के पीछे हैं तो VPN try करें
- `/start` फिर से भेजें

**Music play नहीं हो रहा?**
- FFmpeg properly installed है?
- YouTube accessible है?
- Song का नाम सही है?

**Downloads folder error?**
```bash
mkdir downloads
```

---

## 🎯 Next Steps

1. Bot को improve करें (new features add करें)
2. Voice chat में streaming setup करें
3. Database support add करें
4. Web interface बनाएं

---

**Happy Coding! 🚀**
