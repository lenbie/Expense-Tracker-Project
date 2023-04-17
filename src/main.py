from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Expense Tracker")

ui = UI(window)
ui.start()
window.mainloop()
