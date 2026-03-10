# Quiz Game Project
# Author: Mari Paramasivam S

import random

score = 0
total_questions = 0


def general_knowledge_quiz():
    global score
    global total_questions

    questions = {
        "What is the capital of India? ": "delhi",
        "Which planet is known as the Red Planet? ": "mars",
        "Who developed Python programming language? ": "guido van rossum",
        "Which is the largest ocean in the world? ": "pacific",
        "What is the national animal of India? ": "tiger",
        "How many continents are there on Earth? ": "7",
        "Which gas do plants absorb from the atmosphere? ": "carbon dioxide",
        "Who wrote Romeo and Juliet? ": "shakespeare",
        "Which country invented paper? ": "china",
        "What is the fastest land animal? ": "cheetah"
    }

    print("\nGeneral Knowledge Quiz\n")

    for question, answer in questions.items():

        user = input(question).strip().lower()

        if user == answer:
            print("Correct Answer\n")
            score += 1
        else:
            print("Wrong Answer")
            print("Correct Answer:", answer, "\n")

        total_questions += 1


def python_quiz():
    global score
    global total_questions

    questions = {
        "Which keyword is used to define a function in Python? ": "def",
        "Which symbol is used for comments in Python? ": "#",
        "Which data type stores multiple values? ": "list",
        "Which loop runs while the condition is true? ": "while",
        "What is the file extension of Python files? ": ".py",
        "Which function is used to display output? ": "print",
        "Which keyword is used to create a class? ": "class",
        "Which function is used to take user input? ": "input",
        "Which data type stores True or False values? ": "bool",
        "Which operator is used for equality comparison? ": "=="
    }

    print("\nPython Quiz\n")

    for question, answer in questions.items():

        user = input(question).strip().lower()

        if user == answer:
            print("Correct Answer\n")
            score += 1
        else:
            print("Wrong Answer")
            print("Correct Answer:", answer, "\n")

        total_questions += 1


def math_quiz():
    global score
    global total_questions

    print("\nMathematics Quiz (350 Questions)\n")

    operations = ["+", "-", "*"]

    for i in range(350):

        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        op = random.choice(operations)

        if op == "+":
            correct = num1 + num2
        elif op == "-":
            correct = num1 - num2
        else:
            correct = num1 * num2

        print("Question", i + 1)

        try:
            user = int(input(f"What is {num1} {op} {num2}? "))
        except:
            user = None

        if user == correct:
            print("Correct Answer\n")
            score += 1
        else:
            print("Wrong Answer")
            print("Correct Answer:", correct, "\n")

        total_questions += 1


def show_result():
    print("\n=================================")
    print("Quiz Completed")
    print("Your Score:", score, "/", total_questions)

    if total_questions > 0:
        percentage = (score / total_questions) * 100
    else:
        percentage = 0

    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Excellent Performance")
    elif percentage >= 50:
        print("Good Job")
    else:
        print("Keep Practicing")

    print("=================================\n")


def main():

    print("=================================")
    print("         QUIZ GAME PROJECT       ")
    print("=================================")

    print("Choose Quiz Category")
    print("1. General Knowledge")
    print("2. Python")
    print("3. Mathematics (350 Questions)")

    choice = input("Enter your choice: ")

    if choice == "1":
        general_knowledge_quiz()

    elif choice == "2":
        python_quiz()

    elif choice == "3":
        math_quiz()

    else:
        print("Invalid option")
        return

    show_result()


main()
