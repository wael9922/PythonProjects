question_data = [
	{"text": "A slug's blood is green.", "answer": "True"},
	{"text": "The loudest animal is the African Elephant.", "answer": "False"},
	{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
	{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
	{"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
			 " you are free to take it home to eat.", "answer": "True"},
	{"text": "In London, UK, if you happen to die in the House of Parliament, "
			 "you are entitled to a state funeral.", "answer": "False"},
	{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
	{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
	{"text": "Google was originally called 'Backrub'.", "answer": "True"},
	{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
	{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
	{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
	"""A blueprint for a questions"""
	def __init__(self, q_text, q_answer):
		self.text = q_text
		self.answer = q_answer


class Quiz:
	"""Quiz of True/False questions class"""

	def __init__(self, questions_list):
		self.question_number = 0
		self.questions_list = questions_list
		self.score = 0

	def  next_question(self):
		"""Start the quiz move through the questions bank"""
		current_question = self.questions_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
		self.check_answer(current_question.answer, user_answer)
		print(f"Your current score is: {self.score}/{self.question_number}")
		print("")

	def still_has_questions(self):
		"""Checks if there is any question left"""
		return self.question_number < len(self.questions_list)

	def check_answer(self,correct_answer, user_answer):
		"""Checks the user answer"""
		if correct_answer.lower() == user_answer.lower():
			self.score += 1
			print("That's right!")
		else:
			print("That's wrong!")
		print(f"The correct answer is {correct_answer}")


question_bank = []
for question in question_data:
	question_bank.append(Question(question['text'], question['answer']))

quiz = Quiz(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

