from youtube_dl import YoutubeDL
import json
import os

VIDEO_DIR = '../examples/MMPT/data/coin/videos'
COIN_JSON_FILE = '../examples/MMPT/data/coin/COIN_short.json'
coin_file = open(COIN_JSON_FILE, 'r')

if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)
    print("Created video directory")

def download_video(video_id):
    youtube_dl_opts = {'outtmpl': os.path.join(VIDEO_DIR, str(video_id) + '.mp4'),
                        'format': '137'}
    video_name = 'https://www.youtube.com/watch?v=' + str(video_id)

    with YoutubeDL(youtube_dl_opts) as ydl:
        ydl.download([video_name])

coin_data = json.load(coin_file)

for video_id in coin_data['database'].keys():
    print("VIDEO ID: {}".format(str(video_id)))
    try:
        download_video(video_id)
    except Exception as e:
        print(e)
        print("Could not download video with id: {}".format(str(video_id)))
