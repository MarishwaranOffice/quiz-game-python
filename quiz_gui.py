import tkinter as tk
import random

# ---------------- DATA ----------------
questions = [
    ("Capital of India?", ["Delhi", "Mumbai", "Chennai", "Kolkata"], "Delhi"),
    ("Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("Largest Ocean?", ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),
    ("National Animal of India?", ["Lion", "Tiger", "Elephant", "Leopard"], "Tiger")
]

random.shuffle(questions)

score = 0
q_index = 0
time_left = 10


# ---------------- FUNCTIONS ----------------
def load_question():
    global time_left

    if q_index < len(questions):
        q, options, ans = questions[q_index]

        question_label.config(text=q)

        for i in range(4):
            option_buttons[i].config(text=options[i], state="normal")

        time_left = 10
        update_timer()
    else:
        show_result()


def check_answer(selected):
    global score, q_index

    correct = questions[q_index][2]

    if selected == correct:
        score += 1

    q_index += 1
    load_question()


def update_timer():
    global time_left

    timer_label.config(text=f"Time Left: {time_left}s")

    if time_left > 0:
        time_left -= 1
        root.after(1000, update_timer)
    else:
        next_question()


def next_question():
    global q_index
    q_index += 1
    load_question()


def show_result():
    quiz_frame.pack_forget()
    result_frame.pack()

    result_label.config(text=f"Your Score: {score}/{len(questions)}")


def restart_quiz():
    global score, q_index

    score = 0
    q_index = 0

    result_frame.pack_forget()
    quiz_frame.pack()

    load_question()


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Quiz Game GUI")
root.geometry("500x400")

# -------- QUIZ FRAME --------
quiz_frame = tk.Frame(root)
quiz_frame.pack()

title = tk.Label(quiz_frame, text="Quiz Game", font=("Arial", 20))
title.pack(pady=10)

timer_label = tk.Label(quiz_frame, text="Time Left: 10s", font=("Arial", 12))
timer_label.pack()

question_label = tk.Label(quiz_frame, text="", font=("Arial", 16))
question_label.pack(pady=20)

option_buttons = []

for i in range(4):
    btn = tk.Button(quiz_frame, text="", width=20,
                    command=lambda i=i: check_answer(option_buttons[i].cget("text")))
    btn.pack(pady=5)
    option_buttons.append(btn)

# -------- RESULT FRAME --------
result_frame = tk.Frame(root)

result_label = tk.Label(result_frame, text="", font=("Arial", 18))
result_label.pack(pady=20)

restart_btn = tk.Button(result_frame, text="Play Again", command=restart_quiz)
restart_btn.pack()

exit_btn = tk.Button(result_frame, text="Exit", command=root.quit)
exit_btn.pack(pady=10)

# ---------------- START ----------------
load_question()

root.mainloop()
