from tkinter import *

window = Tk()
window.title("My first FUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Components ------------------------------------------------------------------

# Label -----------------------------------------------------------------------
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()
my_label.grid(column=0, row=0)


# Button ----------------------------------------------------------------------
def button_clicked():
    print("I got clicked")
    my_label.config(text=entry.get())


button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry -----------------------------------------------------------------------
entry = Entry(width=30)
# entry.pack()
print(entry.get())
entry.grid(column=2, row=2)

# Other Components ------------------------------------------------------------







window.mainloop()