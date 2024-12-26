def start_quiz():
    print("Quiz")
    BeginA = "START\n(Yes/No)"
    print(BeginA)
    
    return input()

def check_progress(counter, qr, qrr, total_questions):
    message = ""

    if counter == qr:
        message = "Halfway there!"
    elif counter == qrr:
        message = "Almost there!"
    elif counter == total_questions:
        message = "Quiz is over!"

    return message
