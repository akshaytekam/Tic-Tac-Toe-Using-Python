import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " |", end="")
        print()
        print("-------------")

# Function to check if someone has won
def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to play a single game
def play_game():
    # Initialize the board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    turn = 0
    
    # Play the game
    while True:
        print_board(board)
        print("It's player " + players[turn] + "'s turn.")
        
        # Get the player's move
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        
        # Make the move
        if board[row][col] != " ":
            print("That space is already taken!")
        else:
            board[row][col] = players[turn]
            if check_win(board, players[turn]):
                print_board(board)
                print("Player " + players[turn] + " wins!")
                return
            
            # Check for a tie
            if all([space != " " for row in board for space in row]):
                print_board(board)
                print("It's a tie!")
                return
            
            # Switch to the other player
            turn = (turn + 1) % 2

# Main function to play multiple games
def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            break

# Call the main function to start the game
main()
