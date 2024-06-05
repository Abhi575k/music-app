from fastapi import FastAPI

from routes import music_routes

app = FastAPI()

app.include_router(music_routes.router, prefix="/music", tags=["music"])