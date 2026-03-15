# Quiz Game Project
# Author: Mari Paramasivam S

import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

score = 0
total_questions = 0


def loading(text):
    print(text, end="", flush=True)
    for i in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")


def progress(current, total):
    percent = int((current / total) * 20)
    bar = "█" * percent + "-" * (20 - percent)
    print(f"[{bar}] {current}/{total}")


def general_knowledge_quiz():

    global score
    global total_questions

    questions = [

        ("What is the capital of India?", "delhi"),
        ("Which planet is known as Red Planet?", "mars"),
        ("Who developed Python language?", "guido van rossum"),
        ("Largest ocean in world?", "pacific"),
        ("National animal of India?", "tiger"),
        ("Fastest land animal?", "cheetah"),
        ("How many continents exist?", "7"),
        ("Gas plants absorb?", "carbon dioxide"),
        ("Who wrote Romeo and Juliet?", "shakespeare"),
        ("Country famous for pyramids?", "egypt"),

        ("Tallest mountain?", "everest"),
        ("Largest desert?", "sahara"),
        ("Closest planet to sun?", "mercury"),
        ("Who discovered gravity?", "newton"),
        ("Land of rising sun?", "japan"),
        ("Largest mammal?", "blue whale"),
        ("Longest river?", "nile"),
        ("Inventor of telephone?", "alexander graham bell"),
        ("Metal liquid at room temperature?", "mercury"),
        ("Capital of France?", "paris"),

        ("Currency of Japan?", "yen"),
        ("King of jungle?", "lion"),
        ("Boiling point of water?", "100"),
        ("Country famous for pizza?", "italy"),
        ("India located in which continent?", "asia"),
        ("Largest bird?", "ostrich"),
        ("Language used for web apps?", "javascript"),
        ("Animal with longest neck?", "giraffe"),
        ("Biggest planet?", "jupiter"),
        ("Painter of Mona Lisa?", "da vinci"),

        ("Gas used in balloons?", "helium"),
        ("Country famous for kangaroo?", "australia"),
        ("Smallest ocean?", "arctic"),
        ("Device that measures temperature?", "thermometer"),
        ("National bird of India?", "peacock"),
        ("Planet with rings?", "saturn"),
        ("Ship of desert animal?", "camel"),
        ("Currency of USA?", "dollar"),
        ("Largest continent?", "asia"),
        ("Vitamin from sunlight?", "vitamin d")

    ]

    # repeat list to exceed 150 questions
    questions = questions * 4

    random.shuffle(questions)

    total_questions = len(questions)

    print(Fore.YELLOW + "\nGeneral Knowledge Quiz\n")

    for i, (question, answer) in enumerate(questions, 1):

        print(Fore.CYAN + f"\nQuestion {i}")

        user = input(question + " ").strip().lower()

        if user == answer:
            print(Fore.GREEN + "Correct Answer")
            score += 1
        else:
            print(Fore.RED + "Wrong Answer")
            print("Correct:", answer)

        progress(i, total_questions)


def math_quiz():

    global score
    global total_questions

    total_questions = 350

    operations = ["+", "-", "*"]

    print(Fore.YELLOW + "\nMathematics Quiz (350 Questions)\n")

    for i in range(1, total_questions + 1):

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        op = random.choice(operations)

        if op == "+":
            correct = num1 + num2
        elif op == "-":
            correct = num1 - num2
        else:
            correct = num1 * num2

        print(Fore.CYAN + f"\nQuestion {i}")

        try:
            user = int(input(f"What is {num1} {op} {num2}? "))
        except:
            user = None

        if user == correct:
            print(Fore.GREEN + "Correct Answer")
            score += 1
        else:
            print(Fore.RED + "Wrong Answer")
            print("Correct:", correct)

        progress(i, total_questions)


def show_result():

    print(Fore.MAGENTA + "\n========================")
    print("Quiz Completed")

    print("Score:", score, "/", total_questions)

    percent = (score / total_questions) * 100

    print("Percentage:", round(percent, 2), "%")

    if percent >= 80:
        print(Fore.GREEN + "Excellent")
    elif percent >= 50:
        print(Fore.YELLOW + "Good Job")
    else:
        print(Fore.RED + "Keep Practicing")

    print("========================\n")


def start_quiz():

    global score
    global total_questions

    score = 0
    total_questions = 0

    loading("Starting Quiz")

    print(Fore.BLUE + "==============================")
    print("        QUIZ GAME PROJECT     ")
    print("==============================\n")

    print("1. General Knowledge Quiz (150+)")
    print("2. Mathematics Quiz (350 Auto Questions)")

    choice = input("\nEnter choice: ")

    if choice == "1":
        general_knowledge_quiz()

    elif choice == "2":
        math_quiz()

    else:
        print("Invalid choice")
        return

    show_result()


def main():

    while True:

        start_quiz()

        again = input("Play again? (yes/no): ").lower()

        if again != "yes":

            loading("Closing Game")

            print("Thank you for playing Quiz Game")

            break


main()
