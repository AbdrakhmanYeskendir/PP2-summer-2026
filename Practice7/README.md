# Practice 7

## Description

This practice is a Python and PostgreSQL PhoneBook application.

The goal of this assignment is to learn how to connect Python to a PostgreSQL database using `psycopg2` and perform basic database operations such as creating tables, inserting data, querying data, updating records, deleting records, and importing data from a CSV file.

## Topics Covered

* PostgreSQL
* Python and PostgreSQL connection
* `psycopg2`
* Configuration file with `database.ini`
* Reading database configuration with `configparser`
* Creating tables
* Inserting rows
* Importing data from CSV
* Querying data with filters
* Updating existing records
* Deleting records
* Transactions with `commit`
* Error handling with `try / except`

## Folder Structure

```text
Practice7/
├── config.py
├── connect.py
├── phonebook.py
├── contacts.csv
├── database.ini
└── README.md
```

> Note: `database.ini` contains local database credentials and should not be pushed to GitHub.

## Database Table

The application uses a table called `phonebook`.

```sql
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);
```

## Files Description

### `database.ini`

Stores PostgreSQL connection settings:

```ini
[postgresql]
host=localhost
port=5432
database=phonebook_db
user=postgres
password=your_password_here
```

### `config.py`

Reads the database configuration from `database.ini` using `ConfigParser`.

### `connect.py`

Tests the connection to the PostgreSQL database.

### `contacts.csv`

Contains sample contacts for CSV import.

Example:

```csv
username,phone
Aruzhan,87010000001
Miras,87010000002
Dana,87010000003
```

### `phonebook.py`

Main PhoneBook application.

It supports:

* Creating the `phonebook` table
* Inserting a contact from console input
* Importing contacts from CSV
* Showing all contacts
* Searching contacts by name
* Searching contacts by phone prefix
* Updating username
* Updating phone number
* Deleting contact by username
* Deleting contact by phone number

## How to Run

Go to the `Practice7` folder:

```bash
cd Practice7
```

Test the database connection:

```bash
py connect.py
```

Run the PhoneBook application:

```bash
py phonebook.py
```

## Menu Options

```text
1. Insert contact from console
2. Insert contacts from CSV
3. Show all contacts
4. Search by name
5. Search by phone prefix
6. Update username
7. Update phone
8. Delete by username
9. Delete by phone
0. Exit
```

## Important Notes

* SQL queries use `%s` placeholders instead of f-strings for safer parameter passing.
* `commit()` is needed after insert, update, and delete operations.
* `rollback()` can be used when an error happens during a transaction.
* `phone` is marked as `UNIQUE`, so the same phone number cannot be inserted twice.
* `ILIKE` is used for case-insensitive name search.
* `LIKE` is used for phone prefix search.

## Result

This practice demonstrates how to build a simple console-based PhoneBook application using Python and PostgreSQL.
