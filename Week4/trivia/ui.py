from tkinter import *
from da_trivia import Quiz

bg=BACKGROUND_COLOR = "Black"

class QuizInterface:

    def __init__(self, quiz: Quiz):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Dragon Age Trivia")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=BACKGROUND_COLOR, font=("Arial", 25))
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR)
        self.card_front_img = PhotoImage(file="images/da_card_front.png")
        self.front_card = self.canvas.create_image(400, 300, image=self.card_front_img)
        self.question_text = self.canvas.create_text(400, 300, text="Questions?", font=("Cinzel", 15, "italic", "bold"), width=175)
        self.canvas.config(bg=BACKGROUND_COLOR)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)


        self.wrong_image = PhotoImage(file="images/da_wrong.png")
        self.wrong_button = Button(image=self.wrong_image, bg=BACKGROUND_COLOR, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.right_image = PhotoImage(file="images/da_right.png")
        self.right_button = Button(image=self.right_image, bg=BACKGROUND_COLOR, command=self.right_pressed)
        self.right_button.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="black")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    #
    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    #
    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





