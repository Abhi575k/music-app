\c music_db

-- First create all tables and then add foreign keys

-- class User
CREATE TABLE IF NOT EXISTS user_profile (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    age INT,
    gender VARCHAR(1),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- class UserPreference
CREATE TABLE IF NOT EXISTS user_preference (
    user_id INT,
    song_id INT,
    created_at TIMESTAMP
);

-- class UserHistory
CREATE TABLE IF NOT EXISTS user_history (
    user_id INT,
    song_id INT,
    created_at TIMESTAMP
);

-- class UserPlaylist
CREATE TABLE IF NOT EXISTS user_playlist (
    user_id INT,
    playlist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP
);


-- class Music
CREATE TABLE IF NOT EXISTS music (
    song_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INT,
    album_id INT,
    genre_id INT,
    duration FLOAT,
    tempo FLOAT
);

-- class Artist
CREATE TABLE IF NOT EXISTS artist (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    popularity FLOAT
);

-- class Album
CREATE TABLE IF NOT EXISTS album (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INT,
    release_date DATE,
    popularity FLOAT
);

-- class Genre
CREATE TABLE IF NOT EXISTS genre (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    popularity FLOAT
);

-- class PlaylistMusic
CREATE TABLE IF NOT EXISTS playlist_music (
    playlist_id INT,
    song_id INT,
    created_at TIMESTAMP
);

-- Add foreign keys
ALTER TABLE user_preference ADD FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_preference ADD FOREIGN KEY (song_id) REFERENCES music(song_id);
ALTER TABLE user_history ADD FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE user_history ADD FOREIGN KEY (song_id) REFERENCES music(song_id);
ALTER TABLE user_playlist ADD FOREIGN KEY (user_id) REFERENCES user_profile(user_id);
ALTER TABLE music ADD FOREIGN KEY (artist_id) REFERENCES artist(artist_id);
ALTER TABLE music ADD FOREIGN KEY (album_id) REFERENCES album(album_id);
ALTER TABLE music ADD FOREIGN KEY (genre_id) REFERENCES genre(genre_id);
ALTER TABLE album ADD FOREIGN KEY (artist_id) REFERENCES artist(artist_id);
ALTER TABLE playlist_music ADD FOREIGN KEY (playlist_id) REFERENCES user_playlist(playlist_id);
ALTER TABLE playlist_music ADD FOREIGN KEY (song_id) REFERENCES music(song_id);