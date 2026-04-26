from connection import create_connection

def add_book():
    title = input("Zadaj názov knihy: ")
    author_id = input("Zadaj ID autora: ")
    genre_id = input("Zadaj ID žánru: ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE author_id = %s", (author_id,))
    if cursor.fetchone() is None:
        print("Autor neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("SELECT * FROM genres WHERE genre_id = %s", (genre_id,))
    if cursor.fetchone() is None:
        print("Žáner neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
    if cursor.fetchone() is not None:
        print("Kniha existuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)",
        (title, author_id, genre_id)
    )

    conn.commit()
    print("Kniha bola pridaná")
    cursor.close()
    conn.close()


def delete_book():
    book_id = input("Zadaj ID knihy na vymazanie: ")

    try:
        book_id = int(book_id)
    except:
        print("Zadaj číslo")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
    if cursor.fetchone() is None:
        print("Kniha neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    conn.commit()
    print("Kniha bola vymazaná")
    cursor.close()
    conn.close()

