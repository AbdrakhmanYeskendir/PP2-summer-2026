import psycopg2
from config import load_config
import csv


def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)

        print("PhoneBook table created successfully!")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while creating table:", error)


def insert_contact(username, phone):
    sql = """
    INSERT INTO phonebook (username, phone)
    VALUES (%s, %s)
    ON CONFLICT (phone) DO NOTHING;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, phone))

                if cur.rowcount > 0:
                    print("Contact inserted successfully!")
                else:
                    print("Contact with this phone already exists.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while inserting contact:", error)


def update_username(old_username, new_username):
    sql = """
    UPDATE phonebook
    SET username = %s
    WHERE username = %s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_username, old_username))

                if cur.rowcount > 0:
                    print("Username updated successfully!")
                else:
                    print("No contact found with this username!")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while updating username:", error)


def update_phone(username, new_phone):
    sql = """
    UPDATE phonebook
    SET phone = %s
    WHERE username = %s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, username))

                if cur.rowcount > 0:
                    print("Phone updated successfully.")
                else:
                    print("No contact found with this username.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while updating phone:", error)


def show_all_contacts():
    sql = """
    SELECT id, username, phone
    FROM phonebook
    ORDER BY id;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while showing contacts:", error)


def search_by_name(name):
    sql = """
    SELECT id, username, phone
    FROM phonebook
    WHERE username ILIKE %s
    ORDER BY id;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{name}%",))
                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found with this name.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while searching by name:", error)


def search_by_phone_prefix(prefix):
    sql = """
    SELECT id, username, phone
    FROM phonebook
    WHERE phone LIKE %s
    ORDER BY id;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f"{prefix}%",))
                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found with this phone prefix.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while searching by phone prefix:", error)


def delete_by_username(username):
    sql = """
    DELETE FROM phonebook
    WHERE username = %s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username,))

                if cur.rowcount > 0:
                    print("Contact deleted successfully by username.")
                else:
                    print("No contact found with this username.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while deleting by username:", error)


def delete_by_phone(phone):
    sql = """
    DELETE FROM phonebook
    WHERE phone = %s;
    """

    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone,))

                if cur.rowcount > 0:
                    print("Contact deleted successfully by phone.")
                else:
                    print("No contact found with this phone.")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while deleting by phone:", error)


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    insert_contact(username, phone) 


def insert_from_csv(filename="contacts.csv"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["username"]
                phone = row["phone"]

                insert_contact(username, phone)

        print("Contacts imported from CSV successfully.")

    except FileNotFoundError:
        print("CSV file not found.")

    except KeyError:
        print("CSV file must contain username and phone columns.")

    except Exception as error:
        print("Error while importing from CSV:", error)


def main_menu():
    create_table()

    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update username")
        print("7. Update phone")
        print("8. Delete by username")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console()

        elif choice == "2":
            insert_from_csv()

        elif choice == "3":
            show_all_contacts()

        elif choice == "4":
            name = input("Enter name to search: ")
            search_by_name(name)

        elif choice == "5":
            prefix = input("Enter phone prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == "6":
            old_username = input("Enter current username: ")
            new_username = input("Enter new username: ")
            update_username(old_username, new_username)

        elif choice == "7":
            username = input("Enter username: ")
            new_phone = input("Enter new phone: ")
            update_phone(username, new_phone)

        elif choice == "8":
            username = input("Enter username to delete: ")
            delete_by_username(username)

        elif choice == "9":
            phone = input("Enter phone to delete: ")
            delete_by_phone(phone)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()
