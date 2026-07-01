import psycopg2
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


if __name__ == "__main__":
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM phonebook;")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

        print("Connected successfully!")

    except Exception as error:
        print("Connection error:", error)