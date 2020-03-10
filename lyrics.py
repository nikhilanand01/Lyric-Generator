import requests
import pickle
import string
from collections import Counter
from bs4 import BeautifulSoup
from numpy.random import choice
import sys

#Links to song lyrics for Khalid's Suncity EP, in order appearance on EP (exluding interludes)
url = 'https://www.metrolyrics.com/vertigo-lyrics-khalid.html'
# url = 'https://www.metrolyrics.com/saturday-nights-lyrics-khalid.html'
# url = 'https://www.metrolyrics.com/motion-lyrics-khalid.html'
# url = 'https://www.metrolyrics.com/better-lyrics-khalid.html'
# url = 'https://www.metrolyrics.com/suncity-lyrics-khalid.html'


res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.findAll("p", {"class": "verse"})
songList = []
song = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script',
    'iframe',
]

for t in text:
	if t.parent.name not in blacklist:
		song += '{} '.format(t)

#clean song lyrics
song = song.replace('<br/>','')
song = song.replace('</p>','')
song = song.replace('<p class="verse">','')
song = song.replace(" ' ",'')
song = song.replace(',','')
song = song.replace('[','')
song = song.replace(']','')
song = song.replace('(','')
song = song.replace(')','')
song = song.replace('.','')
song = song.replace('?','')
song = song.replace('!','')
song = song.lower()
songList = song.split()

#add songs to txt file with all songs. For the first song use 'w' as the second open parameter, then change to a for all additional songs
filename = open('discog.txt','a')
filename.write(song)
filename.close()
