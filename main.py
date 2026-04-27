from books import add_book, delete_book
from members import add_member, delete_member
from loans import loan_book, show_loans
from authors import add_author, delete_author
from genres import add_genre


while True:
    print("1 Pridať autora")
    print("2 Pridať žáner")
    print("3 Pridať knihu")
    print("4 Vymazať knihu")
    print("5 Požičať knihu")
    print("6 Zobraziť výpožičky")
    print("7 Pridať člena")
    print("8 Vymazať člena")
    print("9 Vymazať autora")
    print("10 Koniec")

    choice = input("\nMožnosť: ")

    if choice == "1":
        add_author()
    elif choice == "2":
        add_genre()
    elif choice == "3":
        add_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        loan_book()
    elif choice == "6":
        show_loans()  # alebo show_loans()
    elif choice == "7":
        add_member()
    elif choice == "8":
        delete_member()
    elif choice == "9":
        delete_author()
    elif choice == "10":
        print("Koniec")
        break

    else:
        print("Neplatná voľba")