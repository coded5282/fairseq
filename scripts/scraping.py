import os
from youtube_dl import YoutubeDL

videos = []

def download_video(video_id):
    youtube_dl_opts = {'outtmpl': '../examples/MMPT/data/videos/' + str(video_id) + '.mp4'}
    video_name = 'https://www.youtube.com/watch?v=' + str(video_id)

    with YoutubeDL(youtube_dl_opts) as ydl:
        ydl.download([video_name])

for video in videos:
    download_video(video)
