from pytube import YouTube
import os

# Path to the text file containing video links
LINKS_FILE = "video_links.txt"

# Directory to save the downloaded audio files
DOWNLOAD_DIR = "downloads"

def download_audio(video_url, download_dir):
    try:
        yt = YouTube(video_url)
        # Extract audio stream with the highest bitrate
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            print(f"Audio stream not available for: {video_url}")
            return
        
        print(f"Downloading: {yt.title}")
        # Download the audio file
        out_file = audio_stream.download(output_path=download_dir)
        
        # Rename the file to MP3
        base, _ = os.path.splitext(out_file)
        mp3_file = f"{base}.mp3"
        os.rename(out_file, mp3_file)
        print(f"Downloaded and converted to MP3: {mp3_file}")
    except Exception as e:
        print(f"Failed to download {video_url}: {e}")

def main():
    if not os.path.exists(LINKS_FILE):
        print(f"{LINKS_FILE} not found. Please create the file with YouTube video links.")
        return
    
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    
    with open(LINKS_FILE, "r") as file:
        links = [line.strip() for line in file if line.strip()]
    
    if not links:
        print("No links found in the file. Please add YouTube video links.")
        return
    
    for link in links:
        download_audio(link, DOWNLOAD_DIR)

if __name__ == "__main__":
    main()
