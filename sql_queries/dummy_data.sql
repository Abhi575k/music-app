-- Insert dummy data
\c music_db

-- Insert into artist
-- Create 10 artists
INSERT INTO artist (name, popularity) VALUES
('Artist 1', 85.5),
('Artist 2', 90.0),
('Artist 3', 75.3),
('Artist 4', 80.0),
('Artist 5', 85.0),
('Artist 6', 70.0),
('Artist 7', 75.0),
('Artist 8', 80.0),
('Artist 9', 85.0),
('Artist 10', 90.0);

-- Insert into album
-- Each artist has 2 albums
INSERT INTO album (title, artist_id, release_date, popularity) VALUES
('Album 1', 1, '2022-01-01', 80.0),
('Album 2', 2, '2023-03-15', 85.0),
('Album 3', 3, '2021-07-20', 78.0),
('Album 4', 4, '2020-05-10', 75.0),
('Album 5', 5, '2019-12-25', 70.0),
('Album 6', 6, '2018-10-30', 65.0),
('Album 7', 7, '2017-08-15', 60.0),
('Album 8', 8, '2016-06-05', 55.0),
('Album 9', 9, '2015-04-20', 50.0),
('Album 10', 10, '2014-02-10', 45.0),
('Album 11', 1, '2013-01-01', 40.0),
('Album 12', 2, '2012-03-15', 35.0),
('Album 13', 3, '2011-07-20', 30.0),
('Album 14', 4, '2010-05-10', 25.0),
('Album 15', 5, '2009-12-25', 20.0),
('Album 16', 6, '2008-10-30', 15.0),
('Album 17', 7, '2007-08-15', 10.0),
('Album 18', 8, '2006-06-05', 5.0),
('Album 19', 9, '2005-04-20', 2.0),
('Album 20', 10, '2004-02-10', 1.0);

-- Insert into genre
-- Create 10 genres
INSERT INTO genre (name, popularity) VALUES
('Pop', 90.0),
('Rock', 85.0),
('Jazz', 70.0),
('Hip Hop', 75.0),
('R&B', 80.0),
('Country', 65.0),
('Blues', 60.0),
('Reggae', 55.0),
('Classical', 50.0),
('Electronic', 45.0);

-- Insert into music
-- Each album has 2 songs
INSERT INTO music (title, artist_id, album_id, genre_id, duration, tempo) VALUES
('Song 1', 1, 1, 1, 3.5, 120.0),
('Song 2', 2, 2, 2, 4.0, 130.0),
('Song 3', 3, 3, 3, 5.0, 110.0),
('Song 4', 4, 4, 4, 3.0, 140.0),
('Song 5', 5, 5, 5, 4.5, 100.0),
('Song 6', 6, 6, 6, 2.5, 150.0),
('Song 7', 7, 7, 7, 3.5, 120.0),
('Song 8', 8, 8, 8, 4.0, 130.0),
('Song 9', 9, 9, 9, 5.0, 110.0),
('Song 10', 10, 10, 10, 3.0, 140.0),
('Song 11', 1, 11, 1, 4.5, 100.0),
('Song 12', 2, 12, 2, 2.5, 150.0),
('Song 13', 3, 13, 3, 3.5, 120.0),
('Song 14', 4, 14, 4, 4.0, 130.0),
('Song 15', 5, 15, 5, 5.0, 110.0),
('Song 16', 6, 16, 6, 3.0, 140.0),
('Song 17', 7, 17, 7, 4.5, 100.0),
('Song 18', 8, 18, 8, 2.5, 150.0),
('Song 19', 9, 19, 9, 3.5, 120.0),
('Song 20', 10, 20, 10, 4.0, 130.0),
('Song 21', 1, 1, 1, 5.0, 110.0),
('Song 22', 2, 2, 2, 3.0, 140.0),
('Song 23', 3, 3, 3, 4.5, 100.0),
('Song 24', 4, 4, 4, 2.5, 150.0),
('Song 25', 5, 5, 5, 3.5, 120.0),
('Song 26', 6, 6, 6, 4.0, 130.0),
('Song 27', 7, 7, 7, 5.0, 110.0),
('Song 28', 8, 8, 8, 3.0, 140.0),
('Song 29', 9, 9, 9, 4.5, 100.0),
('Song 30', 10, 10, 10, 2.5, 150.0),
('Song 31', 1, 11, 1, 3.5, 120.0),
('Song 32', 2, 12, 2, 4.0, 130.0),
('Song 33', 3, 13, 3, 5.0, 110.0),
('Song 34', 4, 14, 4, 3.0, 140.0),
('Song 35', 5, 15, 5, 4.5, 100.0),
('Song 36', 6, 16, 6, 2.5, 150.0),
('Song 37', 7, 17, 7, 3.5, 120.0),
('Song 38', 8, 18, 8, 4.0, 130.0),
('Song 39', 9, 19, 9, 5.0, 110.0),
('Song 40', 10, 20, 10, 3.0, 140.0);

