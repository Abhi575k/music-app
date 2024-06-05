-- Insert dummy data
\c music_db

-- Insert into artist
INSERT INTO artist (name, popularity) VALUES
('Artist 1', 85.5),
('Artist 2', 90.0),
('Artist 3', 75.3);

-- Insert into album
INSERT INTO album (title, artist_id, release_date, popularity) VALUES
('Album 1', 1, '2022-01-01', 80.0),
('Album 2', 2, '2023-03-15', 85.0),
('Album 3', 3, '2021-07-20', 78.0);

-- Insert into genre
INSERT INTO genre (name, popularity) VALUES
('Pop', 90.0),
('Rock', 85.0),
('Jazz', 70.0);

-- Insert into music
INSERT INTO music (title, artist_id, album_id, genre_id, duration, tempo) VALUES
('Song 1', 1, 1, 1, 3.5, 120.0),
('Song 2', 2, 2, 2, 4.0, 130.0),
('Song 3', 3, 3, 3, 5.0, 110.0);

-- Insert into user_profile
INSERT INTO user_profile (name, email, password, age, gender, created_at, updated_at) VALUES
('User 1', 'user1@example.com', 'password1', 25, 'M', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('User 2', 'user2@example.com', 'password2', 30, 'F', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert into user_preference
INSERT INTO user_preference (user_id, song_id, created_at) VALUES
(1, 1, CURRENT_TIMESTAMP),
(2, 2, CURRENT_TIMESTAMP);

-- Insert into user_history
INSERT INTO user_history (user_id, song_id, created_at) VALUES
(1, 2, CURRENT_TIMESTAMP),
(2, 3, CURRENT_TIMESTAMP);

-- Insert into user_playlist
INSERT INTO user_playlist (user_id, name, created_at) VALUES
(1, 'Playlist 1', CURRENT_TIMESTAMP),
(2, 'Playlist 2', CURRENT_TIMESTAMP);

-- Insert into playlist_music
INSERT INTO playlist_music (playlist_id, song_id, created_at) VALUES
(1, 1, CURRENT_TIMESTAMP),
(2, 2, CURRENT_TIMESTAMP);