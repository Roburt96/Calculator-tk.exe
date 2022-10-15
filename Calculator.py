import tkinter as tk

calculation = ''
# FUNCTIONS
def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, "end")

def add_symbols(*symbols):
    global calculation
    symbol = str(plus_button.get())



# create object
root = tk.Tk()
# name
root.title("Calculator")
# geometry size
root.geometry("300x400")
# background color
root.configure(bg='black')
text_result = tk.Text(root, height=2, width=25, font=("Arial", 20))
text_result.grid(columnspan=5)


# BUTTONS
ac_button = tk.Button(root, text="AC", width=1, font=("Arial", 20), bg="grey", fg="black", command=clear)
plus_button = tk.Button(root, width=1, text="+", font=("Arial", 20), bg="grey", fg="black", command=add_symbols)
# BUTTONS PLACE
ac_button.place(x=10, y=150)
plus_button.place(x=60, y=150)


root.mainloop()