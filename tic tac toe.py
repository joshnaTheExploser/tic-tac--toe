import tkinter as tk

def on_click(button, index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        button.config(text=current_player, fg="red" if current_player == "X" else "blue")

        if check_winner(current_player):
            update_score(current_player)
            show_result(f"Game Over!\nPlayer {current_player} has won the match", "maroon")
            reset_board()

        elif " " not in board:
            show_result("It's a draw!", "green")
            reset_board()

        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Player {current_player}'s Turn")

def check_winner(player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def reset_board():
    global board, current_player
    board = [" "] * 9
    for button in buttons:
        button.config(text=" ", fg="black")
    current_player = "X"
    status_label.config(text=f"Player {current_player}'s Turn")

def update_score(player):
    if player == "X":
        scores["X"] += 1
        score_x_label.config(text=f"Player X: {scores['X']}")
    else:
        scores["O"] += 1
        score_o_label.config(text=f"Player O: {scores['O']}")

def show_result(message, color):
    result_window = tk.Toplevel(window)
    result_window.title("Match Result")
    result_window.configure(bg="white")
    result_window.resizable(False, False)

    result_label = tk.Label(result_window, text=message, font=('Arial', 18, 'bold'), fg=color, bg="white")
    result_label.pack(padx=20, pady=20)

    ok_button = tk.Button(result_window, text="OK", font=('Arial', 14), command=result_window.destroy)
    ok_button.pack(pady=10)

# Initialize
window = tk.Tk()
window.title("Tic Tac Toe")

board = [" "] * 9
current_player = "X"
scores = {"X": 0, "O": 0}

# Status label
status_label = tk.Label(window, text=f"Player {current_player}'s Turn", font=('Arial', 20))
status_label.grid(row=0, column=0, columnspan=3)

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=('Arial', 40), width=5, height=2)
    button.grid(row=(i // 3) + 1, column=i % 3)
    button.config(command=lambda b=button, i=i: on_click(b, i))
    buttons.append(button)

# Scoreboard
score_x_label = tk.Label(window, text=f"Player X: {scores['X']}", font=('Arial', 16))
score_x_label.grid(row=4, column=0)

score_o_label = tk.Label(window, text=f"Player O: {scores['O']}", font=('Arial', 16))
score_o_label.grid(row=4, column=2)

# Restart button
restart_button = tk.Button(window, text="Restart Game", font=('Arial', 14), command=reset_board)
restart_button.grid(row=4, column=1)

window.mainloop()