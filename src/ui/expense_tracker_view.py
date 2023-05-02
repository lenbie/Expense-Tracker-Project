from tkinter import ttk, constants
from services.login_service import login_service
from repositories.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService


class ExpenseTrackerView:
    """This class manages the Home view of the Expense Tracker, which is displayed
    after a user logs in, and from which a user can navigatev to other parts of the Expense Tracker
    """

    def __init__(self, root, handle_login, expense_overview, expense_creation):
        """Class constructor, creates the 'expense tracker' view

        Args:
            root (Tkinter frame): The Tkinter frame within which the login view resides
            handle_login: Callable value, called when the user logs out and returns to login view
            expense_overview: Callable value, called when the user clicks the "View and Edit Expenses" button
            expense_creation: Callable value, called when the user clicks the "Create Expenses" button
        """
        self._root = root
        self._handle_return_to_login = handle_login
        self._handle_expense_overview = expense_overview
        self._handle_create_expense = expense_creation

        self._frame = None
        self._style = None

        self.user = login_service.find_logged_in_user()
        self.expense_service = ExpenseService(ExpenseRepository(), self.user)

        self._expense_name = None
        self._expense_amount = None
        self._expense_date = None
        self._expense_category = None
        self._selected_category = None
        self._selected_table_category = None
        self._expense_table = None
        self._selected_editable = None
        self._user_change = None

        self._initialize()

    def configure(self):
        """Shows the expense tracker view
        """
        self._frame.pack(fill=constants.X)
        self._root.configure(background="#AFE4DE")

    def destroy(self):
        """Destroys the expense tracker view
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1, minsize=200)

        self._style = ttk.Style()
        self._style.configure("TFrame", background="#AFE4DE")

        self._initialize_start_view()

    def _handle_logout(self):
        login_service.logout_user()
        self._handle_return_to_login()

    def _initialize_start_view(self):
        header_label = ttk.Label(
            master=self._frame, text="Welcome to your Expense Tracker", background="#AFE4DE")
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_logout)

        expense_overview_button = ttk.Button(
            master=self._frame, text="View and Edit Expenses", command=self._handle_expense_overview)
        create_expenses_button = ttk.Button(
            master=self._frame, text="Create Expenses", command=self._handle_create_expense)

        logout_button.grid(row=0, column=3, sticky=(
            constants.E), padx=5, pady=5)
        header_label.grid(row=0, columnspan=2, sticky=(
            constants.N), padx=5, pady=5)
        expense_overview_button.grid(row=1, column=0, padx=5, pady=5)
        create_expenses_button.grid(row=2, column=0, padx=5, pady=5)
