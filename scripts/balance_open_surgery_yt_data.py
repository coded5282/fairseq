import os
import json

ROOT_DIR = os.path.join(os.environ["PROJECT"], 'Fall-2021-Rotation/fairseq/examples/MMPT/data/open-surgery-yt')
LABELS_JSON = 'surgery_action_labels_filtered_for_ft.json'
BALANCED_LABELS_JSON = 'balanced_surgery_action_labels_filtered_for_ft.json'

labels_json_f = open(os.path.join(ROOT_DIR, LABELS_JSON), 'r')
balanced_labels_json_f = open(os.path.join(ROOT_DIR, BALANCED_LABELS_JSON), 'w')

labels_data = json.load(labels_json_f)
time_length_dict = {}

# get length of time for each class label
for video_id in labels_data.keys():
    video_data_list = labels_data[video_id]
    for video_data in video_data_list:
        time_length = float(video_data['end']) - float(video_data['start'])
        curr_label = video_data['label']
        if curr_label not in time_length_dict:
            time_length_dict[curr_label] = time_length
        else:
            time_length_dict[curr_label] = time_length_dict[curr_label] + time_length

# use label with minimum amount of time
min_class_label = None
min_time_length = float('inf')
for class_label in time_length_dict:
    class_time_length = time_length_dict[class_label]
    if class_time_length < min_time_length:
        min_time_length = class_time_length
        min_class_label = class_label

assert min_class_label != None, "min_class_label is still None!"

# keep looping until other labels are about the same
# build flat list of class and time values
balanced_labels_dict = {}
flat_values_list = []
curr_label_time_lengths = {}

FLAT_TUPLE_KEYS = {'VIDEO_ID': 0,
                    'LABEL': 1,
                    'START': 2,
                    'END': 3}

for video_id in labels_data.keys():
    video_data_list = labels_data[video_id]
    for video_data in video_data_list:
        curr_label = video_data['label']
        curr_video = video_id
        flat_values_list.append((curr_video, curr_label, float(video_data['start']), float(video_data['end'])))

already_used_list = []
for flat_value in flat_values_list:
    curr_label = flat_value[FLAT_TUPLE_KEYS['LABEL']]
    if curr_label not in curr_label_time_lengths or curr_label_time_lengths[curr_label] < min_time_length:
        video_dict_val = {'start': flat_value[FLAT_TUPLE_KEYS['START']], 'end': flat_value[FLAT_TUPLE_KEYS['END']], 'label': flat_value[FLAT_TUPLE_KEYS['LABEL']]}
        if flat_value[FLAT_TUPLE_KEYS['VIDEO_ID']] in balanced_labels_dict:
            balanced_labels_dict[flat_value[FLAT_TUPLE_KEYS['VIDEO_ID']]].append(video_dict_val)
        else:
            balanced_labels_dict[flat_value[FLAT_TUPLE_KEYS['VIDEO_ID']]] = [video_dict_val]
        if flat_value[FLAT_TUPLE_KEYS['LABEL']] in curr_label_time_lengths:
            curr_label_time_lengths[flat_value[FLAT_TUPLE_KEYS['LABEL']]] += (flat_value[FLAT_TUPLE_KEYS['END']]-flat_value[FLAT_TUPLE_KEYS['START']])
        else:
            curr_label_time_lengths[flat_value[FLAT_TUPLE_KEYS['LABEL']]] = (flat_value[FLAT_TUPLE_KEYS['END']]-flat_value[FLAT_TUPLE_KEYS['START']])
        already_used_list.append(flat_value)

json.dump(balanced_labels_dict, balanced_labels_json_f)

labels_json_f.close()
balanced_labels_json_f.close()
