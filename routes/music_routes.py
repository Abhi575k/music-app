from fastapi import APIRouter

# import errors
from fastapi import HTTPException

from models.music_models import Music, Genre, Artist, Album
from services.music_service import get_top_music_unauthenticated, get_genre_list, get_genre_music_unauthenticated, get_artist_list, get_artist_music_unauthenticated, get_album_list, get_album_music_unauthenticated

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

    if music_list is None:
        raise HTTPException(status_code=404, detail="No music found")
    
    return music_list

@router.get("/genre", status_code=200, response_model=list[Genre])
async def read_music_genre():
    '''
    Function to return the list of genres
    '''
    genre_list = get_genre_list()

    if genre_list is None:
        raise HTTPException(status_code=404, detail="No genres found")
    
    return genre_list

@router.get("/genre/{genre_id}", status_code=200, response_model=list[Music])
async def read_music_by_genre(genre_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the list of music
    based on the genre provided. If the genre
    is not found, we'll return a message to the
    user. The list is sorted by popularity and
    100 songs are returned per page.

    If the user is authenticated, we'll return
    the top songs based on their preferences and
    listening history and a few random ones.
    '''
    music_list = get_genre_music_unauthenticated(genre_id, offset, limit)

    if music_list is None:
        raise HTTPException(status_code=404, detail="No music found")
    
    return music_list

@router.get("/artist", status_code=200, response_model=list[Artist])
async def read_music_artist():
    '''
    Function to return the list of artists
    '''

    artist_list = get_artist_list()

    if artist_list is None:
        raise HTTPException(status_code=404, detail="No artists found")
    
    return artist_list

@router.get("/artist/{artist_id}", status_code=200, response_model=list[Music])
async def read_music_by_artist(artist_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the list of music
    based on the artist provided. If the artist
    is not found, we'll return a message to the
    user. The list is sorted by popularity and
    100 songs are returned per page.

    If the user is authenticated, we'll return
    the top songs based on their preferences and
    listening history and a few random ones.
    '''
    music_list = get_artist_music_unauthenticated(artist_id, offset, limit)

    if music_list is None:
        raise HTTPException(status_code=404, detail="No music found")
    
    return music_list

@router.get("/album", status_code=200, response_model=list[Album])
async def read_music_album():
    '''
    Function to return the list of albums
    '''

    album_list = get_album_list()

    if album_list is None:
        raise HTTPException(status_code=404, detail="No albums found")
    
    return album_list

@router.get("/album/{album_id}", status_code=200, response_model=list[Music])
async def read_music_by_album(album_id: int, offset: int = 0, limit: int = 5):
    '''
    Function to return the list of music
    based on the album provided. If the album
    is not found, we'll return a message to the
    user. The list is sorted by popularity and
    100 songs are returned per page.

    If the user is authenticated, we'll return
    the top songs based on their preferences and
    listening history and a few random ones.
    '''
    music_list = get_album_music_unauthenticated(album_id, offset, limit)

    if music_list is None:
        raise HTTPException(status_code=404, detail="No music found")
    
    return music_list