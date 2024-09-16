import psycopg2
from psycopg2 import OperationalError

config = {
    'user': 'postgres',
    'password': 'P@ss1234',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres'
}

def get_connection():
    try:
        conn = psycopg2.connect(**config)
        return conn
    except OperationalError as err:
        print(f"Erro de PostgreSQL: {err}")
        return None
