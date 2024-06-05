from pydantic import BaseModel

class Music(BaseModel):
    '''
    Class to define the music model.
    '''
    song_id: int
    title: str
    artist_id: int
    album_id: int
    genre_id: int
    duration: float
    tempo: float

class Artist(BaseModel):
    '''
    Class to define the artist model.
    '''
    artist_id: int
    name: str
    popularity: int

class Album(BaseModel):
    '''
    Class to define the album model.
    '''
    album_id: int
    title: str
    artist_id: int
    release_date: str
    popularity: int

class Genre(BaseModel):
    '''
    Class to define the genre model.
    '''
    genre_id: int
    name: str
    popularity: int

class PlaylistMusic(BaseModel):
    '''
    Class to define the playlist music model.
    '''
    playlist_id: int
    song_id: int
    created_at: str
