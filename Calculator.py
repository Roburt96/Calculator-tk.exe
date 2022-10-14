from tkinter import *

# create object
root = Tk()
# name
root.title("Calculator")
# geometry size
root.geometry("300x400")
# background color
root.configure(bg='black')

# FUNCTIONS
def clear():




# BUTTONS
AC_button = Button(root, text="AC", font="arial 15", bg="darkgrey", fg="white", command=clear)
plus_minus = Button(root, text="+/-", font="arial 15", bg="darkgrey", fg="white")

# BUTTON PLACES
AC_button.place(x=10, y=150)
plus_minus.place(x=60, y=150)

writing_numbers = StringVar()
enter_numbers = Entry(root, textvariable= writing_numbers, fg='white', font="arial 15", width=30, bg='black')
enter_numbers.place(x=0, y=110)






root.mainloop()