import tkinter as tk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import simpledialog

# ---------------- BANDIT SETUP ----------------
k = 3
counts = [0]*k
values = [0.0]*k
epsilon = 0.3

delays = [1500, 900, 500]
labels = ["Easy", "Medium", "Hard"]

# ---------------- GAME STATE ----------------
running = False
start_time = 0
score = 0
high_score = 0

total_reward = 0
steps = 0
avg_rewards = []
selection_counts = [0]*k

# ---------------- FILE ----------------
FILE = "scores.txt"

# ---------------- BANDIT ----------------
def select_arm():
    if random.random() < epsilon:
        return random.randint(0, k-1)
    return values.index(max(values))

def update(arm, reward):
    counts[arm] += 1
    selection_counts[arm] += 1
    n = counts[arm]
    values[arm] += (1/n) * (reward - values[arm])

# ---------------- LEADERBOARD ----------------
def save_score():
    global score
    name = simpledialog.askstring("Name", "Enter your name:")
    if not name:
        name = "Player"

    with open(FILE, "a") as f:
        f.write(f"{name},{score}\n")

    show_leaderboard()

def show_leaderboard():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
    except:
        data = []

    scores = []
    for line in data:
        parts = line.strip().split(",")
        if len(parts) == 2:
            name, sc = parts
            scores.append((name, int(sc)))

    scores.sort(key=lambda x: x[1], reverse=True)

    text = "🏆 Leaderboard 🏆\n\n"
    for i, (name, sc) in enumerate(scores[:5], start=1):
        text += f"{i}. {name} - {sc}\n"

    leaderboard_label.config(text=text)

# ---------------- GAME ----------------
def start_game():
    global running, score
    running = True
    score = 0
    status.config(text="Game Started!")
    start_round()

def stop_game():
    global running
    running = False
    status.config(text="Game Stopped")
    target.place_forget()
    save_score()

def start_round():
    global current_arm

    if not running:
        return

    current_arm = select_arm()
    status.config(text=f"{labels[current_arm]} Mode | Get Ready...")

    target.place_forget()
    countdown(3)

def countdown(n):
    if not running:
        return

    if n > 0:
        status.config(text=f"Starting in {n}...")
        root.after(500, lambda: countdown(n-1))
    else:
        show_target()

def show_target():
    global start_time

    if not running:
        return

    status.config(text="CLICK NOW!")

    x = random.randint(20, 220)
    y = random.randint(20, 220)

    target.place(in_=play_area, x=x, y=y)
    start_time = time.time()

# ✅ FIXED FUNCTION
def click_target():
    global score, high_score, total_reward, steps

    if not running:
        return

    reaction_time = time.time() - start_time
    target.place_forget()

    # ✅ ALWAYS GIVE REWARD
    reward = max(1, int(3 - reaction_time))

    update(current_arm, reward)

    score += reward * 10
    if score > high_score:
        high_score = score

    total_reward += reward
    steps += 1
    avg_rewards.append(total_reward / steps)

    # ✅ FEEDBACK
    if reaction_time < 0.4:
        feedback = "🔥 Excellent!"
    elif reaction_time < 1.0:
        feedback = "👍 Good!"
    elif reaction_time < 2.5:
        feedback = "🙂 Slow"
    else:
        feedback = "🐢 Too Slow!"

    info.config(
        text=f"{feedback} | Reaction: {reaction_time:.2f}s | Score: {score} | High Score: {high_score}"
    )

    update_graph()
    root.after(800, start_round)

# ---------------- GRAPH ----------------
def update_graph():
    ax1.clear()
    ax2.clear()

    ax1.plot(avg_rewards)
    ax1.set_title("Learning Curve")

    ax2.bar(labels, selection_counts)
    ax2.set_title("Difficulty Usage")

    canvas.draw()

# ---------------- UI ----------------
root = tk.Tk()
root.title("🔥 AI Reaction Game + Leaderboard")
root.geometry("550x750")
root.configure(bg="#1e1e2f")

tk.Label(root, text="AI Reaction Trainer", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

status = tk.Label(root, text="Press Start", font=("Arial", 14),
                  bg="#1e1e2f", fg="#00ffcc")
status.pack()

info = tk.Label(root, text="", font=("Arial", 12),
                bg="#1e1e2f", fg="white")
info.pack()

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Button(frame, text="Start ▶️", command=start_game,
          bg="#00cc66", fg="white", width=10).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Stop ⏹️", command=stop_game,
          bg="#cc3333", fg="white", width=10).grid(row=0, column=1, padx=5)

play_area = tk.Frame(root, width=300, height=300, bg="#2e2e3e")
play_area.pack(pady=10)

target = tk.Button(play_area, text="🎯", font=("Arial", 16),
                   bg="#ffcc00", command=click_target)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4,5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

leaderboard_label = tk.Label(root, text="🏆 Leaderboard 🏆",
                             font=("Arial", 12),
                             bg="#1e1e2f", fg="white")
leaderboard_label.pack(pady=10)

root.mainloop()
