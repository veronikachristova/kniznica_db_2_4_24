import psycopg2

class Autor:
    def __init__(self, author_id, name, bio):
        self.author_id = author_id
        self.name = name
        self.bio = bio

    def __str__(self):
        return f'ID: {self.author_id}\nName: {self.name}\nBio: {self.bio}\n'

volba_pouzivatela = int(input("Vyber zaner 1-3: "))
print(volba_pouzivatela)

if volba_pouzivatela == 1:
    zaner = "Fantasy"
elif volba_pouzivatela == 2:
    zaner = "Sci-fi"
elif volba_pouzivatela == 3:
    zaner = "Detektívka"

# Establishing connection to the database
conn = psycopg2.connect(
    dbname='bva2e94t1hjabargw4qm',
    user='uoxfcfn6z1ax4uvdhs8d',
    password='BqNof4FiTkz7VmAFcWYqzxjR5vMqRv',
    host='bva2e94t1hjabargw4qm-postgresql.services.clever-cloud.com',
    port='50013'
)

first_name = 'Patrik'
last_name = 'Dendis'
email = 'patrik@dendis.sk'


cursor = conn.cursor()
# cursor.execute("""
# INSERT INTO members (first_name, last_name, email)
# VALUES (%s, %s, %s)
# """, (first_name, last_name, email))
#
# conn.commit()
# print("Novy clen bol uspesne pridany")

#vlozime 3 knihy do db aj s autormi
books_data = [
    ("The Hobbit", 1, 1, "9780547928227", 1937),
    ("Dune", 2, 2, "9780441172719", 1965),
    ("1984", 3, 3, "9780451524935", 1949)
]

# Add the three books to the database
for book_data in books_data:
    cursor.execute("""
    INSERT INTO books (title, author_id, genre_id, isbn, publication_year)
    VALUES (%s, %s, %s, %s, %s)
    """, book_data)

print("book/s added")
cursor.close()
conn.close()
