from tkinter import Tk

from matplotlib import pyplot
from ui.login_view import LoginView
from ui.create_account_view import CreateAccountView
from ui.expense_tracker_view import ExpenseTrackerView
from ui.expense_graph_view import ExpenseGraph
from ui.expense_creation_view import ExpenseCreationView
from ui.expense_overview import ExpenseOverview


class UI:
    """This class manages switching between different UI views and windows.
    """

    def __init__(self, root):
        """Class constructor

        Args:
            root (Tkinter frame): The root Tkinter frame of the application
        """
        self._root = root
        self._current_view = None

        self._root.protocol('WM_DELETE_WINDOW', self._exit)

    def start(self):
        """Shows the UI login view when starting the application.
        """
        self._show_login_view()

    def _exit(self):
        pyplot.close("all")
        self._root.destroy()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login(self):
        self._show_login_view()

    def _handle_create_account(self):
        self._show_create_account_view()

    def _handle_expense_tracker(self):
        self._show_expense_tracker_view()

    def _handle_expense_overview(self):
        self._show_expense_overview()

    def _handle_expense_creation(self):
        self._show_expense_creation_view()

    def _handle_expense_graph(self):
        self._show_expense_graph_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._handle_create_account, self._handle_expense_tracker)
        self._current_view.configure()

    def _show_expense_overview(self):
        self._hide_current_view()

        self._current_view = ExpenseOverview(
            self._root, self._handle_expense_tracker, self._handle_expense_graph, self._handle_expense_creation)
        self._current_view.configure()

    def _show_create_account_view(self):
        self._hide_current_view()

        self._current_view = CreateAccountView(
            self._root, self._handle_login)
        self._current_view.configure()

    def _show_expense_tracker_view(self):
        self._hide_current_view()

        self._current_view = ExpenseTrackerView(
            self._root, self._handle_login, self._handle_expense_overview, self._handle_expense_creation)
        self._current_view.configure()

    def _show_expense_creation_view(self):
        self._hide_current_view()

        self._current_view = ExpenseCreationView(
            self._root, self._handle_expense_tracker, self._handle_expense_overview,)
        self._current_view.configure()

    def _show_expense_graph_view(self):
        self._hide_current_view()

        self._current_view = ExpenseGraph(
            self._root, self._handle_expense_tracker)
        self._current_view.configure()
