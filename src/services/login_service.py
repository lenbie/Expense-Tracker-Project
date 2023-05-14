import string
from entities.user import User

from repositories.user_repository import UserRepository


class LoginService:
    """This class manages the login functionality of the application.
    This includes creating a new user account, and logging in to and out of an existing account. 
    """

    def __init__(self, user_repository=UserRepository):
        """Class constructor

        Args:
            user_repository (UserRepository object): Object with methods of UserRepository class,
                                                        handling database operations
        """
        self.user_repository = user_repository
        self.logged_in_user = None

    def _validate_password(self, password):
        """Checks that a chosen password is valid, i.e. is at least 8 characters long,
        and includes at least one number and one special character

        Args:
            password (str): The chosen password

        Raises:
            IncorrectPasswordFormatError: An error that occurs when the password
            does not meet the validity criteria

        Returns:
            True, if the password is valid
        """
        password = str(password)

        special_characters = list(string.punctuation)
        include_special_char = False

        numbers = list(string.digits)
        include_number = False

        for i in password:
            if i in special_characters:
                include_special_char = True
            if i in numbers:
                include_number = True

        if len(password) >= 8 and include_number is True and include_special_char is True:
            return True

        raise IncorrectPasswordFormatError("Incorrect password format")

    def create_new_user(self, username, password):
        """Creates a new user with username and password

        Args:
            username (str): The chosen username
            password (str): The chosen password

        Raises:
            UsernameNotUniqueError: An error that occurs when a user with
            the chosen username already exists in the database
        """

        username = str(username)
        password = str(password)

        found = self.user_repository.find_user(username)

        if found is None:

            password_test = self._validate_password(password)

            if password_test is True:

                new_user = User(username, password)
                self.user_repository.add_user(new_user)

        else:
            raise UsernameNotUniqueError(
                "User with this username exists already")

    def validate_credentials(self, username, password):
        """Checks whether the entered username exits and matches the entered password

        Args:
            username (str): The entered username
            password (str): The entered password

        Raises:
            InvalidCredentialsError: An error that occurs when the entered username does
            not exist or does not match the password

        Returns:
            True, if the username and password match
        """
        found = self.user_repository.find_user(username)

        if found is not None and found["password"] == password:
            return True

        raise InvalidCredentialsError("Invalid credentials")

    def login_user(self, username, password):
        """Logs in an existing user, after checking the validity of their username and password

        Args:
            username (str): The entered username
            password (str): The entered password

        Returns:
            A user object of the current logged-in user, or
            None if the entered credentials are invalid.
        """
        valid = self.validate_credentials(username, password)

        if valid:
            self.logged_in_user = User(username, password)

        return self.logged_in_user

    def find_logged_in_user(self):
        """Finds and returns which user is currently logged in

        Returns:
            The currently logged-in user as a User object, or None if no user is logged in.
        """
        return self.logged_in_user

    def logout_user(self):
        """Logs out the currently logged-in user
        """
        self.logged_in_user = None


class UsernameNotUniqueError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class IncorrectPasswordFormatError(Exception):
    pass


login_service = LoginService(UserRepository())
