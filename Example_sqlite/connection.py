import sqlite3

# connecting to an existing database

# function to connect to database, 
# establish a cursor
# execute sql command
# fetch the result
# commit and close the connection
# return the result
def run(x, db="chinook.db"):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

# table pragma

pragma = """PRAGMA table_info(customers);"""

run(pragma)

# seeing all tables in database

join = """
        SELECT * 
        FROM tracks
        JOIN albums on tracks.Albumid = albums.Albumid 
        JOIN artists on albums.Artistid = artists.Artistid Limit 10
"""

run(join)

composer_price = """
        SELECT ROUND(AVG(UnitPrice), 2), Composer
        FROM tracks
        GROUP BY 2 
        ORDER by UnitPrice Desc
        Limit 10
"""

run(composer_price)

composer_price_artist = """
        SELECT ROUND(AVG(UnitPrice), 2) as "Average Price", t.Composer, a.name, al.Title
        FROM tracks as t
        JOIN albums as al on t.Albumid = al.Albumid 
        JOIN artists as a on al.Artistid = a.Artistid
        GROUP BY 2 
        ORDER by UnitPrice Desc
        Limit 10
"""

run(composer_price_artist)
