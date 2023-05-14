from entities.user import User
from database_connection import connect_to_database


class UserRepository:
    """Class managing operations on user table in database
    """

    def __init__(self):
        """Class constructor
        """
        self._connection = connect_to_database()

    def add_user(self, user:User):
        """Adding a new user's information to database

        Args:
            user (User object): The User object contains the
            username and password of the user to be added to database
        """
        cursor = self._connection.cursor()

        cursor.execute("""
            insert into users (username, password) values (?, ?)""",
                       (user.username, user.password)
                       )

        self._connection.commit()

    def find_user(self, username):
        """Finds an existing user by username and returns their username
        and password, or returns None if the user does not exist

        Args:
            username (string): The username to be searched for

        Returns:
            Database row object with the user's username and password, or None
        """
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
        """Deletes a user from database

        Args:
            username (string): The username of the user to be deleted from database
        """
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
        """Deletes all users and thus all entries from database users table
        """
        cursor = self._connection.cursor()

        cursor.execute("""
        delete from users;
        """)

        self._connection.commit()

    def find_all_users(self):
        """Finds and returns all users in database users table

        Returns:
            List of users (database rows, each with username and password)
        """
        cursor = self._connection.cursor()

        cursor.execute("""
        select * from users
        """)

        found = cursor.fetchall()

        return found
