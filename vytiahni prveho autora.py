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
cursor.execute('SELECT * FROM authors LIMIT 1')
prvy_autor = cursor.fetchall()

# Creating Autor objects from the retrieved data
autori_objects = [Autor(*autor) for autor in prvy_autor]

# Printing Autor objects
for autor in autori_objects:
    print(autor)

cursor.close()
conn.close()
