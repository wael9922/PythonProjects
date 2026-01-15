from tkinter import *
from quizbrain import QuizBrain
from tkinter import simpledialog
from data import get_questions_data
from question import Question

THEME_COLOR = "#375362"


class QuizInterface:
    """Build The quiz Interface"""

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)
        self.window.withdraw()  # hide window initially

        # Center the window on screen with full height
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 450
        window_height = screen_height  # Full screen height
        x = (screen_width // 2) - (window_width // 2)
        y = 0  # Start from top
        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", pady=20, font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)
        self.question_canvas = self.canvas.create_text(
            (200, 175),
            width=360,
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")

        # ask the user for how many questions he wants for the quiz
        self.questions_count = simpledialog.askinteger(title="Questions", prompt="How many questions you want?")
        self.quiz = self.create_questions(self.questions_count)

        self.window.deiconify()  # Show window after everything is ready

        self.false_btn = Button(image=false_icon, highlightthickness=0, command=self.false_answer, borderwidth=0)
        self.false_btn.grid(row=2, column=0, padx=20, pady=20)

        self.true_btn = Button(image=true_icon, highlightthickness=0, command=self.true_answer, borderwidth=0)
        self.true_btn.grid(row=2, column=1, padx=20, pady=20)

        self.reset_btn = Button(text="Try Again", highlightthickness=0, command=self.try_again, font=("Arial", 12, "bold"),
            bg="white", fg=THEME_COLOR, padx=20, pady=20, )

        self.new_question()  # call the first question

        self.window.mainloop()

    @staticmethod
    def create_questions(count):
        """Create The question data and prepare it return QuizBrain Object"""
        data = get_questions_data(count)
        questions_bank = []
        for question in data:
            questions_bank.append(Question(question["question"], question['correct_answer']))
        return QuizBrain(questions_bank)

    def new_question(self):
        """Update Canvas text with the new question"""
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_canvas, text=q_text)
        if q_text == "Quiz is Over":
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            # Show the reset button
            self.reset_btn.grid(row=3, column=0, columnspan=2, pady=20)
        else:
            # Hide the reset button during the quiz
            self.reset_btn.grid_forget()

    def true_answer(self):
        """Set the user answer to True"""
        is_right = self.quiz.check_answer(self.quiz.current_question, "True")
        self.feedback(is_right)

    def false_answer(self):
        """Set the user answer to False"""
        is_right = self.quiz.check_answer(self.quiz.current_question, "False")
        self.feedback(is_right)

    def feedback(self, is_right):
        """
        Give a visual feedback for the user answer
        green for correct/red for incorrect
        """
        if is_right:
            self.canvas.config(bg="green")
            self.update_score()
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.new_question)

    def update_score(self):
        """Update the score with each correct answer"""
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def try_again(self):
        """Reset the quiz with new questions"""
        self.quiz = self.create_questions(self.questions_count)
        self.update_score()
        self.true_btn.config(state="active")
        self.false_btn.config(state="active")
        self.new_question()