import json
import os

NUM_LABELS = 100

ROOT_DIR = '../examples/MMPT/data/open-surgery-yt'
ORIG_LABELS_FILE = 'surgery_action_labels_filtered.json'
NEW_LABELS_FILE = 'surgery_action_labels_ft_{}.json'.format(str(NUM_LABELS))
VIDEOS_DIR = 'surgery-videos-temp'

orig_labels_f = open(os.path.join(ROOT_DIR, ORIG_LABELS_FILE), 'r')
new_labels_f = open(os.path.join(ROOT_DIR, NEW_LABELS_FILE), 'w')

orig_labels_dict = json.load(orig_labels_f)
new_labels_dict = {}

video_files = os.listdir(os.path.join(ROOT_DIR, VIDEOS_DIR))
video_names = [names.split('.')[0] for names in video_files]

num_added = 0
for key, values in orig_labels_dict.items():
    if key in video_names:
        new_labels_dict[key] = values
        num_added += 1
        if num_added >= NUM_LABELS:
            print("Finished collecting all labels!")
            break

json.dump(new_labels_dict, new_labels_f)

orig_labels_f.close()
new_labels_f.close()
print("All done!")
