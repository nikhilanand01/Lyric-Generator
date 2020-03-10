#Code to get create a randomly generated song
#run the program 'python3 markov.py' and the results will be added to the No1_Singles.txt file


import numpy as np
from numpy.random import choice
import string
import random

#read the lyrics that was pull and stored from lyrics.py file
lyric_base = open('discog.txt', encoding='utf8').read()

#split the text file into single words.
#Note I removed all the punctuation in, so our simulated text has no punctuation
corpus = lyric_base.split()

#function to give us all the pairs of words in the speeches
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus)

#Instantiate an empty dictionary, and fill it words from our pairs.
#If the first word of the pair is already a key in the dictionary, simply append the next word to the list of words that follow that word.
#Otherwise, initialize a new entry in the dictionary with the key equal to the first word and the value a list of length one.
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)

while first_word.islower():
    first_word = np.random.choice(corpus)


#pick a random word to kick off the chain, and choose a random number of words that the song will be
chain = [first_word]
n_words = random.randint(150, 400)

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))


#The join command returns the chain as a string and finalProduct formats the results to be placed in the No1_Singles.txt file
finalSong = ' '.join(chain)
# print(finalSong)
finalProduct = finalSong + "\n\n" + "*******" + "\n"
# print(finalProduct)

filename = open('No1_Singles.txt','a')
filename.write(finalProduct)
filename.close()
