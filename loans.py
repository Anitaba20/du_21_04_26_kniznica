from connection import create_connection
from datetime import date

def loan_book():
    book_id = input("Zadaj ID knihy: ")
    member_id = input("Zadaj ID člena: ")

    try:
        book_id = int(book_id)
        member_id = int(member_id)
    except:
        print("Zadaj čísla")
        return

    loan_date = date.today()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
    if cursor.fetchone() is None:
        print("Kniha neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
    if cursor.fetchone() is None:
        print("Člen neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "INSERT INTO loans (book_id, member_id, loan_date) VALUES (%s, %s, %s)",
        (book_id, member_id, loan_date)
    )

    conn.commit()
    print("Kniha bola požičaná")
    cursor.close()
    conn.close()


def show_loans():
    member_id = input("Zadaj ID člena: ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
    if cursor.fetchone() is None:
        print("Člen neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "SELECT books.title, loans.loan_date, loans.return_date "
        "FROM loans JOIN books ON loans.book_id = books.book_id "
        "WHERE loans.member_id = %s",
        (member_id,)
    )

    results = cursor.fetchall()

    if not results:
        print("Žiadne výpožičky")
    else:
        for item in results:
            print(item)
    cursor.close()
    conn.close()