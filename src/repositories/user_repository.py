from entities.user import User
from database_connection import connect_to_database

class UserRepository:
    def __init__(self):
        self.connection=connect_to_database()

    def add_user(self, user=User()):
        
        cursor=self.connection.cursor()

        cursor.execute("""
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        """) #add somewhere else that this only works if username not present

        self.connection.commit()

    def find_user(self, username):

        cursor=self.connection.cursor()

        found= cursor.execute("""
            select
                username,
                password
            from
                users
            where
                username
            like
                "username";
        """)

        self.connection.commit()
    
        return found
    

 
