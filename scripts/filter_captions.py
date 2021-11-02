import os
import json

ORIGINAL_JSON_PATH = 'examples/MMPT/data/how2/raw_caption.json'
UPDATED_JSON_PATH = 'examples/MMPT/data/how2/raw_caption_updated.json'
VIDEOS_DIR_PATH = 'examples/MMPT/data/videos'

json_file = open(ORIGINAL_JSON_PATH, 'r')

original_raw_captions_dict = json.load(json_file)
updated_captions_dict = {}

video_files = os.listdir(VIDEOS_DIR_PATH)
video_names = [video_name.split('.')[0] for video_name in video_files]

for orig_raw_caption in original_raw_captions_dict:
    if orig_raw_caption in video_names:
        updated_captions_dict[orig_raw_caption] = original_raw_captions_dict[orig_raw_caption]

captions_json = json.dumps(updated_captions_dict)
updated_captions_file = open(UPDATED_JSON_PATH, 'w')
updated_captions_file.write(captions_json)
updated_captions_file.close()
print("Updated captions file")
