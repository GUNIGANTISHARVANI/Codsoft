import random

# Define constants for the players
PLAYER_X = 'X'  # Human player
PLAYER_O = 'O'  # AI player

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("--------")
    print()

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw condition)
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    # Check if game has ended (either win or draw)
    if check_winner(board, PLAYER_X):
        return -10 + depth  # Human wins
    if check_winner(board, PLAYER_O):
        return 10 - depth  # AI wins
    if is_board_full(board):
        return 0  # Draw
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '  # Undo move
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '  # Undo move
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_score = float('-inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = PLAYER_O
            score = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '  # Undo move
            if score > best_score:
                best_score = score
                move = i
    return move

# Function for human move (player X)
def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("This spot is already taken. Choose another spot.")
        except (ValueError, IndexError):
            print("Invalid move! Enter a number between 1 and 9.")

# Main game loop
def play_game():
    board = [' '] * 9  # Initialize an empty board
    print_board(board)
    
    while True:
        # Human (player X) turn
        print("Your turn (Player X):")
        move = human_move(board)
        board[move] = PLAYER_X
        print_board(board)
        
        if check_winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        # AI (player O) turn
        print("AI's turn (Player O):")
        move = best_move(board)
        board[move] = PLAYER_O
        print_board(board)
        
        if check_winner(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
