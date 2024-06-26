import psycopg2


# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query3 - select only "Queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query4 - select only by the "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# Query5 - select only the albums with "artist_id" #51 on the "Album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

#Q Query6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])


# Fetch the results (multiple)
# results = cursor.fetchall()

# Fetch the result (single)
results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)