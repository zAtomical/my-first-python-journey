#quiz game
score = 0
while True:
    print("Quiz")
    BeginA= "START\n(Yes/No)"
    print(BeginA)

    Begin = input()

    
    if Begin.lower() == "yes":
        print("Question 1:")
        print("Is Australia Real?")
        Answer1 = input()
        if Answer1.lower() == "yes":
            print("Good Job!")
            #score = score + 1
            score += 1
        else:
            print("Wrong")

        print("Question 2:")
        print("Am I cool?")
        Answer2 = input()

        if Answer2.lower() == "yes":
            print("Good Job")
            #score = score+1
            score += 1
        else:
            print("wrong")

        print("Last Question:")
        print("AmongUs or Fortnite")
        Answer3 = input()

        if Answer3.lower() == "amongus":
            print("Good Job!")
            score += 
        else:
            print("Wrong")

        End = f"Your score: {score}"

        print(End)
    else :
        print("ok")

    restart = input("Do you want to play again? (Yes/No): ")
    if restart.lower() != "yes":
        break
