from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "Black"
current_card = {}
to_learn ={}

try:
    data = pandas.read_csv("data/characters.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/characters.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_description, text=current_card["Description"])
    canvas.itemconfig(card_front_img, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_description, text=current_card["Character"])
    canvas.itemconfig(front_card, image=card_back_img)

def is_correct():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/correct.csv", index=False)

    next_card()


window = Tk()
window.title("Drago Age Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)


canvas = Canvas(width=800, height=600)
card_front_img = PhotoImage(file="images/da_card_front.png")
card_back_img = PhotoImage(file="images/da_card_back.png")
front_card = canvas.create_image(400, 300, image=card_front_img)
card_description = canvas.create_text(400, 300, text="Description", font=("Cinzel", 15, "italic", "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/da_wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/da_right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, command=is_correct)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()