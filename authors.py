from connection import create_connection

def add_author():
    name = input("Zadaj meno autora: ")
    bio = input("Zadaj bio autora: ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE name = %s", (name,))
    if cursor.fetchone() is not None:
        print("Autor už existuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "INSERT INTO authors (name, bio) VALUES (%s, %s)",
        (name, bio)
    )

    conn.commit()
    print("Autor bol pridaný")
    cursor.close()
    conn.close()

def delete_author():
    author_id = input("Zadaj ID autora na vymazanie: ")

    try:
        author_id = int(author_id)
    except:
        print("Zadaj číslo")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE author_id = %s", (author_id,))
    if cursor.fetchone() is None:
        print("Autor neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("DELETE FROM authors WHERE author_id = %s", (author_id,))
    conn.commit()
    print("Autor bol vymazaný")
    cursor.close()
    conn.close()

