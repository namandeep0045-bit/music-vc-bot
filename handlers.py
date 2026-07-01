#!/usr/bin/env python3
"""
Command Handlers for Music VC Bot
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from music_player import player
from youtube_utils import search_youtube

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command - sends welcome message."""
    user = update.effective_user
    welcome_text = f"""
🎵 **Music VC Bot में स्वागत है!** 🎵

नमस्ते {user.mention_html()}! 👋

मैं एक Voice Chat Music Bot हूँ जो YouTube से गाने play कर सकता हूँ।

**मुझे ये commands use करें:**

🎶 /play <गाना> - गाना ढूंढकर play करता है
⏸️ /pause - संगीत को pause करता है
▶️ /resume - संगीत को फिर से शुरू करता है
⏹️ /stop - संगीत को बंद करता है
⏭️ /skip - अगला गाना play करता है
📋 /queue - Queue में songs देखता है
❓ /help - सभी commands देखता है

**शुरू करने के लिए:** `/play आपका_पसंदीदा_गाना`

🚀 Happy Music!
    """
    await update.message.reply_html(welcome_text)
    logger.info(f"Start command from {user.username}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help command - shows all available commands."""
    help_text = """
📚 **सभी Commands:**

🎵 **Music Controls:**
/play <गाना> - YouTube से गाना search करके play करता है
/pause - संगीत को pause करता है (रोक देता है)
/resume - Paused संगीत को फिर से शुरू करता है
/stop - संगीत को पूरी तरह बंद करता है
/skip - अगला गाना play करता है

📋 **Queue Management:**
/queue - अभी queue में कौन-कौन से गाने हैं

💡 **अन्य:**
/start - Bot को फिर से शुरू करता है
/help - यह message दोबारा दिखाता है

**उदाहरण:**
```
/play Bollywood songs
/play Let it be Beatles
/play Punjabi music
```

💬 अगर कोई समस्या आए तो मुझसे पूछें!
    """
    await update.message.reply_markdown(help_text)


async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Play command - searches and plays music."""
    user = update.effective_user
    
    if not context.args:
        await update.message.reply_text(
            "❌ कृपया गाना का नाम दें!\n\n"
            "उदाहरण: /play Bollywood songs"
        )
        return
    
    song_name = " ".join(context.args)
    await update.message.reply_text(f"🔍 '{song_name}' को YouTube पर ढूंढ रहे हैं...")
    
    try:
        results = search_youtube(song_name)
        
        if not results:
            await update.message.reply_text("❌ कोई गाना नहीं मिला। दूसरा नाम आजमाइए।")
            return
        
        # Get the first result
        video_url = results[0]["url"]
        video_title = results[0]["title"]
        
        await update.message.reply_text(
            f"🎵 अब play हो रहा है:\n\n"
            f"<b>{video_title}</b>\n\n"
            f"🎶 Enjoy!",
            parse_mode="HTML"
        )
        
        # Add to queue
        player.add_to_queue(video_url, video_title, user.username)
        
        logger.info(f"Playing: {video_title} (requested by {user.username})")
        
    except Exception as e:
        logger.error(f"Error in play command: {e}")
        await update.message.reply_text(
            f"❌ कोई error आया:\n{str(e)}\n\n"
            "दूसरा गाना आजमाइए।"
        )


async def pause_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Pause command - pauses the current music."""
    if player.is_playing:
        player.is_paused = True
        await update.message.reply_text("⏸️ संगीत pause कर दिया गया।")
        logger.info("Music paused")
    else:
        await update.message.reply_text("❌ कोई गाना play नहीं हो रहा।")


async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Resume command - resumes paused music."""
    if player.is_paused:
        player.is_paused = False
        await update.message.reply_text("▶️ संगीत फिर से शुरू हो गया।")
        logger.info("Music resumed")
    else:
        await update.message.reply_text("❌ कोई paused गाना नहीं है।")


async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Stop command - stops the music."""
    if player.is_playing or player.queue:
        player.stop()
        await update.message.reply_text("⏹️ संगीत बंद कर दिया गया।")
        logger.info("Music stopped")
    else:
        await update.message.reply_text("❌ कोई गाना play नहीं हो रहा।")


async def queue_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Queue command - shows the music queue."""
    if not player.queue:
        await update.message.reply_text("📋 Queue खाली है। /play करके गाना शामिल करें।")
        return
    
    queue_text = "📋 **Queue में गाने:**\n\n"
    
    for i, (title, requester) in enumerate(player.queue, 1):
        queue_text += f"{i}. <b>{title}</b>\n   (requested by {requester})\n\n"
    
    queue_text += f"\n📊 कुल: {len(player.queue)} गाने"
    
    await update.message.reply_html(queue_text)
    logger.info("Queue displayed")


async def skip_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Skip command - skips to the next song."""
    if player.queue:
        player.skip()
        await update.message.reply_text("⏭️ अगला गाना play हो रहा है...")
        logger.info("Song skipped")
    else:
        await update.message.reply_text("❌ Queue में कोई अगला गाना नहीं है।")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "❌ कोई error आया! कृपया दोबारा कोशिश करें।"
        )
