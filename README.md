# YouTube Audio and Video Downloader 
# Documentation

## Table of Contents
1. Introduction
2. Requirements
3. Installation
4. Usage
5. Adding Video Links
6. Command Line Instructions
7. License
8. Contributions
9. Support
10. Disclaimer

## 1. Introduction

Welcome to the YouTube Audio and Video Downloader! This Python script allows you to download audio and video files from YouTube using their video URLs. To get started, you need to install the `pytube` library and follow the command line instructions provided below.

## 2. Requirements

To use this YouTube Audio and Video Downloader, you'll need the following prerequisites:

- Python 3 installed on your system.
- The `pytube` library installed.

## 3. Installation

1. First, make sure you have Python installed. You can download Python from the official website: https://www.python.org/downloads/

2. Next, install the required `pytube` library using pip:

```bash
pip install pytube
```

3. clone the script from the GitHub repository or simply copy the `main.py` file to your local machine.
```bash
git clone https://github.com/Rishi-k-s/youtube_downloader.git
```
## 4. Usage

To use the YouTube Audio and Video Downloader, follow these steps:

1. Create a file named `video_links.txt` in the same folder as `main.py`.(if you are cloning this repo the folder file already exists)
2. Add the YouTube video URLs you want to download in separate lines within the `video_links.txt` file.

## 5. Adding Video Links

Add the video links you want to download to the `video_links.txt` file in the following format:

```plaintext
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=hvL1339luv0
https://www.youtube.com/watch?v=NZzXzymUgEg
```

Replace this links which already exist with the actual YouTube video IDs you want to download.

## 6. Command Line Instructions

Open a terminal or command prompt, navigate to the folder containing `main.py`, and run the following command:

```bash
python main.py
```

The script will read the video links from the `video_links.txt` file and download the audio and video files for each URL in the same folder as `main.py`.

## 7. License

This YouTube Audio and Video Downloader is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 8. Contributions

Contributions to this project are always welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## 9. Support

For any questions or support related to this script, you can reach out to the project maintainers through the GitHub repository's issue tracker.

## 10. Disclaimer

This script is intended for personal use only. Please ensure you have the necessary permissions to download and use content from YouTube. Respect copyright laws and the terms of service of YouTube while using this script.

**Note:** This script might break if YouTube's website structure or API changes. The maintainers will try their best to keep the script up-to-date, but there is no guarantee of uninterrupted functionality.

# Made with ❤️ by Rishi
