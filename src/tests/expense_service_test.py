import unittest
from services.expense_service import ExpenseService
from entities.expense import Expense
from entities.user import User
from entities.category import Category
from repositories.expense_repository import ExpenseRepository
from datetime import date

test_repository = ExpenseRepository()
test_user = User("alice", "1234abcd!")


class TestExpenseService(unittest.TestCase):
    def setUp(self):
        self.test_expense_service = ExpenseService(test_repository, test_user)
        test_repository.delete_all_expenses()
        self.test_expense = Expense("sushi", 12.5, "2023-04-15", "food")

    def test_create_new_expense_all_details_given(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        expense_entry = [test_user.username, self.test_expense.name,
                         self.test_expense.amount, self.test_expense.date, self.test_expense.category]

        found = test_repository.find_expense(test_user, self.test_expense)
        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(expense_entry, found_expense)

    def test_create_new_expense_only_mandatory_details_given(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount)

        current_date = str(date.today())
        created_expense = Expense(
            self.test_expense.name, self.test_expense.amount, current_date, "undefined")
        created_expense_entry = [test_user.username, self.test_expense.name,
                                 self.test_expense.amount, current_date, "undefined"]

        found = test_repository.find_expense(test_user, created_expense)
        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(created_expense_entry, found_expense)

    def test_edit_expense_name_changes_if_exists(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        new_expense_name = "sushi takeaway"
        self.test_expense_service.edit_expense_name(
            new_expense_name, self.test_expense)

        new_expense = Expense(new_expense_name, self.test_expense.amount,
                              self.test_expense.date, self.test_expense.category)
        found = test_repository.find_expense(test_user, new_expense)

        self.assertNotEqual(self.test_expense.name, found["name"])

    def test_edit_expense_name_creates_new_expense_if_exists(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        new_expense_name = "sushi takeaway"
        self.test_expense_service.edit_expense_name(
            new_expense_name, self.test_expense)
        expected_expense_entry = [test_user.username, new_expense_name,
                                  self.test_expense.amount, self.test_expense.date, self.test_expense.category]

        new_expense = Expense(new_expense_name, self.test_expense.amount,
                              self.test_expense.date, self.test_expense.category)
        found = test_repository.find_expense(test_user, new_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(expected_expense_entry, found_expense)

    def test_edit_expense_name_returns_False_if_not_exists(self):
        new_expense_name = "sushi takeaway"
        edit = self.test_expense_service.edit_expense_name(
            new_expense_name, self.test_expense)

        self.assertEqual(edit, False)

    def test_edit_expense_amount_makes_correct_changes(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        new_expense_amount = "20.2"
        self.test_expense_service.edit_expense_amount(
            new_expense_amount, self.test_expense)
        expected_expense_entry = [test_user.username, self.test_expense.name, float(
            new_expense_amount), self.test_expense.date, self.test_expense.category]

        new_expense = Expense(self.test_expense.name, new_expense_amount,
                              self.test_expense.date, self.test_expense.category)
        found = test_repository.find_expense(test_user, new_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(expected_expense_entry, found_expense)

    def test_edit_expense_amount_returns_False_if_not_exists(self):
        new_expense_amount = 20.2
        edit = self.test_expense_service.edit_expense_amount(
            new_expense_amount, self.test_expense)

        self.assertEqual(edit, False)

    def test_edit_expense_category_makes_correct_changes(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        new_expense_category = "restaurants"
        self.test_expense_service.edit_expense_category(
            new_expense_category, self.test_expense)

        expected_expense_entry = [test_user.username, self.test_expense.name,
                                  self.test_expense.amount, self.test_expense.date, new_expense_category]
        new_expense = Expense(self.test_expense.name, self.test_expense.amount,
                              self.test_expense.date, new_expense_category)
        found = test_repository.find_expense(test_user, new_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(expected_expense_entry, found_expense)

    def test_edit_expense_category_returns_False_if_not_exists(self):
        new_expense_category = "restaurants"
        edit = self.test_expense_service.edit_expense_category(
            new_expense_category, self.test_expense)

        self.assertEqual(edit, False)

    def test_edit_expense_date_makes_correct_changes(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        new_expense_date = "2022-03-28"
        self.test_expense_service.edit_expense_date(
            new_expense_date, self.test_expense)

        new_expense = Expense(self.test_expense.name, self.test_expense.amount,
                              new_expense_date, self.test_expense.category)
        expected_expense_entry = [test_user.username, self.test_expense.name,
                                  self.test_expense.amount, new_expense_date, self.test_expense.category]

        found = test_repository.find_expense(test_user, new_expense)

        if found:
            found_expense = [found["username"], found["name"],
                             found["amount"], found["date"], found["category"]]

        self.assertEqual(expected_expense_entry, found_expense)

    def test_edit_expense_date_returns_False_if_not_exists(self):
        new_expense_date = "2022-03-28"
        edit = self.test_expense_service.edit_expense_date(
            new_expense_date, self.test_expense)

        self.assertEqual(edit, False)

    def test_delete_expense_functions(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.delete_expense(self.test_expense)

        found = test_repository.find_expense(test_user, self.test_expense)

        self.assertEqual(found, None)

    def test_delete_expense_returns_False_if_not_exists(self):
        deletion = self.test_expense_service.delete_expense(self.test_expense)
        self.assertEqual(deletion, False)

    def test_delete_category_old_category_no_longer_exists(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, self.test_expense.category)

        test_category = Category(self.test_expense.category)
        self.test_expense_service.delete_category(test_category)

        found = test_repository.get_all_expenses_by_category_and_user(
            test_user, test_category)

        self.assertEqual(found, [])

    def test_delete_category_old_category_expenses_in_undefined(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        test_category = Category(self.test_expense.category)
        self.test_expense_service.delete_category(test_category)

        undefined_category = Category("undefined")
        found = test_repository.get_all_expenses_by_category_and_user(
            test_user, undefined_category)

        self.assertEqual(found[0]["category"], "undefined")

    def test_delete_category_returns_False_if_not_exists(self):
        test_category = Category(self.test_expense.category)
        deletion = self.test_expense_service.delete_category(test_category)
        self.assertEqual(deletion, False)

    def test_rename_category_old_category_no_longer_exists(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, self.test_expense.category)

        test_category = Category(self.test_expense.category)
        new_category_name = "restaurant"
        self.test_expense_service.rename_category(
            new_category_name, test_category)

        found = test_repository.get_all_expenses_by_category_and_user(
            test_user, test_category)

        self.assertEqual(found, [])

    def test_rename_category_old_category_expenses_in_undefined(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)

        test_category = Category(self.test_expense.category)
        new_category = Category("restaurant")
        self.test_expense_service.rename_category(
            new_category.name, test_category)

        found = test_repository.get_all_expenses_by_category_and_user(
            test_user, new_category)

        self.assertEqual(found[0]["category"], "restaurant")

    def test_rename_category_returns_False_if_not_exists(self):
        test_category = Category(self.test_expense.category)
        new_category = Category("restaurant")
        renamed = self.test_expense_service.rename_category(
            new_category.name, test_category)
        self.assertEqual(renamed, False)

    def test_get_total_all_expenses_by_user(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, self.test_expense.category)

        expected_total = self.test_expense.amount + 15.6
        returned_total = self.test_expense_service.get_total_all_expenses_by_user()

        self.assertEqual(expected_total, returned_total)

    def test_get_total_by_category_and_user(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, self.test_expense.category)

        expected_total = self.test_expense.amount + 15.6
        returned_total = self.test_expense_service.get_total_by_category_and_user(
            Category(self.test_expense.category))

        self.assertEqual(expected_total, returned_total)

    def test_list_all_expenses(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        list_of_expenses = self.test_expense_service.list_all_expenses()

        self.assertEqual(len(list_of_expenses), 1)

    def test_list_expenses_by_category(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, "takeaway")

        list_of_expenses = self.test_expense_service.list_expenses_by_category(
            Category(self.test_expense.category))

        self.assertEqual(len(list_of_expenses), 1)

    def test_list_all_categories(self):
        self.test_expense_service.create_new_expense(
            self.test_expense.name, self.test_expense.amount, self.test_expense.date, self.test_expense.category)
        self.test_expense_service.create_new_expense(
            "pizza", 15.6, self.test_expense.date, "takeaway")

        list_of_categories = self.test_expense_service.list_all_categories()
        expected_list = {self.test_expense.category, "takeaway"}

        self.assertEqual(list_of_categories, expected_list)
