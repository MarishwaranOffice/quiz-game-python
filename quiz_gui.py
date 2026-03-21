import tkinter as tk
from tkinter import messagebox
import random

score = 0
question_index = 0

questions = [
    ("Capital of India?", "delhi"),
    ("Red planet?", "mars"),
    ("Largest ocean?", "pacific"),
    ("National animal of India?", "tiger")
]

random.shuffle(questions)


def check_answer():
    global score, question_index

    user = entry.get().lower()

    if user == questions[question_index][1]:
        score += 1

    question_index += 1
    entry.delete(0, tk.END)

    if question_index < len(questions):
        question_label.config(text=questions[question_index][0])
    else:
        messagebox.showinfo("Result", f"Your Score: {score}/{len(questions)}")
        root.quit()


# GUI Window
root = tk.Tk()
root.title("Quiz Game GUI")
root.geometry("400x300")

title = tk.Label(root, text="Quiz Game", font=("Arial", 18))
title.pack(pady=10)

question_label = tk.Label(root, text=questions[0][0], font=("Arial", 14))
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.pack(pady=10)

root.mainloop()
