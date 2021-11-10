class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    # TODO: asking the question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = (input(f"Q{self.question_number}: {current_question.text} (True/ False): ")).lower()
        self.check_answer(user_answer, current_question.answer)

    # TODO: checking if we are the end of the quiz

    def still_has_question(self, q_list):
        return self.question_number < len(self.question_list)

    # TODO: checking if the answer is correct

    def check_answer(self, user_name, correct_name):
        if user_name == correct_name.lower():
            self.score += 1
            print("You got it right.")
        else:
            self.score += 0
            print("Sorry your wrong.")
        print(f"The correct answer: {correct_name}.\n Your current score: {self.score}/{self.question_number} \n")


