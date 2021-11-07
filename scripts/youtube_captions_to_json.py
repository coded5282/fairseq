import json
import os

CAPTIONS_DIR = '../examples/MMPT/data/youtube-jomi-dataset/captions'
NEW_CAPTION_FILE = '../examples/MMPT/data/youtube-jomi-dataset/raw_caption_jomi.json'

captions_files = os.listdir(CAPTIONS_DIR)

raw_captions_dict = {}

for caption_file in captions_files:
    caption_id = str(caption_file.split('.')[0])
    print("Working on file: {}".format(str(caption_id)))
    start, end, text = [], [], []
    caption_dict = {}
    f = open(os.path.join(CAPTIONS_DIR, caption_file), 'r')
    prev_str = ''
    for line in f:
        fields = line.split('\t')
        cleaned_fields = [field.strip() for field in fields]
        if len(cleaned_fields) == 1:
            prev_str = cleaned_fields[0] + ' '
            continue
        text.append(str(prev_str) + str(cleaned_fields[0]))
        start.append(round(float(cleaned_fields[1]),2))
        end.append(round(float(cleaned_fields[1])+float(cleaned_fields[2]),2))
        prev_str = ''
    caption_dict['start'] = start
    caption_dict['end'] = end
    caption_dict['text'] = text
    raw_captions_dict[caption_id] = caption_dict

with open(NEW_CAPTION_FILE, 'w') as json_file:
    json.dump(raw_captions_dict, json_file)

print("Finished creating updated raw captions JSON file")
