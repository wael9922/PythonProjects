from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
import os

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")# make it pick up where it left off
    words_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")  # this will run if it's first time learning
    words_data = data.to_dict(orient="records")
except pd.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")  # this will run if it's first time learning
    words_data = data.to_dict(orient="records")

current_card = {}


def next_card():
    """call the next card and view it"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if len(words_data) == 0:
        canvas.itemconfig(card, image=front_card)
        canvas.itemconfig(card_title, text="Congrats!", fill="black")
        canvas.itemconfig(card_word, text="You learned all words!\nclick reset to reset cards", fill="black")
        return

    current_card = random.choice(words_data)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(5000, lambda: flip_card())
    canvas.itemconfig(card, image=front_card)


def flip_card():
    """flip the card after a specific time"""
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])


def is_known():
    """keep track of the words the user has learned"""
    if current_card in words_data:
        words_data.remove(current_card)
        words_data_remaining = pd.DataFrame(words_data)
        words_data_remaining.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def reset_cards():
    """reset the cards to start over"""
    global words_data

    # Ask for confirmation
    confirm = messagebox.askyesno(
        "Reset Cards",
        "Are you sure you want to reset all progress?"
    )

    if confirm:
        data_reset = pd.read_csv("data/french_words.csv")
        words_data = data_reset.to_dict(orient="records")

        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")

        messagebox.showinfo("Success", "Cards have been reset!")
        next_card()

# UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")  # to be used later

card = canvas.create_image(400, 263, image=front_card, )
card_title = canvas.create_text(400, 120, text="Title", font=("ariel", 40, "normal"))
card_word = canvas.create_text(400, 263, text="Word", font=("ariel", 40, "normal"))

unknown_icon = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_icon, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_icon = PhotoImage(file="images/right.png")
known_button = Button(image=known_icon, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_cards)
reset_button.grid(row=2, column=0, columnspan=2)
flip_timer = window.after(3000, lambda: flip_card())
next_card()

window.mainloop()
