from fastapi import FastAPI

from routes import music_routes
from core.config import psql_conn

app = FastAPI()

def get_db():
    try:
        yield psql_conn
    finally:
        psql_conn.close()

app.include_router(music_routes.router, prefix="/music", tags=["music"])