import os

ROOT_DIR = '../examples/MMPT/data/youtube-jomi-dataset/'

TRAIN_PROPORTION = 0.75

train_list = open(os.path.join(ROOT_DIR, 'how2_s3d_train.lst'), 'w')
valid_list = open(os.path.join(ROOT_DIR, 'how2_s3d_val.lst'), 'w')

video_files = os.listdir(os.path.join(ROOT_DIR, 'videos'))

video_filenames = [filename.split('.')[0] for filename in video_files]

num_train = int(len(video_filenames) * TRAIN_PROPORTION)
print("{} files in train list".format(str(num_train)))

for i in range(len(video_filenames)):
    if i < num_train:
        train_list.write(video_filenames[i] + '\n')
    else:
        valid_list.write(video_filenames[i] + '\n')

train_list.close()
valid_list.close()

print("Finished creating train and valid splits")
