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

