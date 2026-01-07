
"""
@file LinkToMP3.py
@author Gandla Bhargavi
@brief Convert a video link to MP3 audio using yt-dlp.

@date 2025-12-10
"""

import yt_dlp

def convert_to_mp3(video_url):
 options = {
     'format': 'bestaudio/best',
     'outtmpl': '%(title)s.%(ext)s',
     'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
     }],
 }

 with yt_dlp.YoutubeDL(options) as ydl:
     ydl.download([video_url])

def main():
 link = input("Enter video link: ")
 convert_to_mp3(link)
 print("MP3 download completed successfully.")

if __name__ == "__main__":
 main()