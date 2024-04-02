class Zaner:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte nazov zanru: ")
        nazov = input()
        cursor.execute("INSERT INTO genres (name) VALUES (%s)", (nazov,))
        print("Zaner vlozeny do databazy.")


    def __str__(self):
        return f"---ZANER---\nID Zanru: {self.id}\nNazov: {self.name}"
