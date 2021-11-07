import json
import os

old_f = open('../examples/MMPT/data/coin/COIN.json', 'r')
new_f = open('../examples/MMPT/data/coin/COIN_short.json', 'w')

coin_data = json.load(old_f)
short_coin_data = {}
new_coin_data = {}
NUM_TEST_SAMPLES = 10

i = 0
for key, item in coin_data['database'].items():
    if item['subset'] == 'testing':
        short_coin_data[key] = item
        i += 1
        if i > NUM_TEST_SAMPLES:
            break

new_coin_data['database'] = short_coin_data
json.dump(new_coin_data, new_f)
new_f.close()
print("Finished creating new COIN json file")
