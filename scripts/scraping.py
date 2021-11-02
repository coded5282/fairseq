import os
from youtube_dl import YoutubeDL
import csv

NUM_TRAIN = 100
NUM_VALID = 50

if not os.path.exists('../examples/MMPT/data/how2/longer'):
    print("Creating directory for longer data")
    os.makedirs('../examples/MMPT/data/how2/longer')

if not os.path.exists('../examples/MMPT/data/videos_longer'):
    print("Creating directory for longer videos")
    os.makedirs('../examples/MMPT/data/videos_longer')

train_list = open('../examples/MMPT/data/how2/longer/how2_s3d_train.lst', 'w')
valid_list = open('../examples/MMPT/data/how2/longer/how2_s3d_val.lst', 'w')

videos = []

with open('../examples/MMPT/data/data/HowTo100M_v1.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    for row_idx, row in enumerate(filereader):
        if row_idx != 0:
            videos.append(str(row[0])) # appending video id
print("All videos appended to list")

def download_video(video_id):
    youtube_dl_opts = {'outtmpl': '../examples/MMPT/data/videos_longer/' + str(video_id) + '.mp4'}
    video_name = 'https://www.youtube.com/watch?v=' + str(video_id)

    with YoutubeDL(youtube_dl_opts) as ydl:
        ydl.download([video_name])

def download_video_if_not_present(video_id):
    curr_videos_dir = '../examples/MMPT/data/videos'
    curr_video_files = os.listdir(curr_videos_dir)
    curr_video_ids = [video_names.split('.')[0] for video_names in curr_video_files]
    if video_id not in curr_video_ids:
        print("{} is not in current list of videos, so downloading it!".format(str(video_id)))
        download_video(video_id)

#for i in range(NUM_VIDEOS_TO_DOWNLOAD):
#    download_video(videos[i])

downloaded_video_ct = 0
for i in range(len(videos)):
    try:
        download_video(videos[i])
        downloaded_video_ct += 1
        if downloaded_video_ct <= NUM_TRAIN:
            train_list.write(str(videos[i]) + '\n')
        else:
            valid_list.write(str(videos[i]) + '\n')
        if downloaded_video_ct >= (NUM_TRAIN+NUM_VALID):
            print("Have downloaded " + str(NUM_TRAIN+NUM_VALID) + " videos")
            break
        print("Have downloaded " + str(downloaded_video_ct) + " videos so far!")
    except Exception as e:
        print(e)
        print("Could not download video ID: " + str(videos[i]))

print("All videos now downloaded")

train_list.close()
valid_list.close()
print("Successfully wrote train and valid list files")
