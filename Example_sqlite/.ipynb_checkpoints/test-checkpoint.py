# creating a new database and putting stuff in it. 

import sqlite3

# establish database

conn = sqlite3.connect("test.sqlite3")

curs = conn.cursor()

new_table = """
            CREATE TABLE test(
            name TEXT,
            age INT,
            grade Float,
            year DATE
            );
"""

# add table to database

curs.execute(new_table).fetchall()

data = """
        INSERT INTO test(name, age, grade, year)
        VALUES ("Kelli", 23, 1, 1980),
        ("Amin", 29, 2, 1960),
        ("Ping", 45, 4, 2008),
        ("Chris", 25, 6, 1920);
"""

curs.execute(data).fetchall()

curs.close()
conn.commit()

conn = sqlite3.connect("test.sqlite3")

curs = conn.cursor()
curs.execute("""SELECT * from test""").fetchall()

data2 = """
        INSERT INTO test(name, age)
        VALUES ("Evidence", 22),
        ("Destiny", 30)
"""

curs.execute(data2).fetchall()

curs.close()
conn.commit()

conn = sqlite3.connect("test.sqlite3")

curs = conn.cursor()
curs.execute("""SELECT * from test""").fetchall()

curs.execute("""
            SELECT 
            AVG(age)
            FROM test
            where grade >= 4.0""").fetchall()

data3 = """
        INSERT INTO test(grade, year)
        VALUES ("25", 2020)
"""
curs.execute(data3).fetchall()

curs.close()
conn.commit()
curs.execute("""SELECT * from test""").fetchall()
