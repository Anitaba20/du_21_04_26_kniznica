from books import add_book, delete_book
from members import add_member, delete_member
from loans import loan_book, show_loans_by_member
from authors import add_author
from genres import add_genre


while True:
    print("1 Pridať knihu")
    print("2 Vymazať knihu")
    print("3 Pridať člena")
    print("4 Vymazať člena")
    print("5 Požičať knihu")
    print("6 Zobraziť výpožičky člena")
    print("7 Pridať autora")
    print("8 Pridať žáner")
    print("9 Koniec")

    choice = input("Vyber možnosť: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        add_member()
    elif choice == "4":
        delete_member()
    elif choice == "5":
        loan_book()
    elif choice == "6":
        show_loans_by_member()
    elif choice == "7":
        add_author()
    elif choice == "8":
        add_genre()
    elif choice == "9":
        print("Koniec")
        break
    else:
        print("Neplatná voľba")