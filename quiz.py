__author__ = 'ronanpiercehiggins'

import sys


def get_questions():
    questions, answers = [], []
    with open('questions.txt') as f:
        for i, line in enumerate(f):
            answers.append(line.strip()) if i % 2 else questions.append(line)

    return zip(questions, answers)
try:
    questions = get_questions()
except:
    print 'Questions file not found.'
    sys.exit()


score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s out of %s questions right' % (score, total)


