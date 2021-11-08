import json
import os

VIDEOS_DIR = '../examples/MMPT/data/coin/videos'
COIN_JSON_FILE = '../examples/MMPT/data/coin/COIN_short.json'
COIN_JSON_FILE_NEW = '../examples/MMPT/data/coin/COIN_match.json'

coin_file_old = open(COIN_JSON_FILE, 'r')
coin_file_new = open(COIN_JSON_FILE_NEW, 'w')
coin_old_dict = json.load(coin_file_old)

videos = os.listdir(VIDEOS_DIR)
video_names = [names.split('.')[0] for names in videos]

coin_dict_new = {}

for key, value in coin_old_dict['database'].items():
    if key in video_names:
        coin_dict_new[key] = value

final_coin_dict_new = {}
final_coin_dict_new['database'] = coin_dict_new

json.dump(final_coin_dict_new, coin_file_new)
print("Finished wriitng new JSON file")

coin_file_old.close()
coin_file_new.close()
