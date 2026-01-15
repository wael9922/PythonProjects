class QuizBrain:
    """Build the Quiz Logic"""
    def __init__(self, questions):
        self.question_number = 0
        self.questions_bank = questions
        self.score = 0
        self.current_question = None

    def next_question(self):
        """Move on to the next question"""
        if self.any_question_left():
            self.current_question = self.questions_bank[self.question_number]
            self.question_number += 1
            return  self.current_question.question
            # self.check_answer(current_question, ask)
        else:
            return "Quiz is Over"

    def check_answer(self, current_question, user_answer):
        """Check if user answered correctly"""
        if current_question.answer==user_answer:
            self.score += 1
            return True
        else:
            return False

    def any_question_left(self):
        """check if there is still questions left"""
        return self.question_number < len(self.questions_bank)
