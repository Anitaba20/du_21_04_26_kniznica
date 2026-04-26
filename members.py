from connection import create_connection

def add_member():
    first_name = input("Zadaj meno: ")
    last_name = input("Zadaj priezvisko: ")
    email = input("Zadaj email: ")

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members WHERE email = %s", (email,))
    if cursor.fetchone() is not None:
        print("Člen s týmto emailom už existuje")
        cursor.close()
        conn.close()
        return

    cursor.execute(
        "INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)",
        (first_name, last_name, email)
    )

    conn.commit()
    print("Člen bol pridaný")
    cursor.close()
    conn.close()


def delete_member():
    member_id = input("Zadaj ID člena na vymazanie: ")

    try:
        member_id = int(member_id)
    except:
        print("Zadaj číslo")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
    if cursor.fetchone() is None:
        print("Člen neexistuje")
        cursor.close()
        conn.close()
        return

    cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
    conn.commit()
    print("Člen bol vymazaný")
    cursor.close()
    conn.close()