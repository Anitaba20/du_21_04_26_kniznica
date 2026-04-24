from database import get_connection

def add_genre():
    name = input("Zadaj názov žánru: ")
    description = input("Zadaj popis žánru: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO genres (name, description) VALUES (%s, %s)",
        (name, description)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Žáner bol pridaný.")