from models.music_models import Music

import random

# DATABASE
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
psql_conn = None

try:
    conn = connect(
        dbname='music_db',
        user='abhinav',
        password='password',
        port='5432',
        cursor_factory=RealDictCursor
    )
    psql_conn = conn.cursor()
    print('Connected to the database')
except Exception as e:
    print(f'An error occurred: {e}')
##

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
    query = f"SELECT * FROM music LIMIT {limit} OFFSET {offset}"
    psql_conn.execute(query)
    query_result = psql_conn.fetchall()
    print(query_result)
    music_list = query_result

    # Convert the query result to a list of Music objects
    # for the API to return
    music_list = [Music(**music) for music in music_list]

    return music_list

def get_top_music_authenticated(offset: int = 0, limit: int = 5):
    return None

def get_genre_music_unauthenticated(genre: str, offset: int = 0, limit: int = 5):
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
    
    # Buisness Logic
    music_list = SONGS_DB[offset:offset+limit]

    return music_list