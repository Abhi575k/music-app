from fastapi import APIRouter

from models.music_models import Music
from services.music_service import get_top_music_unauthenticated, get_genre_music_unauthenticated


# DATABASE
from core.constants import MUSIC_GENRE, SONGS_DB
##

router = APIRouter()

@router.get("/", status_code=200, response_model=list[Music])
async def read_music(offset: int = 0, limit: int = 5):
    '''
    Function to return the list of music
    in the database. Since the list can be
    long, we'll return the most popular
    songs and a few random ones, totalling
    up to 5.

    If the user is authenticated, we'll return
    the top songs based on their preferences and
    listening history and a few random ones.
    '''
    music_list = get_top_music_unauthenticated(offset, limit)
    return music_list

@router.get("/genre/{genre}", status_code=200, response_model=list[Music])
async def read_music_by_genre(genre: str, offset: int = 0, limit: int = 5):
    '''
    Function to return the list of music
    based on the genre provided. If the genre
    is not found, we'll return a message to the
    user. The list is sorted by popularity and
    100 songs are returned per page.
    '''
    music_list = get_genre_music_unauthenticated(genre, offset, limit)
    return music_list

@router.get("/genre", status_code=200)
async def read_music_genre():
    return {"music": MUSIC_GENRE}