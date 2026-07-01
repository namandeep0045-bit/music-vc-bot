#!/usr/bin/env python3
"""
Music Player Logic
"""

import logging
from collections import deque
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class MusicPlayer:
    """Manages music playback and queue."""
    
    def __init__(self):
        self.queue: deque = deque()
        self.is_playing = False
        self.is_paused = False
        self.current_song: Optional[Tuple[str, str]] = None
    
    def add_to_queue(self, url: str, title: str, requester: str) -> None:
        """Add a song to the queue."""
        self.queue.append((title, requester))
        logger.info(f"Added to queue: {title}")
        
        if not self.is_playing:
            self.is_playing = True
            self.current_song = (title, requester)
    
    def skip(self) -> Optional[Tuple[str, str]]:
        """Skip to the next song in the queue."""
        if self.queue:
            self.queue.popleft()
            if self.queue:
                self.current_song = self.queue[0]
                logger.info(f"Skipped to: {self.current_song[0]}")
                return self.current_song
            else:
                self.is_playing = False
                self.current_song = None
        return None
    
    def stop(self) -> None:
        """Stop playing and clear the queue."""
        self.queue.clear()
        self.is_playing = False
        self.is_paused = False
        self.current_song = None
        logger.info("Music stopped and queue cleared")
    
    def get_queue_info(self) -> dict:
        """Get information about the current queue."""
        return {
            "queue_size": len(self.queue),
            "is_playing": self.is_playing,
            "is_paused": self.is_paused,
            "current_song": self.current_song
        }


# Global player instance
player = MusicPlayer()
