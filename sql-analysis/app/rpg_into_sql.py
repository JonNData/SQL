import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import sqlite3

# open up a connector, get cursor, execute query on cursor
# diff between elephant and sqlite3 is must specify user pw db
db_filepath = os.path.join(os.path.dirname(__file__), '..', 'assets', 'rpg_db.sqlite3')

sqlite_conn = sqlite3.connect(db_filepath)

sqlite_curs = sqlite_conn.cursor()

# Open the connection to the postgres DB
load_dotenv()  # scan for env file and vars
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

elephant_conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

ele_cursor = elephant_conn.cursor()

# query for character table and store as result to create table in elephantsql

char_query = "SELECT * FROM charactercreator_character"

char_result = sqlite_curs.execute(char_query).fetchall()

# Create table in elephantSQL to fit the right data

char_table = """
    CREATE TABLE IF NOT EXISTS charactercreator_character (
        character_id smallint PRIMARY KEY,
        name text,
        level smallint,
        exp int,
        hp int,
        strength int,
        intelligence int,
        dexterity int,
        wisdom int
        
    );
    """
ele_cursor.execute(char_table)

# Insert char table into elephantSQL
char_insert_query = """
    INSERT INTO charactercreator_character
    VALUES %s
    ON CONFLICT DO NOTHING
    """
execute_values(ele_cursor, char_insert_query, char_result)

elephant_conn.commit()

# so happy :)