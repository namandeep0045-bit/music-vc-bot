#!/usr/bin/env python3
"""
Telegram Music VC Bot - Main Entry Point
"""

import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, BOT_NAME, BOT_DESCRIPTION, LOG_LEVEL
from handlers import (
    start_command,
    help_command,
    play_command,
    pause_command,
    resume_command,
    stop_command,
    queue_command,
    skip_command,
    error_handler
)

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL)
)
logger = logging.getLogger(__name__)


async def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("play", play_command))
    application.add_handler(CommandHandler("pause", pause_command))
    application.add_handler(CommandHandler("resume", resume_command))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("queue", queue_command))
    application.add_handler(CommandHandler("skip", skip_command))

    # Add error handler
    application.add_error_handler(error_handler)

    # Run the bot
    logger.info(f"🤖 {BOT_NAME} शुरू हो रहा है...")
    logger.info(f"Description: {BOT_DESCRIPTION}")
    
    await application.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
