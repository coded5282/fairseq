from youtube_dl import YoutubeDL
import json
import os

SURGERY_VIDEO_DIR = '../examples/MMPT/data/open-surgery-yt/surgery-videos'
SURGERY_JSON_NEW = '../examples/MMPT/data/open-surgery-yt/surgery_action_labels_filtered.json'

surgery_json_f = open(SURGERY_JSON_NEW, 'r')

if not os.path.exists(SURGERY_VIDEO_DIR):
    os.makedirs(SURGERY_VIDEO_DIR)
    print("Creating open surgery video directory")

surgery_video_files = os.listdir(SURGERY_VIDEO_DIR)
surgery_filenames = [filename.split('.')[0] for filename in surgery_video_files]

def download_video(video_id):
    youtube_dl_opts = {'outtmpl': os.path.join(SURGERY_VIDEO_DIR, str(video_id) + '.mp4'),
                        'cookiefile': '../examples/MMPT/data/open-surgery-yt/youtube.com_cookies.txt'}
    video_name = 'https://www.youtube.com/watch?v=' + str(video_id)

    with YoutubeDL(youtube_dl_opts) as ydl:
        ydl.download([video_name])

open_surgery_action_data = json.load(surgery_json_f)

for idx, link in enumerate(open_surgery_action_data.keys()):
    print("Currently downloading video id: {}".format(str(link)))
    print("Currently downloading video idx: {}".format(str(idx)))
    try:
        if link in surgery_filenames:
            print("Skipping this video since already exists!")
            continue
        else:
            download_video(link)
    except Exception as e:
        print(e)
        print("Could not download video with ID: " + str(link))
