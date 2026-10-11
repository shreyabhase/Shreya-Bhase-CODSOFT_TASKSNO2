
import math

# Create an empty board
board = [" " for _ in range(9)]


# Display the game board
def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check whether the board is full
def is_draw():
    return " " not in board


# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# Find the computer's best move
def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        print("Computer chose position:", best_move + 1)


# Main game
def play_game():
    print("===== TIC-TAC-TOE AI =====")
    print("You are X | Computer is O")
    print("Choose positions from 1 to 9.")
    print("Position layout:")

    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        display_board()

        # Human player's turn
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid position! Choose 1 to 9.")
                continue

            if board[position - 1] != " ":
                print("That position is already occupied!")
                continue

            board[position - 1] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        if check_winner("X"):
            display_board()
            print("Congratulations! You win!")
            break

        if is_draw():
            display_board()
            print("It's a draw!")
            break

        # Computer's turn
        computer_move()

        if check_winner("O"):
            display_board()
            print("Computer wins! Better luck next time.")
            break

        if is_draw():
            display_board()
            print("It's a draw!")
            break

    print("===== GAME OVER =====")


# Start the game
play_game()
