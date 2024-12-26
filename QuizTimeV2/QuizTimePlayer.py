#quiz game
from CheckIntent import start_quiz, check_progress
from QuizTuples import questions, answers

while True:
    score = 0
    counter = 0
    qr = (questions.__len__())//2
    qrr = ((questions.__len__())*8)//10

    Begin = start_quiz()
    
    if Begin.lower() == "yes":
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
                message = check_progress(counter, qr, qrr, questions.__len__())
                if message != "":
                    print(message)

            print(question)

            Answer = input()
            if Answer.lower() == answers[counter]:
                print("Good Job!")
                score += 1
            else:
                print("Wrong")
            counter +=1

        End = f"Your score: {score}"
        print(End)
    else :
        print("ok")

    restart = input("Do you want to play again? (Yes/No): ")
    if restart.lower() != "yes":
        break


