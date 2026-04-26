from connection import get_connection

def add_book():
    title = input("Zadaj názov knihy: ")
    author_id = input("Zadaj ID autora: ")
    genre_id = input("Zadaj ID žánru: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)",
        (title, author_id, genre_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Kniha bola pridaná.")


def delete_book():
    book_id = input("Zadaj ID knihy na vymazanie: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM books WHERE book_id = %s",
        (book_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Kniha bola vymazaná.")