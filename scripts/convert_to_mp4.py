import ffmpeg
import os

ROOT_DIR = '../examples/MMPT/data/open-surgery-yt/surgery-videos-temp/'

def convert_to_mp4(src_file):
    filename = src_file.split('.')[0]
    target_name = filename + '.mp4'
    print("Target name: {}".format(target_name))
    ffmpeg.input(os.path.join(ROOT_DIR, src_file)).output(os.path.join(ROOT_DIR, target_name)).run()
    print("Finished converting {}".format(src_file))

all_files = os.listdir(ROOT_DIR)
for each_file in all_files:
    each_file_split = each_file.split('.')
    if (len(each_file_split) >= 3) or (len(each_file_split) >= 2 and 'mp4' not in each_file_split):
        print("Incorrect file type for: {}".format(each_file))
        file_name = each_file_split[0]
        convert_to_mp4(each_file)
        os.remove(os.path.join(ROOT_DIR, each_file))
        print("Removed file: {}".format(each_file))

print("All done converting!")

#convert_to_mp4(FILE_NAME)
