from tkinter import ttk, constants, OptionMenu, StringVar, messagebox, END, VERTICAL
from tkinter.messagebox import showinfo
from services.login_service import login_service
from repositories.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService, InvalidInputError
from entities.category import Category
from entities.expense import Expense

class ExpenseTrackerView:
    def __init__(self, root, handle_login, expense_graph):
        self._root = root
        self._handle_return_to_login = handle_login
        self._expense_graph_view = expense_graph

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
        self._initialize_view_expense_tables()

    def _initialize_start_view(self):
        header_label = ttk.Label(
            master=self._frame, text="Your Expense Tracker", background="#AFE4DE")

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_logout)

        logout_button.grid(row=0, column=3, sticky=(
            constants.E), padx=5, pady=5)
        header_label.grid(row=0, columnspan=2, sticky=(
            constants.N), padx=5, pady=5)

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

        create_expense_button.grid(column=1, sticky=(
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

    def _initialize_view_expense_tables(self):
        table_view_all_button = ttk.Button(
            master=self._frame, text="View all expenses as table", command=self._get_expense_table)
        table_view_by_category_button = ttk.Button(master=self._frame, text="View expenses by category as table", command=self._get_expense_category_table)
        graph_view_button = ttk.Button(
            master=self._frame, text="View expenses as graph", command=self._expense_graph_view)
    
        table_view_all_button.grid(row=12, padx=5, pady=5)
        table_view_by_category_button.grid(row=12, column=1, padx=5, pady=5)
        graph_view_button.grid(row=12, column=3, padx=10, pady=10)

        self._get_expense_table()
        self._get_category()
        self._initialize_edit_expenses()

    def _get_expense_table(self):
        if self._expense_table:
            self._delete_table()

        expense_list = self.expense_service.list_all_expenses()

        if expense_list:
            column_names = ["Expense Name", "Amount", "Date", "Category"]
            self._expense_table = ttk.Treeview(master=self._frame, columns=column_names, show ="headings", selectmode="browse")
            self._style.configure("Treeview.Heading", background="#AFE4DE")
            for column in column_names:
                self._expense_table.heading(column, text=column)
            for expense in expense_list:
                self._expense_table.insert("", END, values=expense)
            self._expense_table.grid(row=14, columnspan=2, sticky='NSEW', padx=5, pady=5)
            self._insert_table_scrollbar(self._expense_table)
        else:
            note=ttk.Label(master=self._frame, text="You do not currently have any recorded expenses", background="#AFE4DE")
            note.grid(row=14, padx=5, pady=5)
    
    def _get_expense_category_table(self):
        if self._expense_table:
            self._delete_table()

        category=self._selected_table_category.get()

        if category:
            expense_list = self.expense_service.list_expenses_by_category(Category(category))
            if expense_list:

                column_names = ["Expense Name", "Amount", "Date", "Category"]
                self._expense_table = ttk.Treeview(master=self._frame, columns=column_names, show ="headings", selectmode="browse")
                self._style.configure("Treeview.Heading", background="#AFE4DE")

                for column in column_names:
                    self._expense_table.heading(column, text=column)
                for expense in expense_list:
                    self._expense_table.insert("", END, values=expense)
                self._expense_table.grid(row=14, columnspan=2, sticky='NSEW', padx=5, pady=5)

                self._insert_table_scrollbar(self._expense_table)

            else:
                note=ttk.Label(master=self._frame, text="You do not currently have any recorded expenses", background="#AFE4DE")
                note.grid(row=14, padx=5, pady=5)

    def _delete_table(self):
        for element in self._expense_table.get_children():
            self._expense_table.delete(element)
    
    def _insert_table_scrollbar(self, table):
        scrollbar = ttk.Scrollbar(self._frame, orient=VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=14, column=2, sticky='NS')
    
    def _get_category(self):
        self._selected_table_category = StringVar()
        category_options = self.expense_service.list_all_categories()
        if category_options:
            expense_category_dropdown = OptionMenu(
                self._frame, self._selected_table_category, *category_options)
            expense_category_dropdown.grid(row=13, column=1, padx=5, pady=5)

    def _initialize_edit_expenses(self):
        edit_expense_label = ttk.Label(master=self._frame, text="Choose expense to edit by selecting it via click, choose expense aspect to edit in the dropdown and then fill in changed value in the text field.", background="white")
        
        self._selected_editable = StringVar()
        edit_options = ["Name", "Amount", "Date", "Category"]
        edit_expense_dropdown = OptionMenu(self._frame, self._selected_editable, *edit_options)

        self._user_change_input = ttk.Entry(master=self._frame)
        
        edit_expense_label.grid(padx=5, pady=5)
        edit_expense_dropdown.grid(padx=5, pady=5)
        self._user_change_input.grid(sticky=(
            constants.E, constants.W), padx=5, pady=5)

        edit_expense_button = ttk.Button(master=self._frame, text="Edit Expense", command=self._edit_expenses)
        edit_expense_button.grid(padx=5, pady=5)

    def _edit_expenses(self):
        editable=self._selected_editable.get()
        chosen_expense = self._expense_table.focus()

        if editable and chosen_expense:
            chosen_expense_details = self._expense_table.item(chosen_expense)

            old_expense = Expense(chosen_expense_details.get("values")[0], chosen_expense_details.get("values")[1],
                                  chosen_expense_details.get("values")[2], chosen_expense_details.get("values")[3])

            user_change = self._user_change_input.get()
            if user_change:
                if editable == "Name":
                    self.expense_service.edit_expense_name(user_change, old_expense)
                elif editable == "Amount":
                    self.expense_service.edit_expense_amount(user_change, old_expense)
                elif editable =="Date":
                    self.expense_service.edit_expense_date(user_change, old_expense)
                elif editable =="Category":
                    self.expense_service.edit_expense_category(user_change, old_expense)
            
            self._user_change_input.delete(0, constants.END)
            self._get_expense_table()

#figure out "Edit expenses" --> add check validity of input in expense service and error messages in UI
# refactor UI!!

#make graphing function in Exp.Services
#make UI for that
#add category total to table view
#revert view more often
#add delete expense, add delete and edit category