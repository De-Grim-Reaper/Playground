def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for keys in questions:
        print("------------------------------------")
        print(keys)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A,B,C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(keys), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")

    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guesses/len(questions))*100)
    print()
    print("Your Score is: "+str(score)+"%")


def play_again():
    response = input("Play again? (Yes/No): ").capitalize()
    if response == "Yes":
        return True
    else:
        return False


# -----------------------

questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python was tributed to what comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print()
print("Thanks for playing!!!")
