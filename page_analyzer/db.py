import psycopg2


def get_db_connection(database_url):
    return psycopg2.connect(database_url)


def insert_url(url, conn):
    with conn:
        with conn.cursor() as cur:
            cur.execute("""insert into urls (name) values (%s);""", (url,))
