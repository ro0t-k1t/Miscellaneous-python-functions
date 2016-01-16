__author__ = 'ronanpiercehiggins'

import difflib

def open_and_write():
    f = open('quizquestions', 'w')

    for counter in range(3):
        question = raw_input("Please enter your %sst question:" % (counter + 1))
        answer = raw_input("Please enter the %sst answer:" % (counter + 1))
        f.write(question)
        f.write("\n")
        f.write(answer)
        f.write("\n")
        f.flush()


    f.close()

def prepare_quiz():
    questions, answers = [], []
    with open('quizquestions') as f:
        for i, line in enumerate(f):
            answers.append(line.strip()) if i % 2 else questions.append(line)

    return zip(questions, answers)



def initiate_quiz():
    open_and_write()
    questions = prepare_quiz()
    score = 0
    guesses_left = 3
    total = len(questions)
    for question, answer in questions:
        while guesses_left:
            guess = raw_input(question)
            seq=difflib.SequenceMatcher(None, guess,answer)
            d=seq.ratio()*100
            if d > 80:
                print "Correct answer. Here is the next question"
                score += 1
                guesses_left = 3
                break
            elif d < 80:
                print "Wrong answer try again!"
                guesses_left -= 1
                print "Guesses left: %s" % guesses_left
                if guesses_left == 0:
                    print "Game Over"
                    break
                    print 'You got %s out of %s questions right' % (score, total)

    print 'You got %s out of %s questions right' % (score, total)





initiate_quiz()


