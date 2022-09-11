import psycopg2
import psycopg2.extras
import os


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            port=5431,
                            database='blog',
                            user=os.getenv("PG_USER"),
                            password=os.getenv("PG_PASSWORD"),
                            )
    return conn
