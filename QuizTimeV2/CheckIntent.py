quizCategories = (
    "General Knowledge",
    "Goofy Knowledge Check"
) 

def start_quiz():
    print("Quiz")
    startQuiz = "START\n(Yes/No)"
    print(startQuiz)

    startQuizOption = input()

    return startQuizOption

def choose_category():
    print("Choose a category:")
    for i in range(len(quizCategories)):
        print(f"{i+1}. {quizCategories[i]}")

    chosenCategory = input()

    return chosenCategory

def check_progress(counter, halfQuestionMilestone, eightyPctQuestionMilestone, totalQuestions):
    message = ""

    if counter == halfQuestionMilestone:
        message = "Halfway there!"    
    elif counter == eightyPctQuestionMilestone:
        message = "Almost there!"
    elif counter == totalQuestions:
        message = "Quiz is over!"
    
    return message
