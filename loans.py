from database import get_connection

def loan_book():
    book_id = input("Zadaj ID knihy: ")
    member_id = input("Zadaj ID člena: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO loans (book_id, member_id, loan_date) VALUES (%s, %s, CURRENT_DATE)",
        (book_id, member_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Kniha bola požičaná.")


def show_loans_by_member():
    member_id = input("Zadaj ID člena: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT books.title, loans.loan_date, loans.return_date
        FROM loans
        JOIN books ON loans.book_id = books.book_id
        WHERE loans.member_id = %s
        """,
        (member_id,)
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()