from tkinter import ttk, constants, OptionMenu, StringVar, messagebox, END, VERTICAL
from services.login_service import login_service
from repositories.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService
from entities.category import Category
from entities.expense import Expense

class ExpenseOverview:
    def __init__(self, root, expense_tracker, expense_graph):
        self._root = root
        self._handle_return_to_homescreen = expense_tracker
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
    
    def _initialize_start_view(self):
        header_label = ttk.Label(
            master=self._frame, text="Your Expenses", background="#AFE4DE")

        logout_button = ttk.Button(
            master=self._frame, text="Home", command=self._handle_return_to_homescreen)
       
        header_label.grid(row=0, columnspan=2, sticky=(
            constants.N), padx=5, pady=5)
        logout_button.grid(row=0, column=3, sticky=(
            constants.E), padx=5, pady=5)

        self._initialize_view_expense_total()
        self._initialize_view_expense_tables()

    def _initialize_view_expense_total(self):
        total = self.expense_service.get_total_all_expenses_by_user()
        display_total = ttk.Label(
            master=self._frame, text=f"Total amount spent: {total} €", background="#AFE4DE")

        display_total.grid(row=1, sticky=(
            constants.W),padx=5, pady=5)

    def _initialize_view_expense_tables(self):
        table_view_all_button = ttk.Button(
            master=self._frame, text="View all expenses as table", command=self._get_expense_table)
        table_view_by_category_button = ttk.Button(master=self._frame, text="View expenses by category as table", command=self._get_expense_category_table)
        graph_view_button = ttk.Button(
            master=self._frame, text="View expenses as graph", command=self._expense_graph_view)
    
        table_view_all_button.grid(row=2, column=0, padx=5, pady=5, sticky=(
            constants.W))
        table_view_by_category_button.grid(row=2, column=1, padx=5, pady=5)
        graph_view_button.grid(row=1, column=3, padx=10, pady=10)

        self._get_expense_table()
        self._get_category()

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
            self._expense_table.grid(row=4, columnspan=2, sticky='NSEW', padx=5, pady=5)
            self._insert_table_scrollbar(self._expense_table)

            self._initialize_edit_expenses()
        else:
            note=ttk.Label(master=self._frame, text="You do not currently have any recorded expenses", background="#AFE4DE")
            note.grid(row=4, padx=5, pady=5)
    
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
                self._expense_table.grid(row=4, columnspan=2, sticky='NSEW', padx=5, pady=5)

                self._insert_table_scrollbar(self._expense_table)

                self._initialize_edit_expenses()
            else:
                note=ttk.Label(master=self._frame, text="You do not currently have any recorded expenses", background="#AFE4DE")
                note.grid(row=4, padx=5, pady=5)

    def _delete_table(self):
        for element in self._expense_table.get_children():
            self._expense_table.delete(element)
    
    def _insert_table_scrollbar(self, table):
        scrollbar = ttk.Scrollbar(self._frame, orient=VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=4, column=2, sticky='NS')
    
    def _get_category(self):
        self._selected_table_category = StringVar()
        category_options = self.expense_service.list_all_categories()
        if category_options:
            expense_category_dropdown = OptionMenu(
                self._frame, self._selected_table_category, *category_options)
            expense_category_dropdown.grid(row=3, column=1, padx=5, pady=5)

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