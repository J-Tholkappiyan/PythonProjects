import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x600")
root.config(bg="#2C3E50")


choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0


def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    
    if choice == computer_choice:
        result_text = "⚖️ It's a Tie!"
        result_label.config(bg="#F1C40F")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result_text = "🎉 You Win!"
        result_label.config(bg="#27AE60")
        user_score += 1
    else:
        result_text = "😞 Computer Wins!"
        result_label.config(bg="#E74C3C")
        computer_score += 1
    
    
    result_label.config(text=f"You: {choice}  |  Computer: {computer_choice}\n{result_text}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="", bg="#F1C40F")


def exit_game():
    confirm_exit = messagebox.askyesno("Exit Game", "Are you sure you want to exit?")
    if confirm_exit:
        root.quit()


def show_scoreboard():
    messagebox.showinfo("Scoreboard", f"Current Score:\nYou 🏆 {user_score} - Computer 🤖 {computer_score}")


header = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
header.pack(pady=15)


buttons_frame = tk.Frame(root, bg="#2C3E50")
buttons_frame.pack(pady=20)

rock_button = tk.Button(buttons_frame, text="🪨 Rock", font=("Arial", 14), width=10, bg="#3498DB", fg="white", command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(buttons_frame, text="📄 Paper", font=("Arial", 14), width=10, bg="#2ECC71", fg="white", command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(buttons_frame, text="✂️ Scissors", font=("Arial", 14), width=10, bg="#E67E22", fg="white", command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)


result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#F1C40F", fg="black", pady=10, width=40)
result_label.pack(pady=10)


scoreboard_button = tk.Button(root, text="📊 View Scoreboard", font=("Arial", 14, "bold"), bg="#F39C12", fg="white", command=show_scoreboard)
scoreboard_button.pack(pady=10)


actions_frame = tk.Frame(root, bg="#2C3E50")
actions_frame.pack(pady=10)

reset_button = tk.Button(actions_frame, text="Restart Game", font=("Arial", 14, "bold"), bg="#1ABC9C", fg="white", command=reset_game)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(actions_frame, text="Exit Game", font=("Arial", 14, "bold"), bg="#E74C3C", fg="white", command=exit_game)
exit_button.grid(row=0, column=1, padx=10)


root.mainloop()
