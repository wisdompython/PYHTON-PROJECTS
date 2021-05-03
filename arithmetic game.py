import random, time
class arithmetic_game:
    def __init__(self, num_questions):
        self.num_questions = num_questions
    def generate_questions(self):
        operand_1 = random.randint(1,30)
        operand_2 = random.randint(1,30)
        operator = random.choice(['+', '-', '//', '*'])
        if operator == '+':
            answer = operand_1 + operand_2
        if operator == '-':
            answer = operand_1 - operand_2
        if operator == '//':
            answer = operand_1 // operand_2
        if operator == '*':
            answer = operand_1 * operand_2
        question = str(operand_1)  + ' ' + operator + ' ' + str(operand_2)
        return question, answer
    def play_game(self):
        num_correct = 0
        start_time = time.time()
        for i in range(self.num_questions):
            print('Question' + str(i+1) + ':')
            question, answer = self.generate_questions()
            print(question)
            user_answer = int(input('what is your answer? '))
            if user_answer == answer:
                num_correct = num_correct + 1
                print('you are correct')
            else:
                print('you are wrong. The answer is ' + str(answer))
        end_time = time.time()
        print('You got ' + str(num_correct) + ' answers correct')
        print(' you used {0:.3f} seconds'.format(end_time - start_time))

new_game = arithmetic_game(10)
new_game.play_game()

