import json
import os

labels_path = '../examples/MMPT/data/open-surgery-yt/surgery_action_labels.json'
filtered_labels_path = '../examples/MMPT/data/open-surgery-yt/surgery_action_labels_filtered.json'
labels_f = open(labels_path, 'r')
filtered_labels_f = open(filtered_labels_path, 'w')

action_labels_list = ['cutting', 'suturing', 'tying']

data = json.load(labels_f)
filtered_dict = {}

for key, item in data.items():
    filtered_list = []
    for it in item:
        if it['label'] in action_labels_list:
            filtered_list.append(it)
    if len(filtered_list) > 0:
        filtered_dict[key] = filtered_list

json.dump(filtered_dict, filtered_labels_f)
labels_f.close()
filtered_labels_f.close()
print("Finished filtering labels file")
