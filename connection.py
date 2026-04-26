import psycopg2

def create_connection():
    return psycopg2.connect(
        host=a,
        database=b,
        user=c,
        password=d)

