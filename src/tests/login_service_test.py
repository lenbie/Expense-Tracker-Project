import unittest
from services.login_service import LoginService
from entities.user import User
from repositories.user_repository import UserRepository


test_repository = UserRepository()


class TestLoginService(unittest.TestCase):

    def setUp(self):
        self.test_login_service = LoginService(test_repository)
        test_repository.delete_all_users()

    def test_validate_password(self):
        valid = self.test_login_service.validate_password("1234abc!")

        self.assertEqual(valid, True)

    def test_invalid_password_too_short(self):
        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_password("1a!")

        self.assertTrue("Incorrect password format" in str(context.exception))

    def test_invalid_password_no_number(self):
        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_password("abcdefg!")

        self.assertTrue("Incorrect password format" in str(context.exception))

    def test_invalid_password_no_special_char(self):
        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_password("abcdefg1")

        self.assertTrue("Incorrect password format" in str(context.exception))

    def test_create_user(self):
        self.test_login_service.create_new_user("mark", "1234abc!")

        found = test_repository.find_user("mark")

        self.assertEqual(found["username"], "mark")

    def test_create_user_already_exists(self):
        self.test_login_service.create_new_user("mark", "1234abc!")

        with self.assertRaises(Exception) as context:
            self.test_login_service.create_new_user("mark", "test123!")

        self.assertTrue(
            "User with this username exists already" in str(context.exception))

    def test_create_user_invalid_password(self):
        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_password("abcdefg1")

        self.assertTrue("Incorrect password format" in str(context.exception))

    def test_validate_credentials(self):
        self.test_login_service.create_new_user("mark", "1234abc!")

        valid = self.test_login_service.validate_credentials(
            "mark", "1234abc!")

        self.assertEqual(valid, True)

    def test_validate_credentials_user_doesnt_exist(self):
        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_credentials("mark", "1234abc!")

        self.assertTrue("Invalid credentials" in str(context.exception))

    def test_validate_credentials_wrong_password(self):
        self.test_login_service.create_new_user("mark", "1234abc!")

        with self.assertRaises(Exception) as context:
            self.test_login_service.validate_credentials("mark", "1234abc?")

        self.assertTrue("Invalid credentials" in str(context.exception))
