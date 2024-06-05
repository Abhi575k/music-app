from pydantic import BaseModel

class Music(BaseModel):
    '''
    Class to define the music model.
    '''
    title: str
    artist: str
    genre: str
    popularity: int
    song_id: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True