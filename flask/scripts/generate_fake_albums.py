from random import randint
import json


tempwords = list(open("1000_words.txt"))
words = []
for word in tempwords:
    words.append(word.capitalize().strip("\n"))


genres = ["Rock", "Soul", "Rap", "Classical", "Jazz", "Blues", "R&B"]
albums = []

class Song:
    def __init__(self,year,artist,album,genre):
        self.dict = {}
        self.dict["title"] = words[randint(0,len(words)-1)] +" "+ words[randint(0,len(words)-1)] +" "+ words[randint(0,len(words)-1)]+" "+ words[randint(0,len(words)-1)]
        self.dict["artist"] = artist
        self.dict["album"] = album
        self.dict["genre"] = genre
        self.dict["duration"] = randint(150,300)
        self.dict["year"] = year

    def todict(self):

        return self.dict




class Album:
    def __init__(self):
        self.dict = {}

        year = randint(1960,2019)
        self.songs = []
        album = words[randint(0,len(words)-1)] +" "+ words[randint(0,len(words)-1)] +" "+ words[randint(0,len(words)-1)]
        artist = words[randint(0,len(words)-1)] +" "+ words[randint(0,len(words)-1)]
        genre = genres[randint(0,len(genres)-1)]

        self.dict["album"] = album
        self.dict["artist"] = artist
        self.dict["genre"] = genre

        for i in range(randint(5,10)):
            self.songs.append(Song(year,artist,album,genre).todict())

        self.dict["songs"] = self.songs

    def todict(self):

        return self.dict



for i in range(100):
    albums.append(Album().todict())



with open("albums.txt","w") as file:
    json.dump(albums,file)






