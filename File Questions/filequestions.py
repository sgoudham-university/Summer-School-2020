def read_in_files(quiz_dict):
    """Save questions and answers into a dict"""

    with open(r'questions.txt', 'r') as file:
        # Read in lines
        lines = file.read().split("\n")
        # Store every question and answer within a dictionary
        for line in lines:
            data = line.split(',')
            quiz_dict[data[0].strip()] = data[1].strip()


def check_answer(answer, value):
    """Check answers, if they're wrong or right"""

    # Count wrong and correct answers
    # Boolean variable to detect whether answer was wrong or right
    if answer.lower() == value.lower():
        print("Well Done! You got this question right!\n")
        is_correct = True
    else:
        print(f"Oh no! You were wrong! The correct answer was {value}\n")
        is_correct = False

    return is_correct


def show_quiz(quiz_dict, score):
    """Quiz the player based on the questions read in"""

    question_num = 1

    # Iterate through the dictionary while asking the user questions
    # Increment the score if the user got the correct answer
    # When no user input has been retrieved, question is skipped
    for key, value in quiz_dict.items():
        user_answer = input(f"Question {question_num}: {key}\n")
        if user_answer:
            if check_answer(user_answer, value):
                score += 1
        else:
            print("Question Skipped!\n")
        question_num += 1

    # Print the results of the quiz
    print(f"\nYou have completed the quiz!"
          f"\nYour Total Score {score}/{len(quiz_dict)}")


def main():
    """Read in questions and quiz the player"""

    quiz_dict = {}
    score = 0

    read_in_files(quiz_dict)
    show_quiz(quiz_dict, score)


# Execute main method
main()
