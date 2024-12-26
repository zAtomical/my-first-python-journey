#quiz game
from CheckIntent import start_quiz
from QuizTuples import questions, answers

while True:
    score = 0
    counter =0
    Begin = start_quiz()
    
    if Begin.lower() == "yes":

        for question in questions:
            if (counter+1 == questions.__len__()):
                print("Last Question:")
            else:
                print(f"Question {counter+1}:")

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
