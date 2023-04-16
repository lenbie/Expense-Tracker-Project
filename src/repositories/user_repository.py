from entities.user import User
from database_connection import connect_to_database


class UserRepository:
    def __init__(self):
        self._connection = connect_to_database()

    def add_user(self, user=User):

        cursor = self._connection.cursor()

        cursor.execute("""
            insert into users (username, password) values (?, ?)""",
                       (user.username, user.password)
                       )

        self._connection.commit()

    def find_user(self, username):

        cursor = self._connection.cursor()

        cursor.execute("""
            select
                username,
                password
            from
                users
            where
                username=:c""",
                       {"c": username}
                       )

        found = cursor.fetchone()

        return found

    def delete_user(self, username):

        cursor = self._connection.cursor()

        cursor.execute("""
            delete from
                users
            where
                username=:c""",
                       {"c": username}
                       )

        self._connection.commit()

    def delete_all_users(self):

        cursor = self._connection.cursor()

        cursor.execute("""
        delete from users;
        """)

        self._connection.commit()

    def find_all_users(self):

        cursor = self._connection.cursor()

        cursor.execute("""
        select * from users
        """)

        found = cursor.fetchall()

        return found
