def print_board(board):
    """Helper function to print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Check if there's a winner."""
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
            
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9): 
        print_board(board)
        print(f"Player {current_player}, enter your move from 0 to 2 with a space between the numbers(row and column): ")
        
        while True:
            try:
                row, col = map(int, input().split())
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("This position is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers from 0 to 2.")
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
    
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()