from database_connection import connect_to_database


def create_users_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists users ( 
            username text primary key,
            password text
        );
    """)

    connection.commit()


def create_expenses_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists expenses (
            username text primary key,
            name text,
            amount real,
            date text,
            category text
        );
    """)

    connection.commit()


def drop_user_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    cursor = connection.cursor()


def drop_expenses_table(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists expenses;
    """)

    cursor = connection.cursor()


def initialize_database():

    connection = connect_to_database()

    drop_user_table(connection)
    drop_expenses_table(connection)

    create_users_table(connection)
    create_expenses_table(connection)


if __name__ == "__main__":
    initialize_database()
