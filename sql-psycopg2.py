import psycopg2 

# connect to 'chinook' database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the datbase

cursor = connection.cursor()

# Query1 - select all record from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')
# Query2 - select only Name record from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query4 - select only by "AristId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query5 - select only by "AristId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query6 - select only by "composer" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query7 - select only by "composer"  from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# Query8 - select only by "composer" from the "Track" table TEST
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# fetch the results(multiple)
results = cursor.fetchall()

# fetch result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(results)

