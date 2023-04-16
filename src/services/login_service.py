from entities.user import User

from repositories.user_repository import UserRepository


class LoginService:
    def __init__(self, user_repository=UserRepository):
        self.user_repository = user_repository
        self.logged_in_user = None

    def validate_password(self, password):
        password = str(password)

        special_characters = set()
        include_special_char = False

        for i in range(33, 48):
            special_characters.add(chr(i))

        numbers = set()
        include_number = False

        for i in range(48, 58):
            numbers.add(chr(i))

        for i in password:
            if i in special_characters:
                include_special_char = True
            if i in numbers:
                include_number = True

        if len(password) >= 8 and include_number is True and include_special_char is True:
            return True

        raise Exception("Incorrect password format")

    def create_new_user(self, username, password):

        username = str(username)
        password = str(password)

        found = self.user_repository.find_user(username)

        if found is None:

            password_test = self.validate_password(password)

            if password_test is True:

                new_user = User(username, password)
                self.user_repository.add_user(new_user)

        else:
            raise Exception("User with this username exists already")

    def validate_credentials(self, username, password):
        found = self.user_repository.find_user(username)

        if found is not None and found["password"] == password:
            return True

        raise Exception("Invalid credentials")
        # return False instead and then do exception in login user?

    def login_user(self, username, password):
        valid = self.validate_credentials(username, password)

        if valid:
            self.logged_in_user = User(username, password)

        return self.logged_in_user

    def logout_user(self):
        self.logged_in_user = None
