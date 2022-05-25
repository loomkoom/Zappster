# import the sqlite3 library to work with SQLite databases in Python
import sqlite3

# connect and open the database file database.db, the database will be created when it does not exists
conn = sqlite3.connect('database.db')
print("Opened database successfully")

# drop table if exists:
conn.execute('DROP TABLE IF EXISTS card;')
conn.execute('DROP TABLE IF EXISTS wish;')

# create a new table card with two columns:
# cardid - title
conn.execute('CREATE TABLE card (cardid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT)')
print("Table card created successfully")

# insert four rows in the newly created table
conn.execute("INSERT INTO card (title) VALUES ('Greetings')")
conn.execute("INSERT INTO card (title) VALUES ('Happy valentine''s day')")
conn.execute("INSERT INTO card (title) VALUES ('Happy Birthday')")
conn.execute("INSERT INTO card (title) VALUES ('Happy Birthday')")
conn.execute("INSERT INTO card (title) VALUES ('Happy Birthday')")
conn.execute("INSERT INTO card (title) VALUES ('I love you')")
conn.execute("INSERT INTO card (title) VALUES ('Happy Birthday')")
conn.execute("INSERT INTO card (title) VALUES ('Merry Christmas')")
conn.execute("INSERT INTO card (title) VALUES ('Congratulations')")
print("Cards inserted successfully")

# create a second table wish:
# wishid - uid - sender - message - cardid
conn.execute('CREATE TABLE wish (wishid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,uid TEXT, sender TEXT, message TEXT, cardid INTEGER)')
# there are no wishes already sent, so the table stays empty
print("Table wish created successfully")

# commit all changes to the database, otherwise they will be lost
conn.commit()

# close the connection
conn.close()
