# sql-practice/chinook_queries.py

import os
import sqlite3

# DB_filepath = 'chinook.db'
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'chinook.db')

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = """
SELECT
    Country
    , count(distinct CustomerID) as customer_count
FROM customers
GROUP BY Country
ORDER BY customer_count DESC
LIMIT 5
"""

# result = cursor.execute(query)
# print("RESULT", result) # This returndscursor object w/o results(need fetch)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row))
    print(row)
    # print(row[0])
    # print(row[1])
    # breakpoint()
    print(row['Country'])
    print(row['customer_count'])
    print("-----")