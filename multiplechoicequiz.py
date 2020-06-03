from question import Question #import the Question class from the question.py file

#array to hold the questions for the multiple choice quiz
question_prompts = [ 
"\nWhat is 5 + 4?\n (a) 9\n (b) 20\n (c) 15\n\n",
"\nWhat is 8 / 2?\n (a) 2\n (b) 1\n (c) 4\n\n",
"\nWhat is 10 * 5?\n (a) 15\n (b) 50\n (c) 30\n\n",
"\nWhat is 5 / 0?\n (a) Undefined\n (b) 0\n (c) 1\n\n"
]

#list to hold the classes for the question and correct answer
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),       
]

#function to run the test
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\nAnswer: ")
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " questions correct")

#function call to run_test function
run_test(questions)