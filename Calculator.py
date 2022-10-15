from tkinter import *

calculation = ''
# FUNCTIONS
def press_buttons(symbol):
    global calculation
    expression = calculation + str(symbol)
    calculm.set(expression)

# def clear():
#     global calculation
#     calculation = ''
#     text_result.delete(1.0, "end")


# create object
root = Tk()
# name
root.title("Calculator")
# geometry size
root.geometry("250x450")
# background color
root.configure(bg='black')

text_entry = StringVar()
button_expression_field = Entry(root, textvariable=text_entry, font=("Arial" "bolt", 20), bg="grey" )
button_expression_field.place(x=1, y=1, height=147, width=247)

# BUTTONS

ac_button = Button(root, text="AC", font=("Arial" "bolt", 20), bg="grey", fg="black",
                   command=lambda: press_buttons("AC"))
plus_button = Button(root, text="+", font=("Arial" "bolt", 20), bg="grey", fg="black",
                     command=lambda: press_buttons("+"))
minus_button = Button(root, text="-", font=("Arial" "bolt", 20), bg="grey", fg="black",
                      command=lambda: press_buttons("-"))
multiply_button = Button(root, text="*", font=("Arial" "bolt", 20), bg="grey", fg="black",
                         command=lambda: press_buttons("*"))
button_7 = Button(root, text="7", font=("Arial" "bolt", 20), bg="grey", fg="black",
                  command=lambda: press_buttons(7))
button_8 = Button(root, text="8", font=("Arial" "bolt", 20), bg="grey", fg="black",
                  command=lambda: press_buttons(8))
button_9 = Button(root, text="9", font=("Arial" "bolt", 20), bg="grey", fg="black",
                  command=lambda: press_buttons(9))
# BUTTONS PLACE
ac_button.place(x=7, y=150, height=35, width=55,)
plus_button.place(x=67, y=150, height=35, width=55)
minus_button.place(x=127, y=150, height=35, width=55)
multiply_button.place(x=187, y=150, height=35, width=55)
button_7.place(x=7, y=190, height=35, width=55)
button_8.place(x=67, y=190, height=35, width=55)
button_9.place(x=127, y=190, height=35, width=55)

root.mainloop()