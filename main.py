import os
import yt_dlp

def download_playlist(playlist_url, output_folder="outputV"):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define options for yt-dlp
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(playlist_index)s - %(title)s.%(ext)s',  # Save in outputV folder
        'format': 'best',  # Choose the best format with combined audio and video
        'noplaylist': False,  # Download entire playlist
        'quiet': False,  # Display progress
        '--abort-on-error': True,  # Stop on errors
    }

    # Use yt-dlp to download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Replace with your playlist URL
playlist_url = 'https://www.youtube.com/watch?v=MnRrTmGvN_c'

# Call the function to download the playlist
download_playlist(playlist_url)
