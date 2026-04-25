from database import get_connection

def add_author():
    name = input("Zadaj meno autora: ")
    bio = input("Zadaj bio autora: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO authors (name, bio) VALUES (%s, %s)",
        (name, bio)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Autor bol pridaný.")

