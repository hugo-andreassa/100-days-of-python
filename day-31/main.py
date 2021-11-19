import random

from pandas import *
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    change_card_text("English", current_card["English"], "black")


def change_card_text(title: str, word: str, color: str):
    canvas.itemconfig(card_title, text=title, fill=color)
    canvas.itemconfig(card_word, text=word, fill=color)


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)

    canvas.itemconfig(card_image, image=card_front_img)
    change_card_text("French", current_card["French"], "black")
    flip_timer = window.after(3000, func=flip_card)


# ------------------------- NEW CARDS -------------------------
words_dict = read_csv("data/french_words.csv").to_dict(orient="records")
print(words_dict)

# ------------------------- CREATING UI -------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas -------------------------
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=2)
# Create card
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
# Create title
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
# Create subtitle
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

# Buttons ------------------------
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=2)

# Generate first word
next_card()

window.mainloop()
