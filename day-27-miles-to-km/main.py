from tkinter import *


def btn_calculate_action():
    lbl_result.config(text=entry_miles.get())


window = Tk()
window.title("Miles to Km calculator")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

lbl_is_equal = Label(text="is equal to")
lbl_is_equal.grid(column=1, row=1)

lbl_miles = Label(text="Km")
lbl_miles.grid(column=3, row=1)

lbl_result = Label(text="0")
lbl_result.grid(column=2, row=1)

lbl_miles = Label(text="Miles")
lbl_miles.grid(column=3, row=0)

entry_miles = Entry(width=15)
entry_miles.grid(column=2, row=0)

btn_calculate = Button(text="Calculate", command=btn_calculate_action)
btn_calculate.grid(column=2, row=2)


window.mainloop()
