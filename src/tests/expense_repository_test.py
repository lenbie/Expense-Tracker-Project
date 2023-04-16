import unittest
from repositories.expense_repository import ExpenseRepository
from entities.expense import Expense
from entities.user import User
from entities.category import Category

test_repository = ExpenseRepository()


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        test_repository.delete_all_expenses()
        self.test_user = User("alice", "1234abc!")
        self.test_expense = Expense("sushi", 12.5, "2023-04-15", "food")

    def test_add_expense(self):
        test_repository.add_expense(self.test_user, self.test_expense)

        found = test_repository.find_expense(self.test_user, self.test_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        test_expense_list = ["alice", "sushi", 12.5, "2023-04-15", "food"]
        self.assertEqual(found_expense, test_expense_list)

    def test_delete_expense(self):
        test_repository.add_expense(self.test_user, self.test_expense)

        test_repository.delete_expense(self.test_user, self.test_expense)

        found = test_repository.find_expense(self.test_user, self.test_expense)

        self.assertEqual(found, None)

    def test_find_expense_returns_false_if_not_added(self):
        found = test_repository.find_expense(self.test_user, self.test_expense)

        self.assertEqual(found, None)

    def test_find_expense_returns_correct_expense_amongst_similar(self):
        test_repository.add_expense(self.test_user, self.test_expense)
        similar_expense = Expense("sushi", 12.5, "2023-04-17", "food")
        test_repository.add_expense(self.test_user, similar_expense)

        found = test_repository.find_expense(self.test_user, similar_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        test_expense_list = ["alice", "sushi", 12.5, "2023-04-15", "food"]
        self.assertNotEqual(found_expense, test_expense_list)

    def test_delete_all_expenses(self):
        test_repository.delete_all_expenses()

        found = test_repository.get_all_expenses_in_table()

        self.assertEqual(len(found), 0)

    def test_get_all_expenses_in_table(self):
        test_repository.add_expense(self.test_user, self.test_expense)
        similar_expense = Expense("sushi", 12.5, "2023-04-17", "food")
        test_repository.add_expense(self.test_user, similar_expense)

        found = test_repository.get_all_expenses_in_table()

        self.assertEqual(len(found), 2)

    def test_get_all_expenses_by_user(self):
        test_repository.add_expense(self.test_user, self.test_expense)

        similar_expense = Expense("sushi", 12.5, "2023-04-17", "food")
        test_repository.add_expense(self.test_user, similar_expense)

        found = test_repository.get_all_expenses_by_user(self.test_user)

        self.assertEqual(len(found), 2)

    def test_get_all_expenses_by_category_and_user(self):
        test_repository.add_expense(self.test_user, self.test_expense)

        similar_expense = Expense("sushi", 12.5, "2023-04-17", "food")
        test_repository.add_expense(self.test_user, similar_expense)

        third_expense = Expense("dress", 55.6, "2023-03-28", "clothes")
        test_repository.add_expense(self.test_user, third_expense)

        test_category = Category("food")

        found = test_repository.get_all_expenses_by_category_and_user(
            self.test_user, test_category)

        self.assertEqual(len(found), 2)

    def test_get_all_expenses_by_category_and_user_category_does_not_exist(self):
        test_repository.add_expense(self.test_user, self.test_expense)

        test_category = Category("clothes")
        found = test_repository.get_all_expenses_by_category_and_user(
            self.test_user, test_category)

        self.assertEqual(found, [])
