from models.music_models import Music

import random

# DATABASE
from core.constants import SONGS_DB
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
    music_list = SONGS_DB[offset:offset+limit]

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