import json
import os

COIN_JSON_FILE = '../examples/MMPT/data/coin/COIN_match.json'
COIN_JSON_FILE_NEW = '../examples/MMPT/data/coin/COIN_match_new.json'

f_old = open(COIN_JSON_FILE, 'r')
f_new = open(COIN_JSON_FILE_NEW, 'w')

data_old = json.load(f_old)
data_new_dict = {}
label_dict = {}
label_id = 1

for key, value in data_old['database'].items():
    for annotations in value['annotation']:
        curr_label = annotations['label']
        if curr_label not in label_dict:
            label_dict[curr_label] = label_id
            label_id += 1
        updated_id = label_dict[curr_label]
        annotations['id'] = updated_id
    data_new_dict[key] = value

overall_dict_new = {}
overall_dict_new['database'] = data_new_dict
json.dump(overall_dict_new, f_new)
print("Finished updating id of json file")

f_old.close()
f_new.close()

