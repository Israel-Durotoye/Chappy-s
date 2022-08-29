# import calender module
import calendar
# import tkinter module
from tkinter import *

def show_calender():
    root = Tk()
    # root.config(background = 'white')
    root.title("Calender For The Year")
    root.resizable(False, False)
    root.geometry("400x480")
    year = int(year_field.get())
    root_content = calendar.calendar(year)
    calender_year = Label(root, text = root_content ,font = "chalkboard 10", justify = CENTER)
    calender_year.grid(row = 5, column = 1, padx = 20)
    root.mainloop()

# Driver Code
if __name__ == '__main__':
    new = Tk()
    # new.config(background = 'grey')
    new.title("Calender")
    new.geometry("200x140")
    new.resizable(False, False)
    cal = Label(new, text = "Calender", font = ("chalkboard", 28, 'bold'), anchor = "center")
    # Label for year entry
    year = Label(new, text = "Enter Year:")
    # text box for year input
    year_field = Entry(new)
    button = Button(new, text = 'Show Calender', command = show_calender)
    # adjusting widgets in position
    cal.grid(row = 1, column = 1)
    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    button.grid(row = 4, column = 1)
    # exit.grid(row = 6, column = 1)
    new.mainloop()