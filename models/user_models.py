from pydantic import BaseModel

class User(BaseModel):
    '''
    Information stored for each user.
    '''
    user_id: int
    name: str
    email: str
    password: str
    age: int
    gender: str
    created_at: str
    updated_at: str


class UserPreference(BaseModel):
    '''
    When a user likes a song, we'll
    store the respective song_id
    '''
    user_id: int
    song_id: int
    created_at: str

class UserHistory(BaseModel):
    '''
    The history of the user's listening
    '''
    user_id: int
    song_id: int
    created_at: str

class UserPlaylist(BaseModel):
    '''
    The playlists created by the user
    '''
    user_id: int
    playlist_id: int
    name: str
    created_at: str
    updated_at: str