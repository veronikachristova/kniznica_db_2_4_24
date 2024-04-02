import psycopg2
from autor import Author
from zaner import Zaner
from kniha import Kniha

conn = psycopg2.connect(
    dbname='b4l1o2iguxktujhgmzv1',
    user='uhkelmgkhpkwcyjdl3qd',
    password='ZIuTMMFceJbOGxBmDJGxtBRfTrRVSs',
    host='b4l1o2iguxktujhgmzv1-postgresql.services.clever-cloud.com',
    port=50013
)

cursor = conn.cursor()

def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")

def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
            print("Pridat autora")
        elif choice == "2":
            Zaner.vloz_do_db(cursor)
            conn.commit()
            print("Pridat zaner")
        elif choice == "3":
            Kniha.vloz_do_db(cursor)  # Call the vloz_do_db method from Kniha class
            conn.commit()
            print("Pridat knihu")
        else:
            print("Neplatny vstup")

aplikacia()
