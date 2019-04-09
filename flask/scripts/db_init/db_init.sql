CREATE DATABASE IF NOT EXISTS glo2005 CHARACTER SET utf8;

USE glo2005;

DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Users(id INTEGER NOT NULL AUTO_INCREMENT,
 username VARCHAR(64) NOT NULL UNIQUE,
 hashedPassword VARCHAR(60) NOT NULL,
 INDEX indexUser (id ASC),
 PRIMARY KEY (id));


CREATE TABLE IF NOT EXISTS Albums(album_id INTEGER NOT NULL AUTO_INCREMENT,
 title VARCHAR(64) NOT NULL,
 year INTEGER NOT NULL,
 artist_id INTEGER,
 genre_id INTEGER,
 INDEX indexAlbum (album_id ASC),
 PRIMARY KEY (album_id),
 FOREIGN KEY(artist_id) REFERENCES Artists(artist_id),
 FOREIGN KEY(genre_id) REFERENCES Genres(genre_id));

CREATE TABLE IF NOT EXISTS Songs(song_id INTEGER NOT NULL AUTO_INCREMENT,
 album_id INTEGER, artist_id INTEGER, title VARCHAR(64) NOT NULL,
 duration INTEGER NOT NULL,
 INDEX indexSong (song_id ASC),
 PRIMARY KEY (song_id),
 CONSTRAINT fk_Songs_album
    FOREIGN KEY (album_id)
    REFERENCES Albums (album_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fk_Songs_artist
    FOREIGN KEY (artist_id)
    REFERENCES Artists (artist_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Genres(genre_id INTEGER NOT NULL AUTO_INCREMENT,
 genre_name VARCHAR(64) NOT NULL UNIQUE,
 INDEX indexGenre (genre_id ASC),
 PRIMARY KEY (genre_id));

CREATE TABLE IF NOT EXISTS Artists(artist_id INTEGER NOT NULL AUTO_INCREMENT,
artist_name VARCHAR(64) NOT NULL,
years_active INTEGER,
INDEX indexArtist (artist_id ASC),
PRIMARY KEY (artist_id));

CREATE TABLE IF NOT EXISTS Playlists(playlist_id INTEGER NOT NULL AUTO_INCREMENT,
title VARCHAR(64) NOT NULL,
INDEX indexPlaylist (playlist_id ASC),
PRIMARY KEY (playlist_id));

CREATE TABLE IF NOT EXISTS Users_Playlists(user_id INTEGER NOT NULL,
playlist_id INTEGER NOT NULL,
INDEX indexUser (user_id ASC),
INDEX indexPlaylist(playlist_id ASC),
CONSTRAINT fk_Users_Playlists_users
    FOREIGN KEY (user_id)
    REFERENCES Users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fk_Users_Playlists_playlist
    FOREIGN KEY (playlist_id)
    REFERENCES Playlists (playlist_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Playlist_Songs(playlist_id INTEGER NOT NULL,
song_id INTEGER NOT NULL,
INDEX indexPlaylist (playlist_id ASC),
INDEX indexSong (song_id ASC),
CONSTRAINT fk_Playlist_Songs_playlist
    FOREIGN KEY (playlist_id)
    REFERENCES Playlists (playlist_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_Playlist_Songs_song
    FOREIGN KEY (song_id)
    REFERENCES Songs (song_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Album_Songs(song_id INTEGER NOT NULL,
album_id INTEGER NOT NULL,
INDEX indexSong (song_id ASC),
INDEX indexAlbum (album_id ASC),
CONSTRAINT fk_Album_Songs_album
    FOREIGN KEY (album_id)
    REFERENCES Albums (album_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_Album_Songs_song
    FOREIGN KEY (song_id)
    REFERENCES Songs (song_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Artist_Release(album_id INTEGER NOT NULL,
artist_id INTEGER NOT NULL,
INDEX indexAlbum (album_id ASC),
INDEX indexArtist (artist_id ASC),
CONSTRAINT fk_Artist_Release_artist
    FOREIGN KEY (artist_id)
    REFERENCES Artists (artist_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_Artist_Release_album
    FOREIGN KEY (album_id)
    REFERENCES Albums (album_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);








