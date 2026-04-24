from database import get_connection

def add_member():
    first_name = input("Zadaj meno člena: ")
    last_name = input("Zadaj priezvisko člena: ")
    email = input("Zadaj email člena: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)",
        (first_name, last_name, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Člen bol pridaný.")


def delete_member():
    member_id = input("Zadaj ID člena na vymazanie: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM members WHERE member_id = %s",
        (member_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Člen bol vymazaný.")