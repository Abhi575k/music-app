from models.music_models import Music, Genre, Artist, Album

from core.config import psql_conn

def get_top_music_unauthenticated(offset: int = 0, limit: int = 5):
    '''
    Function to return the top music
    for unauthenticated users. We'll return
    the list of music from the database
    based on the offset and limit provided.

    TODO: Need to add more randomness so that the
    user can discover new music.
    '''
    music_list = list[Music]
    
    # Buisness Logic
    # Use artist_id to get artist popularity
    query = f'''
        SELECT m.song_id, m.title, m.artist_id, m.album_id, m.genre_id, m.duration, m.tempo
        FROM music m
        JOIN artist a ON m.artist_id = a.artist_id
        JOIN album al ON m.album_id = al.album_id
        JOIN genre g ON m.genre_id = g.genre_id
        ORDER BY a.popularity DESC, al.popularity DESC, g.popularity DESC
        LIMIT {limit} OFFSET {offset};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None
    
    music_list = query_result

    return music_list

def get_top_music_authenticated(offset: int = 0, limit: int = 5):
    return None

def get_genre_list():
    '''
    Function to return the list of genres
    available in the database. We'll return
    the list of genres from the database.
    '''
    genre_list = list[Genre]
    
    query = '''
        SELECT * FROM genre;
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    genre_list = query_result

    return genre_list

def get_genre_music_unauthenticated(genre_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the music based on
    the genre provided. We'll return the
    list of music from the database based
    on the genre and page number provided.

    If the genre is not found, we'll return
    a message to the user.

    TODO: Need to add more randomness so that the
    user can discover new music.
    '''
    music_list = list[Music]

    query = f'''
        SELECT * FROM genre WHERE genre_id = {genre_id};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None
    
    query = f'''
        SELECT m.song_id, m.title, m.artist_id, m.album_id, m.genre_id, m.duration, m.tempo
        FROM music m
        JOIN artist a ON m.artist_id = a.artist_id
        JOIN album al ON m.album_id = al.album_id
        JOIN genre g ON m.genre_id = g.genre_id
        WHERE m.genre_id = {genre_id}
        ORDER BY a.popularity DESC, al.popularity DESC, g.popularity DESC
        LIMIT {limit} OFFSET {offset};
    '''
    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    music_list = query_result

    return music_list

def get_genre_music_authenticated(genre_id: int, offset: int = 0, limit: int = 5):
    return None

def get_artist_list():
    '''
    Function to return the list of artists
    available in the database. We'll return
    the list of artists from the database.
    '''
    artist_list = list[Artist]
    
    query = '''
        SELECT * FROM artist;
    '''
    
    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    artist_list = query_result

    print(artist_list)

    return artist_list

def get_artist_music_unauthenticated(artist_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the music based on
    the artist provided. We'll return the
    list of music from the database based
    on the artist and page number provided.

    If the artist is not found, we'll return
    a message to the user.
    '''
    music_list = list[Music]

    query = f'''
        SELECT * FROM artist WHERE artist_id = {artist_id};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    query = f'''
        SELECT m.song_id, m.title, m.artist_id, m.album_id, m.genre_id, m.duration, m.tempo
        FROM music m
        JOIN artist a ON m.artist_id = a.artist_id
        JOIN album al ON m.album_id = al.album_id
        JOIN genre g ON m.genre_id = g.genre_id
        WHERE m.artist_id = {artist_id}
        ORDER BY a.popularity DESC, al.popularity DESC, g.popularity DESC
        LIMIT {limit} OFFSET {offset};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    music_list = query_result

    return music_list

def get_artist_music_authenticated(artist_id: int, offset: int = 0, limit: int = 5):
    return None

def get_album_list():
    '''
    Function to return the list of albums
    available in the database. We'll return
    the list of albums from the database.
    '''
    album_list = list[Album]
    
    query = '''
        SELECT * FROM album;
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    album_list = query_result

    return album_list

def get_album_music_unauthenticated(album_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the music based on
    the album provided. We'll return the
    list of music from the database based
    on the album and page number provided.

    If the album is not found, we'll return
    a message to the user.
    '''
    music_list = list[Music]

    query = f'''
        SELECT * FROM album WHERE album_id = {album_id};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    query = f'''
        SELECT m.song_id, m.title, m.artist_id, m.album_id, m.genre_id, m.duration, m.tempo
        FROM music m
        JOIN artist a ON m.artist_id = a.artist_id
        JOIN album al ON m.album_id = al.album_id
        JOIN genre g ON m.genre_id = g.genre_id
        WHERE m.album_id = {album_id}
        ORDER BY a.popularity DESC, al.popularity DESC, g.popularity DESC
        LIMIT {limit} OFFSET {offset};
    '''

    try:
        psql_conn.execute(query)
        query_result = psql_conn.fetchall()
    except:
        return None

    music_list = query_result

    return music_list

def get_album_music_authenticated(album_id: int, offset: int = 0, limit: int = 5):
    return None

