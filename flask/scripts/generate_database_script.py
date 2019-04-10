from random import randint

temporary_words = list(open("1000_words.txt"))
words = []
for word in temporary_words:
    words.append(word.capitalize().strip("\n"))

genres = [(1, 'Grunge'),
          (2, 'Alternative'),
          (3, 'Rock'),
          (4, 'Blues'),
          (5, 'Pop'),
          (6, 'Jazz'),
          (7, 'Classical'),
          (8, 'EDM'),
          (9, 'Dance'),
          (10, 'Funk'),
          (11, 'R&B'),
          (12, 'Soul'),
          (13, 'Metal'),
          (14, 'Acoustic'),
          (15, 'Acapella'),
          (16, 'Indie'),
          (17, 'Folk'),
          (18, 'Country'),
          (19, 'Soundtrack'),
          (20, 'Hip-Hop'),
          (21, 'Trap'),
          (22, 'Electronic'),
          (23, 'Rap'),
          (24, 'House'),
          (25, 'Tropical House'),
          (26, 'Lo-fi')]


def make_string_of_random_words(number_of_words_min, number_of_words_max):
    random_string = []
    number_of_words = randint(number_of_words_min, number_of_words_max)
    for _ in range(number_of_words):
        random_string.append(words[randint(0, len(words) - 1)])

    return str(" ".join(random_string))


class Song:
    song_id = 10000000

    def __init__(self, artist_id, album_id, genre_id):
        self.title = make_string_of_random_words(1, 7)
        self.artist_id = artist_id
        self.album_id = album_id
        self.genre = genre_id
        self.duration = randint(150, 300)
        self.song_id = Song.song_id
        Song.song_id += 1

    def to_string(self):
        return """({}, {}, {}, "{}", {})""".format(self.song_id, self.album_id, self.artist_id, self.title,
                                                   self.duration)


class Album:
    album_id = 10000000

    def __init__(self, artist_id, year):
        self.year = year
        self.title = make_string_of_random_words(1, 4)
        self.artist_id = artist_id
        self.genre_id = genres[randint(0, len(genres) - 1)][0]
        self.description = make_string_of_random_words(10, 30)
        self.album_id = Album.album_id
        Album.album_id += 1

        self.songs = []
        for _ in range(randint(5, 10)):
            self.songs.append(Song(self.artist_id, self.album_id, self.genre_id))

    def to_string(self):
        return """({}, "{}", {}, {}, {})""".format(self.album_id, self.title, self.year, self.artist_id, self.genre_id)


class Artist:
    artist_id = 10000000

    def __init__(self):
        self.artist_id = Artist.artist_id
        Artist.artist_id += 1
        self.artist_name = make_string_of_random_words(1, 4)
        self.albums = []
        min_year = randint(1960, 2018)
        max_year = randint(min_year, 2019)
        self.years_active = max_year - min_year

        for _ in range(randint(1, 5)):
            self.albums.append(Album(self.artist_id, randint(min_year, max_year)))

    def to_string(self):
        return """({}, "{}", {})""".format(self.artist_id, self.artist_name, self.years_active)


artists_insert_string = "INSERT INTO Artists (artist_id, artist_name, years_active) VALUES "
albums_insert_string = "INSERT INTO Albums (album_id, title, year, artist_id, genre_id) VALUES "
songs_insert_string = "INSERT INTO Songs (song_id, album_id, artist_id, title, duration) VALUES "

artists = []
albums = []
songs = []

for i in range(100):
    artist = Artist()
    artists.append(artist.to_string())

    for album in artist.albums:
        albums.append(album.to_string())

        for song in album.songs:
            songs.append(song.to_string())

for artist in artists:
    artists_insert_string = artists_insert_string + artist + ",\n"
index_to_remove = artists_insert_string.rfind(",\n")
artists_insert_string = artists_insert_string[0:index_to_remove]
artists_insert_string = artists_insert_string + ";\n\n"

for album in albums:
    albums_insert_string = albums_insert_string + album + ",\n"
index_to_remove = albums_insert_string.rfind(",\n")
albums_insert_string = albums_insert_string[0:index_to_remove]
albums_insert_string = albums_insert_string + ";\n\n"

for song in songs:
    songs_insert_string = songs_insert_string + song + ",\n"
index_to_remove = songs_insert_string.rfind(",\n")
songs_insert_string = songs_insert_string[0:index_to_remove]
songs_insert_string = songs_insert_string + ";\n\n"

with open("db_init/generate_much.sql", "w") as file:
    file.write("USE glo2005;\n\n")
    file.write(artists_insert_string)
    file.write(albums_insert_string)
    file.write(songs_insert_string)
