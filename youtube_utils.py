#!/usr/bin/env python3
"""
YouTube Search and Download Utilities
"""

import logging
import yt_dlp
from typing import List, Dict

logger = logging.getLogger(__name__)


def search_youtube(query: str, max_results: int = 5) -> List[Dict]:
    """
    Search YouTube for videos.
    
    Args:
        query: Search query
        max_results: Maximum number of results to return
    
    Returns:
        List of search results with title and URL
    """
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'default_search': 'ytsearch',
            'extract_flat': 'in_playlist',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Search for videos
            info = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
            
            results = []
            if 'entries' in info:
                for video in info['entries']:
                    if video:
                        results.append({
                            'title': video.get('title', 'Unknown'),
                            'url': video.get('url', ''),
                            'duration': video.get('duration', 0),
                            'channel': video.get('uploader', 'Unknown')
                        })
            
            logger.info(f"Search results for '{query}': {len(results)} found")
            return results
    
    except Exception as e:
        logger.error(f"Error searching YouTube: {e}")
        return []


def get_video_info(url: str) -> Dict:
    """
    Get information about a YouTube video.
    
    Args:
        url: YouTube video URL
    
    Returns:
        Dictionary with video information
    """
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration', 0),
                'channel': info.get('uploader', 'Unknown'),
                'url': url
            }
    
    except Exception as e:
        logger.error(f"Error getting video info: {e}")
        return {}


def download_audio(url: str, output_path: str = "downloads") -> str:
    """
    Download audio from YouTube video.
    
    Args:
        url: YouTube video URL
        output_path: Path to save the audio file
    
    Returns:
        Path to the downloaded audio file
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info)
            logger.info(f"Downloaded: {audio_file}")
            return audio_file
    
    except Exception as e:
        logger.error(f"Error downloading audio: {e}")
        return ""
