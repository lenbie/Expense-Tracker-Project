from tkinter import ttk, constants
from services.login_service import login_service
from repositories.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService


class ExpenseGraph:
    def __init__(self, root, expense_tracker_homescreen):
        self._root = root
        self._return_to_homescreen = expense_tracker_homescreen
        self._frame = None
        self._style = None

        self.user = login_service.find_logged_in_user()
        self.expense_service = ExpenseService(ExpenseRepository(), self.user)

        self._expense_name = None
        self._expense_amount = None
        self._expense_date = None
        self._expense_category = None
        self._selected_category = None

        self._initialize()

    def configure(self):
        self._frame.pack(fill=constants.X)
        self._root.configure(background="#AFE4DE")

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._table_frame = ttk.Frame(master=self._frame)
        self._frame.grid_columnconfigure(1, weight=1, minsize=200)

        self._style = ttk.Style()
        self._style.configure("TFrame", background="#AFE4DE")

        header_label = ttk.Label(
            master=self._frame, text="Expense Graph", background="#AFE4DE")
        return_to_homescreen = ttk.Button(
            master=self._frame, text="Return to Expense Tracker Homescreen", command=self._return_to_homescreen)

        return_to_homescreen.grid(row=0, column=3, sticky=(
            constants.E), padx=5, pady=5)
        header_label.grid(row=0, columnspan=2, sticky=(
            constants.N), padx=5, pady=5)
