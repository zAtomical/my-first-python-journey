#quiz game
from CheckIntent import start_quiz, check_progress, choose_category
from GoofyTuple import questions as goofy_questions
from GoofyTuple import answers as goofy_answers
from GKTuple import questions as gk_questions
from GKTuple import questions as gk_answers

while True:

    score = 0
    counter = 0
    questions = []
    answers = []

    chosenCat = choose_category()
    
    if chosenCat == "1":
        questions = gk_questions
        answers = gk_answers
    elif chosenCat == "2":
        questions = goofy_questions
        answers = goofy_answers 
    else :
        questions = goofy_questions
        answers = goofy_answers
    
    halfQuestionMilestone = (questions.__len__())//2
    eightyPctQuestionMilestone = ((questions.__len__())*8)//10

    begin = start_quiz()

    if begin.lower() == "yes":
        message = ""
        isLastQuestion = False

        for question in questions:
            if (counter+1 == questions.__len__()):
                isLastQuestion = True
                message = "Hurray! You've reached the last question.."
            else:
                print(f"Question {counter+1}:")
            
            if isLastQuestion:
                print(message)
            else:
                message = check_progress(counter, halfQuestionMilestone, eightyPctQuestionMilestone, questions.__len__())
                if message != "":
                    print(message)

            print(question)

            answer = input()
            if answer.lower() == answers[counter]:
                print("Good Job!")
                score += 1
            else:
                print("Wrong")
            counter +=1

        end = f"Your score: {score}"
        print(end)
    else :
        print("ok")

    restart = input("Do you want to play again? (Yes/No): ")
    if restart.lower() != "yes":
        break


