from tkinter import *
import pandas as pd
from datetime import datetime
import random
from time import sleep as s

BACKGROUND_COLOR = "#B1DDC6"

try:
    DATA = "data/known_words.csv"
except:
    DATA = "data/french_words.csv"

pddata = pd.read_csv(DATA)
dictdata = pddata.to_dict(orient="records")
# french_words = dictdata["French"]
# english_words = dictdata["English"]
current = {}


# -------------------------------- FUNCTIONS ----------------------------------------------------
def correct():
    dictdata.remove(current)
    new_data = pd.DataFrame(dictdata)
    new_data.to_csv("data/known_words.csv", index=False)
    nextcard()


def nextcard():
    global current, flip_timer
    window.after_cancel(flip_timer)
    current = random.choice(dictdata)
    canvas.itemconfig(card, image=file)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current["French"], fill="black")
    flip_timer = window.after(3000, flip_english)
    # canvas.after(3000, flip_english(x))


def flip_english():
    canvas.itemconfig(card, image=file2)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current["English"], fill="white")


# -------------------------------- UI COMPONENTS ----------------------------------------------------


window = Tk()
window.minsize(width=900, height=900)
window.title("Flash Cards App")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_english)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
file = PhotoImage(file="images/card_front.png")
file2 = PhotoImage(file="images/card_back.png")

canvas.grid(column=0, row=0, columnspan=3)
# canvas.after(3000, flip_english(y))
card = canvas.create_image(400, 300, image=file)
title = canvas.create_text(400, 200, text="French", font=("Courier", 25, "italic"), fill="black")
word = canvas.create_text(400, 300, text="", font=("Courier", 25, "bold"), fill="black")
# score = canvas.create_text()
# ------------- BUTTONS ---------


correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

correct_button = Button(image=correct_image, command=correct, highlightthickness=0)
correct_button.grid(row=1, column=2)

wrong_button = Button(image=wrong_image, command=nextcard, highlightthickness=0)
wrong_button.grid(row=1, column=0)

nextcard()

window.mainloop()
