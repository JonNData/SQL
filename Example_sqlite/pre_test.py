# create new db and insert

import sqlite3

# establish db

conn = sqlite3.connect('slider.sqlite3')

curs = conn.cursor()

sick_table = """
    CREATE TABLE IF NOT EXISTS ollie_table(
        name TEXT,
        height INT,
        rating INT
    )
"""
# add table to DB

curs.execute(sick_table).fetchall()

put_me_in = """
    INSERT INTO ollie_table(name, height)
    VALUES
        ('Rhodie bird', 50),
        ('Tanzo Mancha', 210),
        ('Witherton Rauzghoul', 300)
"""
results= curs.execute("""Select * from ollie_table""").fetchall()
print(results)

# curs.execute(put_me_in).fetchall()
curs.close()
conn.commit()

