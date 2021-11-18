import os
import nltk
from nltk import FreqDist
import json
import re
import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

ROOT_DIR = '../examples/MMPT/data/youtube-jomi-dataset'
CAPTION_FILE = 'raw_caption_jomi.json'

caption_f = open(os.path.join(ROOT_DIR, CAPTION_FILE), 'r')

caption_dict = json.load(caption_f)

nouns_list, verbs_list = [], []

for video_id, values in caption_dict.items():
    video_text_list = caption_dict[video_id]['text']
    for video_text in video_text_list:
        video_text = re.sub(r'[^\w\s]','',video_text)
        video_text = video_text.strip()
        video_tokens = nltk.word_tokenize(video_text)
        video_tagged_tokens = nltk.pos_tag(video_tokens)
        video_nouns = [token[0] for token in video_tagged_tokens if token[1] in ['NN', 'NNP']]
        video_verbs = [token[0] for token in video_tagged_tokens if token[1] in ['VP', 'VBD', 'VBP']]
        nouns_list.extend(video_nouns)
        verbs_list.extend(video_verbs)

print("Finished gathering all nouns and verbs")

fdist_nouns = FreqDist(nouns_list)
fdist_verbs = FreqDist(verbs_list)

print("Most common nouns")
print(fdist_nouns.most_common())
noun_words = [noun_pair[0] for noun_pair in fdist_nouns.most_common()]
noun_counts = [noun_pair[1] for noun_pair in fdist_nouns.most_common()]
sns.barplot(noun_counts[:30], noun_words[:30], x='frequency', y='word')
plt.savefig('../examples/MMPT/data/youtube-jomi-dataset/noun_counts.png')

print("Most common verbs")
print(fdist_verbs.most_common())

verb_words = [verb_pair[0] for verb_pair in fdist_verbs.most_common()]
verb_counts = [verb_pair[1] for verb_pair in fdist_verbs.most_common()]
sns.barplot(verb_counts[:30], verb_words[:30], x='frequency', y='word')
plt.savefig('../examples/MMPT/data/youtube-jomi-dataset/verb_counts.png')
