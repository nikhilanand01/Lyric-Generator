import numpy as np
from numpy.random import choice
import string
import random

lyric_base = open('discog.txt', encoding='utf8').read()

corpus = lyric_base.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)

while first_word.islower():
    first_word = np.random.choice(corpus)

chain = [first_word]

n_words = random.randint(150, 400)

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

finalSong = ' '.join(chain)
# print(finalSong)

finalProduct = finalSong + "\n\n" + "*******" + "\n"
# print(finalProduct)

filename = open('No1_Singles.txt','a')
filename.write(finalProduct)
filename.close()
