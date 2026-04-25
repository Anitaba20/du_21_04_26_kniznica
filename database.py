import psycopg2

def get_connection():
    return psycopg2.connect(
        host=a,
        database=b,
        user=c,
        password=d
    )

