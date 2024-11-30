import os
import subprocess
import sys

def convert_mp4_to_mp3(input_folder='outputV', output_folder='outputA'):
    """Convert all MP4 files in input_folder to MP3 files in output_folder."""
    # Validate input and output folders
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder {input_folder} does not exist.")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Find FFmpeg executable
    ffmpeg_path = None
    for path in os.environ["PATH"].split(os.pathsep):
        possible_path = os.path.join(path, "ffmpeg.exe")
        if os.path.exists(possible_path):
            ffmpeg_path = possible_path
            break
    
    if not ffmpeg_path:
        print("Error: FFmpeg not found. Please install FFmpeg and add it to PATH.")
        return

    # Convert MP4 files
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp4') and filename == "NA - Original Happy Birthday Song ♫♫♫ Birthday Song For Kids with Dora the Explorer.mp4":
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.mp3'
            output_path = os.path.join(output_folder, output_filename)
            
            try:
                # Use subprocess to call FFmpeg directly
                subprocess.run([
                    ffmpeg_path, 
                    '-i', input_path, 
                    output_path
                ], check=True)
                print(f"Converted {filename} to {output_filename}")
            
            except subprocess.CalledProcessError as e:
                print(f"Error converting {filename}: {e}")

if __name__ == '__main__':
    convert_mp4_to_mp3()