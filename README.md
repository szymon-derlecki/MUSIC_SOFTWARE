# Spotify -> MP3 Downloader

A simple interactive Python script allowing you to download tracks, playlists, or albums from Spotify as MP3 files. 

This script acts as a user-friendly wrapper around [spotDL](https://github.com/spotDL/spotify-downloader), automatically configuring the output format to MP3 and fetching audio from YouTube Music.

## Prerequisites

Before running the script, ensure you have the following installed on your system:
1. **Python 3.x**
2. **FFmpeg** (Required by 'spotd' to convert audio files to MP3)
   - **Windows:** Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) or install via winget: 'winget install ffmpeg'
   - **macOS:** Install via Homebrew: `brew install ffmpeg`
   - **Linux:** Install via your package manager, e.g., 'sudo apt install ffmpeg'

## Installation

1. Clone or download this repository to your local machine.
2. Install the required 'spotdl' Python package by running:

'''bash
pip install spotdl
'''

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python (considering that you named your file 'main.py'):

'''bash
python main.py
'''

4. Follow the interactive prompts:
   - Type 'track', `playlist`, or 'album' depending on what you want to download.
   - Paste the Spotify URL relevant for the particular single/playlist/album.

### Output
The script will automatically create a new folder based on the title of the track/album/playlist and save the MP3 files inside using the format:
'[Title] / [Artist] - [Title].mp3'

## Disclaimer
This tool is intended for personal, educational, and fair-use purposes only. Please respect the copyright of the artists and the terms of service of the platforms involved.
