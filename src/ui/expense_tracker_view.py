from tkinter import ttk, constants, OptionMenu, StringVar, messagebox, Entry, END
from services.login_service import login_service
from repositories.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService, InvalidInputError


class ExpenseTrackerView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_return_to_login = handle_login
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
        self._frame.grid_columnconfigure(1, weight=1, minsize=200)

        self._style = ttk.Style()
        self._style.configure("TFrame", background="#AFE4DE")

        self._initialize_start_view()
        self._initialize_create_expense_view()
        self._initialize_view_expense_total()
        self._initialize_view_expense_table()

    def _initialize_start_view(self):
        header_label = ttk.Label(
            master=self._frame, text="Your Expense Tracker", background="#AFE4DE")

        # create_expense_label = ttk.Label(
        # master=self._frame, text="Further functionality is present in application logic but not yet accessible via the UI", background="#AFE4DE")

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_logout)

        logout_button.grid(row=0, column=3, sticky=(
            constants.E), padx=5, pady=5)
        header_label.grid(row=0, columnspan=2, sticky=(
            constants.N), padx=5, pady=5)

        # create_expense_label.grid(
        # columnspan=2, sticky=(constants.N), padx=5, pady=5)

    def _initialize_create_expense_view(self):
        header_label = ttk.Label(
            master=self._frame, text="Create Expense", background="#AFE4DE")

        expense_name_label = ttk.Label(
            master=self._frame, text="Name *", background="#AFE4DE")
        self._expense_name = ttk.Entry(master=self._frame)

        expense_amount_label = ttk.Label(
            master=self._frame, text="Amount *", background="#AFE4DE")
        self._expense_amount = ttk.Entry(master=self._frame)

        expense_date_label = ttk.Label(
            master=self._frame, text="Date (YYYY-MM-DD)", background="#AFE4DE")
        self._expense_date = ttk.Entry(master=self._frame)

        expense_category_label = ttk.Label(
            master=self._frame, text="Create new category (default) or choose category", background="#AFE4DE")

        create_expense_button = ttk.Button(
            master=self._frame, text="Create new expense", command=self._handle_create_new_expense)

        header_label.grid(row=3, padx=5, pady=5, sticky=(constants.W))
        expense_name_label.grid(padx=5, pady=5)
        self._expense_name.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        expense_amount_label.grid(padx=5, pady=5)
        self._expense_amount.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        expense_date_label.grid(padx=5, pady=5)
        self._expense_date.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        expense_category_label.grid(padx=5, pady=5)
        self._add_expense_category()

        create_expense_button.grid(column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _add_expense_category(self):

        self._expense_category = ttk.Entry(master=self._frame)

        self._selected_category = StringVar()
        self._selected_category.set("undefined")

        category_options = self.expense_service.list_all_categories()
        category_options.append("undefined")

        if category_options:
            expense_category_dropdown = OptionMenu(
                self._frame, self._selected_category, *category_options)

        self._expense_category.grid(row=7, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        expense_category_dropdown.grid(row=8, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _handle_create_new_expense(self):
        expense_name = self._expense_name.get()
        expense_amount = self._expense_amount.get()

        expense_date = self._expense_date.get()
        expense_category = self._expense_category.get()
        if not expense_category:
            expense_category = self._selected_category.get()

        if expense_name and expense_amount:
            try:
                self.expense_service.check_input_validity_expense_amount(
                    expense_amount)
                if expense_date:
                    self.expense_service.check_input_validity_expense_date(
                        expense_date)

                self.expense_service.create_new_expense(
                    expense_name, expense_amount, expense_date, expense_category)

                self._expense_name.delete(0, constants.END)
                self._expense_amount.delete(0, constants.END)
                self._expense_date.delete(0, constants.END)
                self._expense_category.delete(0, constants.END)
                self._selected_category.set("undefined")
                self._add_expense_category()

            except InvalidInputError:
                self._display_error_message(
                    "Invalid input. Make sure you have entered a nonnegative numeric amount and a valid date in YYYY-MM-DD format")

    def _display_error_message(self, message):
        messagebox.showerror("Error", message)

    def _handle_logout(self):
        login_service.logout_user()
        self._handle_return_to_login()

    def _initialize_view_expense_total(self):
        header_label = ttk.Label(
            master=self._frame, text="Your Expense History", background="#AFE4DE")
        total = self.expense_service.get_total_all_expenses_by_user()
        display_total = ttk.Label(
            master=self._frame, text=f"Total amount spent: {total} €", background="#AFE4DE")

        header_label.grid(padx=5, pady=5,  sticky=(constants.W))
        display_total.grid(padx=5, pady=5)

    def _initialize_view_expense_table(self):
        list_view_label = ttk.Label(
            master=self._frame, text="View expenses as Table", borderwidth=5, relief="sunken")
        graph_view_button = ttk.Button(
            master=self._frame, text="View expenses as graph")

        list_view_label.grid(row=12, padx=5, pady=5)
        graph_view_button.grid(row=12, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._get_expense_table()

    def _get_expense_table(self):
        expense_list = self.expense_service.list_all_expenses()
        if expense_list:
            for list_row in range(len(expense_list)):
                for list_column in range(len(expense_list[0])):
                    entry = Entry(master=self._frame)
                    entry.grid(row=13+list_row, column=list_column, sticky=(constants.NSEW))
                    entry.insert(END, expense_list[list_row][list_column])
        else:
            label=ttk.Label(master=self._frame, text="You have not entered any expenses yet")
            label.grid(padx=5, pady=5)