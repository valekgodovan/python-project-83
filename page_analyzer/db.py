import psycopg2


def get_db_connection(database_url):
    return psycopg2.connect(database_url)


def insert_url(url, conn):
    with conn.cursor() as cur:
        cur.execute("""insert into urls (name) values (%s);""", (url,))


def is_url_in_db(url, conn):
    with conn.cursor() as cur:
        cur.execute("""select name from urls;""")
        urls_in_db = cur.fetchall()
    return (url,) in urls_in_db


def get_row_from_name_db(url, conn):
    with conn.cursor() as cur:
        cur.execute("""
        select * from urls
        where name = (%s);
        """, (url,))
        [(id, name, date)] = cur.fetchall()
        return id, name, date


def get_row_from_id_db(id, conn):
    with conn.cursor() as cur:
        cur.execute("""
        select * from urls
        where id = (%s);
        """, (id,))
        [(id, name, date)] = cur.fetchall()
        return id, name, date
