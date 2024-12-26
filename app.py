import tkinter as tk
import random

def check_guess():
    try:
        user_guess = int(guess_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    if user_guess < number_to_guess:
        result_label.config(text="Too low! Try again.")
    elif user_guess > number_to_guess:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Correct! The number was {number_to_guess}.")
        guess_button.config(state=tk.DISABLED)
        play_again_button.pack(pady=10)

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 10)
    result_label.config(text="Guess a number between 1 and 10")
    guess_button.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)
    play_again_button.pack_forget()

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Random number to guess
number_to_guess = random.randint(1, 10)

# Widgets
description_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14))
description_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Check Guess", font=("Helvetica", 14), command=check_guess)
guess_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 14), command=reset_game)

# Start the game
root.mainloop()