from tkinter import *

calculation = ''
# FUNCTIONS


def press_buttons(symbol):
    global calculation
    calculation = calculation + str(symbol)
    text_entry.set(calculation)


def press_equal():
    global calculation
    total = str(eval(calculation))
    text_entry.set(total)
    calculation = ""


def clear():
    global calculation
    calculation = ''
    text_entry.set("")


# create object
root = Tk()
# name
root.title("Calculator")
# geometry size
root.geometry("250x347")
# background color
root.configure(bg='black')

text_entry = StringVar()
button_expression_field = Entry(root, textvariable=text_entry, font=("Arial" "bolt", 20), bg="grey" )
button_expression_field.place(x=1, y=1, height=147, width=247)

# BUTTONS

ac_button = Button(root, text="AC", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                   command=clear)
plus_button = Button(root, text="+", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                     command=lambda: press_buttons("+"))
minus_button = Button(root, text="-", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                      command=lambda: press_buttons("-"))
multiply_button = Button(root, text="x", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                         command=lambda: press_buttons("*"))
divide_button = Button(root, text="/", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                         command=lambda: press_buttons("//"))
button_7 = Button(root, text="7", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(7))
button_8 = Button(root, text="8", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(8))
button_9 = Button(root, text="9", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(9))
button_4 = Button(root, text="4", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(4))
button_5 = Button(root, text="5", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(5))
button_6 = Button(root, text="6", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(6))
button_1 = Button(root, text="1", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(1))
button_2 = Button(root, text="2", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(2))
button_3 = Button(root, text="3", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(3))
button_0 = Button(root, text="0", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(0))
button_comma = Button(root, text=",", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=lambda: press_buttons(','))
button_equal = Button(root, text="=", font=("Arial" "bolt", 20), bg="darkgrey", fg="black",
                  command=press_equal)

# BUTTONS PLACE
ac_button.place(x=7, y=150, height=35, width=55,)
plus_button.place(x=67, y=150, height=35, width=55)
minus_button.place(x=127, y=150, height=35, width=55)
multiply_button.place(x=187, y=150, height=35, width=55)
divide_button.place(x=187, y=190, height=35, width=55)
button_7.place(x=7, y=190, height=35, width=55)
button_8.place(x=67, y=190, height=35, width=55)
button_9.place(x=127, y=190, height=35, width=55)
button_4.place(x=7, y=230, height=35, width=55)
button_5.place(x=67, y=230, height=35, width=55)
button_6.place(x=127, y=230, height=35, width=55)
button_1.place(x=7, y=270, height=35, width=55)
button_2.place(x=67, y=270, height=35, width=55)
button_3.place(x=127, y=270, height=35, width=55)
button_0.place(x=7, y=310, height=35, width=115)
button_comma.place(x=127, y=310, height=35, width=55)
button_equal.place(x=187, y=230, height=115, width=55)


root.mainloop()
