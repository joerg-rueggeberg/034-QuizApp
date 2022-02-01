from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR_BG = "#375362"
THEME_COLOR_FG = "white"
FONT_SCORE = ("Arial", 10, "bold")
FONT_QUESTION = ("Arial", 16, "italic")


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Open Trivia DB Quiz (Sinclair)")
        self.window.config(padx=20, pady=20, background=THEME_COLOR_BG)

        # CANVAS
        self.canvas = Canvas(width=300, height=250, border=0, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text",
                                                     font=FONT_QUESTION, fill=THEME_COLOR_BG, width=280)

        # LABEL
        self.label_question = Label(text=f"Question: {self.quiz.question_number}/{len(question_data)}",
                                    font=FONT_SCORE, bg=THEME_COLOR_BG, fg=THEME_COLOR_FG)
        self.label_question.grid(row=0, column=1, sticky="e")
        self.label_score = Label(text=f"Score: {self.quiz.score}",
                                 font=FONT_SCORE, bg=THEME_COLOR_BG, fg=THEME_COLOR_FG)
        self.label_score.grid(row=1, column=1, sticky="e")
        label_logo_img = PhotoImage(file="./images/logo.png")
        self.label_logo = Label(image=label_logo_img, bg=THEME_COLOR_BG)
        self.label_logo.grid(row=0, column=0, rowspan=2, sticky="nw")

        # BUTTONS
        button_true_img = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=button_true_img, command=self.click_true, borderwidth=0)
        self.button_true.grid(row=3, column=0)
        button_false_img = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=button_false_img, command=self.click_false, borderwidth=0)
        self.button_false.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            new_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_text)
            self.label_question.config(text=f"Question: {self.quiz.question_number}/{len(question_data)}")
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the Quiz with:\n\n"
                                                            f"{self.quiz.score} pts. out of {len(question_data)}")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def click_true(self):
        answer_status = self.quiz.check_answer("True")
        self.feedback(answer_status)

    def click_false(self):
        answer_status = self.quiz.check_answer("False")
        self.feedback(answer_status)

    def feedback(self, answer_status_input):
        if answer_status_input:
            self.canvas.config(bg="#83b8a0")
        else:
            self.canvas.config(bg="#e8938d")
        self.window.after(1000, self.get_next_question)