-- Insert into user_profile
-- Create 2 users
INSERT INTO user_profile (name, email, password, age, gender, created_at, updated_at) VALUES
('User 1', 'user1@example.com', 'password1', 25, 'M', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('User 2', 'user2@example.com', 'password2', 30, 'F', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert into user_preference
-- Each user has 10 preferences
INSERT INTO user_preference (user_id, song_id, created_at) VALUES
(1, 1, CURRENT_TIMESTAMP),
(2, 2, CURRENT_TIMESTAMP),
(1, 3, CURRENT_TIMESTAMP),
(2, 4, CURRENT_TIMESTAMP),
(1, 5, CURRENT_TIMESTAMP),
(2, 6, CURRENT_TIMESTAMP),
(1, 7, CURRENT_TIMESTAMP),
(2, 8, CURRENT_TIMESTAMP),
(1, 9, CURRENT_TIMESTAMP),
(2, 10, CURRENT_TIMESTAMP),
(1, 11, CURRENT_TIMESTAMP),
(2, 12, CURRENT_TIMESTAMP),
(1, 13, CURRENT_TIMESTAMP),
(2, 14, CURRENT_TIMESTAMP),
(1, 15, CURRENT_TIMESTAMP),
(2, 16, CURRENT_TIMESTAMP),
(1, 17, CURRENT_TIMESTAMP),
(2, 18, CURRENT_TIMESTAMP),
(1, 19, CURRENT_TIMESTAMP),
(2, 20, CURRENT_TIMESTAMP);

-- Insert into user_history
-- Each user has 10 history
INSERT INTO user_history (user_id, song_id, created_at) VALUES
(1, 2, CURRENT_TIMESTAMP),
(2, 3, CURRENT_TIMESTAMP),
(1, 4, CURRENT_TIMESTAMP),
(2, 5, CURRENT_TIMESTAMP),
(1, 6, CURRENT_TIMESTAMP),
(2, 7, CURRENT_TIMESTAMP),
(1, 8, CURRENT_TIMESTAMP),
(2, 9, CURRENT_TIMESTAMP),
(1, 10, CURRENT_TIMESTAMP),
(2, 11, CURRENT_TIMESTAMP),
(1, 12, CURRENT_TIMESTAMP),
(2, 13, CURRENT_TIMESTAMP),
(1, 14, CURRENT_TIMESTAMP),
(2, 15, CURRENT_TIMESTAMP),
(1, 16, CURRENT_TIMESTAMP),
(2, 17, CURRENT_TIMESTAMP),
(1, 18, CURRENT_TIMESTAMP),
(2, 19, CURRENT_TIMESTAMP),
(1, 20, CURRENT_TIMESTAMP),
(2, 1, CURRENT_TIMESTAMP);

-- Insert into user_playlist
-- Each user has 2 playlists
INSERT INTO user_playlist (user_id, name, created_at) VALUES
(1, 'Playlist 1', CURRENT_TIMESTAMP),
(2, 'Playlist 2', CURRENT_TIMESTAMP),
(1, 'Playlist 3', CURRENT_TIMESTAMP),
(2, 'Playlist 4', CURRENT_TIMESTAMP);

-- Insert into playlist_music
-- Each playlist has 5 songs
INSERT INTO playlist_music (playlist_id, song_id, created_at) VALUES
(1, 1, CURRENT_TIMESTAMP),
(2, 2, CURRENT_TIMESTAMP),
(1, 3, CURRENT_TIMESTAMP),
(2, 4, CURRENT_TIMESTAMP),
(1, 5, CURRENT_TIMESTAMP),
(2, 6, CURRENT_TIMESTAMP),
(1, 7, CURRENT_TIMESTAMP),
(2, 8, CURRENT_TIMESTAMP),
(1, 9, CURRENT_TIMESTAMP),
(2, 10, CURRENT_TIMESTAMP),
(1, 11, CURRENT_TIMESTAMP),
(2, 12, CURRENT_TIMESTAMP),
(1, 13, CURRENT_TIMESTAMP),
(2, 14, CURRENT_TIMESTAMP),
(1, 15, CURRENT_TIMESTAMP),
(2, 16, CURRENT_TIMESTAMP),
(1, 17, CURRENT_TIMESTAMP),
(2, 18, CURRENT_TIMESTAMP),
(1, 19, CURRENT_TIMESTAMP),
(2, 20, CURRENT_TIMESTAMP);