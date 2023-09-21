from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------- WRONG OR RIGHT ---------------------#
current_card = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    words = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer, words
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    french_word = current_card["French"]
    back_canvas.itemconfig(background_image, image=front_image)
    back_canvas.itemconfig(title, text=f"French", fill="black")
    back_canvas.itemconfig(word, text=f"{french_word}", fill="black")
    flip_timer = window.after(3000, func=show_english)


def show_english():
    back_canvas.itemconfig(background_image, image=back_image)
    english_word = current_card["English"]
    back_canvas.itemconfig(title, text=f"English", fill="white")
    back_canvas.itemconfig(word, text=f"{english_word}", fill="white")


def known():
    words.remove(current_card)
    n_data = pandas.DataFrame(words)
    n_data.to_csv("./data/words_to_learn.csv", index=False)
    next_word()

# ------------------- UI Design ---------------------- #


window = Tk()
window.title("Flash Cards")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_english)

back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

back_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# back_canvas.create_image(400, 263, image=back_image)
background_image = back_canvas.create_image(400, 263, image=front_image)
back_canvas.grid(row=0, column=0, columnspan=2)
title = back_canvas.create_text(400, 150, text=f"", font=("Ariel", 40, "italic"))
word = back_canvas.create_text(400, 263, text=f"", font=("Ariel", 60, "bold"))


right_button = Button(image=right_image, highlightthickness=0, border=0, command=known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=next_word)
wrong_button.grid(row=1, column=0)

next_word()


window.mainloop()
