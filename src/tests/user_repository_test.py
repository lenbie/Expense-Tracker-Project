import unittest
from repositories.user_repository import UserRepository
from entities.user import User

test_repository = UserRepository()


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        test_repository.delete_all_users()
        self.test_user = User("mark", "1234abc!")

    def test_add_user(self):
        test_repository.add_user(self.test_user)

        found = test_repository.find_user(self.test_user.username)

        self.assertEqual(found["username"], self.test_user.username)

    def test_find_user_if_added_correct_username(self):
        test_repository.add_user(self.test_user)

        found = test_repository.find_user(self.test_user.username)

        self.assertEqual(found["username"], self.test_user.username)

    def test_find_user_if_added_correct_password(self):
        test_repository.add_user(self.test_user)

        found = test_repository.find_user(self.test_user.username)

        self.assertEqual(found["password"], self.test_user.password)

    def test_find_user_returns_None_if_not_added(self):
        found = test_repository.find_user(self.test_user.username)

        self.assertEqual(found, None)

    def test_delete_all_users(self):
        test_repository.delete_all_users()

        found = test_repository.find_all_users()

        self.assertEqual(len(found), 0)

    def test_find_all_users_finds_correct_amount(self):
        test_repository.add_user(self.test_user)
        another_user = User("another", "test1234!")
        test_repository.add_user(another_user)

        found = test_repository.find_all_users()

        self.assertEqual(len(found), 2)

    def test_delete_user(self):
        test_repository.add_user(self.test_user)

        test_repository.delete_user("mark")

        found = test_repository.find_user("mark")

        self.assertEqual(found, None)
