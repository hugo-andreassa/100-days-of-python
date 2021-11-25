from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Labels ---------------------------
        self.lbl_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(column=1, row=0)

        # Canvas ---------------------------
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.lbl_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons --------------------------
        false_img = PhotoImage(file="images/false.png")
        self.btn_wrong = Button(image=false_img, command=self.right_pressed)
        self.btn_wrong.grid(column=0, row=2)

        true_img = PhotoImage(file="images/true.png")
        self.btn_right = Button(image=true_img, command=self.wrong_pressed)
        self.btn_right.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.lbl_score.config(text=f"Score: {self.quiz_brain.score}")

        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.lbl_question, text=q_text)
        else:
            self.canvas.itemconfig(self.lbl_question, text="You've reached the end of the quiz.")
            self.btn_right.config(state="disable")
            self.btn_wrong.config(state="disable")

    def right_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def wrong_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
