import sqlite3

# connect and open the database file database.db
conn = sqlite3.connect('database.db')
print("Opened database successfully")

# use the opened connection to read all cards into a cursor
cursor = conn.execute("SELECT cardid, title from card")
# loop over all rows in the cursor and print the cardid and title column
for row in cursor:
    print("CARDID = ", row[0], "TITLE = ", row[1])

cursor = conn.execute("SELECT * from wish")
# loop over all rows in the cursor and print the cardid and title column
for row in cursor:
    print(row)

# close the connection
print("Operation done successfully")
conn.close()
