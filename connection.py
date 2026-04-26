import psycopg2

def get_connection():
    return psycopg2.connect(
        host="ep-old-sun-ala7ftma-pooler.c-3.eu-central-1.aws.neon.tech",
        database="neondb",
        user="neondb_owner",
        password="npg_I5zs0OAwrtVm")

