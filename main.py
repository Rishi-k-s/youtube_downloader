from pytube import YouTube
import math
import os
vid_save_dir = "videos"
audio_save_dir = "audio"

file_handlr = open("video_links.txt","r",newline="\n")
urlListFile = file_handlr.readlines()

# HAVE TO DO A LOT OF WORK
def download_vid_high_quality(video_url_list):
    for eachUrlFromList in video_url_list:
        video = YouTube(eachUrlFromList)
        # video = video.streams.get_highest_resolution()
        video = video.streams.get_by_resolution(resolution="720p")
        video_name = video.default_filename
        video_size = video.filesize
        video_res = video.resolution
        print("Video Details")
        print("-------------")
        print("Name: {}\nSize:{} Current Res: {}".format(
            video_name,video_size, video_res))

        try:
            video.download(vid_save_dir)
            print("Downloading")
        except:
            print("Failed to download video")

        print("video was downloaded successfully")

# def download_vid_low_quality(video_url_list):
#     for eachUrlFromList in video_url_list:
#         video = YouTube(eachUrlFromList)
#         video = video.streams.get_highest_resolution()
#         video_resolution = video.resolution
#         video_name = video.default_filename
#         video_size = math.floor(video.filesize)/10**6
#         print("Video Details")
#         print("-------------")
#         print("Name: {}\nSize:{} Mb\nResolution:{}".format(
#             video_name,video_size,video_resolution
#         ))

#         try:
#             video.download(vid_save_dir)
#         except:
#             print("Failed to download video")

#         print("video was downloaded successfully")

# def download_audio(audio_url_list):
#     for eachUrlFromList in audio_url_list:
#         video = YouTube(eachUrlFromList)
#         audio = video.streams.filter(only_audio = True).first()
#         # audio_bitrate = audio.bitrate
#         # audio_name = audio.default_filename
#         # audio_size =  (math.floor(audio.filesize)/8000)

#         # print("Audio Details")
#         # print("-------------")
#         # print("(Dont mind the .mp4 extension)")
#         # print("Name: {}\nSize:{} Mb\nBitrate:{}".format(
#         #     audio_name,audio_size,audio_bitrate
#         # ))

#         try:
#             out_file = video.download(output_path=audio_save_dir)
#             base, ext = os.path.splitext(out_file)
#             new_file = base + '.mp3'
#             os.rename(out_file, new_file)
#         except:
#             print("Failed to download audio")

#         print("audio was downloaded successfully")

# def test_dwnld_audio (audio_link_list):
#     for each_audio_link in audio_link_list:
#         yt = YouTube("https://www.youtube.com/watch?v=eiGdsH1g20k")
#     video = yt.streams.filter(only_audio=True).first()
#     destination = 'audio'
#     out_file = video.download(destination)
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp3'
#     os.rename(out_file, new_file)
#     print(yt.title + " has been successfully downloaded.")


while True:
    print("[1] Download video")
    # print("[2] Download Audio")
    get_type = int(input("--> "))
    is_video = True

    if (get_type == 1):
        print("[1] Highest Quality")
        # print("[2] Lowest Quality")
        get_res = int(input("--> ")) 
        if(get_res == 1):
            download_vid_high_quality(urlListFile)
        # elif(get_res == 2):
        #     download_vid_low_quality(urlListFile)

    # elif(get_type == 2):
    #     download_audio(urlListFile)