from connection import create_connection

def add_genre():
    name = input("Zadaj názov žánru: ")
    description = input("Zadaj popis žánru: ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genres WHERE name = %s", (name,))
    if cursor.fetchone() is not None:
        print("Žáner už existuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "INSERT INTO genres (name, description) VALUES (%s, %s)",
        (name, description)
    )

    conn.commit()
    print("Žáner bol pridaný")
    cursor.close()
    conn.close()