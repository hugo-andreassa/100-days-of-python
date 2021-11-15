import json
from random import *
from tkinter import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    # Copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    etr_password.delete(0, END)
    etr_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entrys():
    etr_web.delete(0, END)
    # etr_email.delete(0, END)
    etr_password.delete(0, END)


def save():
    website = etr_web.get()
    email = etr_email.get()
    password = etr_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    with open("data.json", "w+") as file:
        # Read old data
        data = json.load(file)
        # Update old data with new data
        data.update(new_data)
        # Save updated data to file
        json.dump(data, file, indent=4)

        clear_entrys()
        etr_web.focus()


def find_data():
    website = etr_web.get()

    with open("data.json", "r") as file:
        data = json.load(file)
        info = data.get(website)

        if info is not None:
            messagebox.showinfo(title="Data", message=f"Email: {info['email']}, Password: {info['password']}")

        # print(data)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.config(height=200, width=200)

# --------------- Canvas --------------- #
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# --------------- Labels --------------- #
lbl_web = Label(text="Website:")
lbl_web.grid(row=1, column=0)

lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

# --------------- Entrys --------------- #
etr_web = Entry(width=21)
etr_web.grid(row=1, column=1)

etr_email = Entry(width=39)
etr_email.insert(0, "hugo.andreassa@gmail.com")
etr_email.grid(row=2, column=1, columnspan=2)

etr_password = Entry(width=21)
etr_password.grid(row=3, column=1)

# --------------- Buttons --------------- #
btn_generate = Button(width=15, text="Find", command=find_data)
btn_generate.grid(row=1, column=2)

btn_generate = Button(width=15, text="Generate Password", command=generate_password)
btn_generate.grid(row=3, column=2)

btn_add = Button(width=33, text="Add", command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
