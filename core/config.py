# config.py
from psycopg2 import connect
from psycopg2.extras import RealDictCursor

def get_psql_conn():
    try:
        conn = connect(
            dbname='music_db',
            user='abhinav',
            password='password',
            port='5432',
            cursor_factory=RealDictCursor
        )
        conn = conn.cursor()
        print('Connected to the database')
        return conn
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

psql_conn = get_psql_conn()
