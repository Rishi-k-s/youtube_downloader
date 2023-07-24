# importing packages
from pytube import YouTube
import os
  

yt = YouTube("https://www.youtube.com/watch?v=eiGdsH1g20k")
video = yt.streams.filter(only_audio=True).first()
destination = 'audio'
out_file = video.download(destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")