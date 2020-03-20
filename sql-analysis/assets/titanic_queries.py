# titanic_queries.py


import os
import sqlite3
import pandas as pd 
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# read in
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')

df = pd.read_csv(DB_FILEPATH)


load_dotenv() # look in the .env file for env vars, and add them to the env
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)
#
# TABLE CREATION
#
query = """
CREATE TABLE IF NOT EXISTS titanic_table (
  Survived int,
  Pclass int,
  Name varchar(255),
  Sex varchar(255),
  Age int,
  Siblings_or_Spouses varchar(255),
  Parents_Children varchar(255),
  Fare float)
"""
cursor.execute(query)
cursor.execute("SELECT * from titanic_table")
result = cursor.fetchall()
print("RESULT:", result)

connection.commit()