import json
import os

ROOT_DIR = '../examples/MMPT/data/open-surgery-yt'
ORIG_LABELS_FILE = 'surgery_action_labels_filtered.json'

surgery_files = os.listdir(ROOT_DIR)
ft_files = [names for names in surgery_files if '_ft_' in names]
orig_labels_f = open(os.path.join(ROOT_DIR, ORIG_LABELS_FILE), 'r')

orig_labels_dict = json.load(orig_labels_f)
ft_labels_dict = {}

for ft_file in ft_files:
    ft_f = open(os.path.join(ROOT_DIR, ft_file), 'r')
    ft_dict = json.load(ft_f)
    for key, values in ft_dict.items():
        if key not in ft_labels_dict:
            ft_labels_dict[key] = values
    ft_f.close()

surgery_labels_ft_test_file = 'surgery_action_labels_filtered_for_ft.json'
ft_test_f = open(os.path.join(ROOT_DIR, surgery_labels_ft_test_file), 'w')
ft_test_dict = {}
for key, values in orig_labels_dict.items():
    if key not in ft_labels_dict:
        ft_test_dict[key] = values
json.dump(ft_test_dict, ft_test_f)
ft_test_f.close()
print("Finished for fine-tune labels")
