'''
Created on 07-May-2020

@author: raghuveer
'''
song="JINGLE Bells jingle Bells Jingle All The Way"
song.lower()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)