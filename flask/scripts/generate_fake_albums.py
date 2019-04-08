from random import randint

tempwords = list(open("1000_words.txt"))
words = []
for word in tempwords:
    words.append(word.capitalize().strip("\n"))

genres = ["Rock", "Soul", "Rap", "Classical", "Jazz", "Blues", "R&B"]
albums = []
album_id = 10000000
song_id = 10000000


class Song:
    def __init__(self, year, artist_name, album_name, genre):
        self.title = words[randint(0, len(words) - 1)] + " " + words[randint(0, len(words) - 1)] + " " + words[
            randint(0, len(words) - 1)] + " " + words[randint(0, len(words) - 1)]
        self.artist_name = artist_name
        self.album_name = album_name
        self.genre = genre
        self.duration = randint(150, 300)
        self.year = year


def make_string_of_random_words(number_of_words):
    random_string = []
    for i in range(number_of_words):
        random_string.append(words[randint(0, len(words) - 1)])

    return str(" ".join(random_string))


class Album:
    def __init__(self):
        self.year = randint(1960, 2019)
        self.album_name = make_string_of_random_words(3)
        self.artist_name = make_string_of_random_words(2)
        self.genre = genres[randint(0, len(genres) - 1)]
        self.description = make_string_of_random_words(20)

        self.songs = []
        for i in range(randint(5, 10)):
            self.songs.append(Song(self.year, self.artist_name, self.album_name, self.genre))


for i in range(100):
    albums.append(Album())

with open("albums.sql", "w") as file:
    file.write("USE glo2005;\n")
    file.write("CREATE TABLE IF NOT EXISTS Albums(id INTEGER NOT NULL, \
 year SMALLINT, genre VARCHAR(256), title VARCHAR(256), description TEXT,\
 PRIMARY KEY (id));\n\n")

    file.write("CREATE TABLE IF NOT EXISTS Songs(id INTEGER NOT NULL,\
 year SMALLINT, genre VARCHAR(256), title VARCHAR(256), duration SMALLINT,\
 PRIMARY KEY (id));\n\n")

    for album in albums:
        file.write("""INSERT INTO Albums (id, year, genre, title, description) VALUES ({}, {}, "{}", "{}", "{}");\n"""
                   .format(album_id, album.year, album.genre, album.album_name, album.description))

        for song in album.songs:
            file.write("""INSERT INTO Songs (id, year, genre, title, duration) VALUES ({}, {}, "{}", "{}", {});\n"""
                       .format(song_id, song.year, song.genre, song.title, song.duration))
            song_id += 1
        album_id += 1
