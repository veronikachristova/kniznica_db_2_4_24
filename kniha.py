class Kniha:
    def __init__(self, title, author_id, genre_id, isbn, publication_year, copies):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2], value[3], value[4], value[5])

    @staticmethod
    def get_id_by_name(cursor, table, name_column, name):
        cursor.execute(f"SELECT id FROM {table} WHERE {name_column} = %s", (name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte meno autora: ")
        author_name = input()
        author_id = Kniha.get_id_by_name(cursor, 'authors', 'name', author_name)
        if author_id is None:
            print("Autor nebol najdeny v databaze.")
            return

        print("Vlozte nazov zanru: ")
        genre_name = input()
        genre_id = Kniha.get_id_by_name(cursor, 'genres', 'name', genre_name)
        if genre_id is None:
            print("Zaner nebol najdeny v databaze.")
            return

        print("Vlozte nazov knihy: ")
        title = input()
        print("Vlozte ISBN: ")
        isbn = input()
        print("Vlozte rok publikacie: ")
        publication_year = input()
        print("Vlozte pocet kopií: ")
        copies = input()

        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn, publication_year, copies) VALUES (%s, %s, %s, %s, %s, %s)",
                       (title, author_id, genre_id, isbn, publication_year, copies))
        print("Kniha vlozena do databazy.")

    def __str__(self):
        return f"---KNIHA---\nTitul: {self.title}\nAutor ID: {self.author_id}\nZaner ID: {self.genre_id}\nISBN: {self.isbn}\nRok publikacie: {self.publication_year}\nPocet kopií: {self.copies}"
