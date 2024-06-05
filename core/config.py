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