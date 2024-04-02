import psycopg2

class Autor:
    def __init__(self, author_id, name, bio):
        self.author_id = author_id
        self.name = name
        self.bio = bio

    def __str__(self):
        return f'ID: {self.author_id}\nName: {self.name}\nBio: {self.bio}\n'

# Establishing connection to the database
conn = psycopg2.connect(
    dbname='bva2e94t1hjabargw4qm',
    user='uoxfcfn6z1ax4uvdhs8d',
    password='BqNof4FiTkz7VmAFcWYqzxjR5vMqRv',
    host='bva2e94t1hjabargw4qm-postgresql.services.clever-cloud.com',
    port='50013'
)

cursor = conn.cursor()

# Fetching data from the database
cursor.execute('SELECT * FROM authors')
autori = cursor.fetchall()

# Creating Autor objects from the retrieved data
autori_objects = [Autor(*autor) for autor in autori]

# Printing Autor objects
for autor in autori_objects:
    print(autor)

number_of_ids = len(list(map(lambda autor: autor.author_id, autori_objects)))
print("Number of IDs:", number_of_ids)

#parametrizovany vyber
# cursor.execute('SELECT * FROM books WHERE publication_year > %s AND publication_year < %s', (1900, 1950))
# knihy = cursor.fetchall()
# print(knihy)

#nazvy knih zo zanru Fantasy

cursor.execute('SELECT b.title FROM books b JOIN genres g ON g.genre_id = b.genre_id WHERE g.name = %s', ('Fantasy',))
fantasy = cursor.fetchall()
print(fantasy)

cursor.close()
conn.close()