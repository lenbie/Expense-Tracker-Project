class User:
    """
    Class representing a user of the application

    Attributes:
        username (string): The user's unique username
        password (string): The user's password

    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
