def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board) - i - 1] == board[0][len(board) - 1] and board[i][len(board) - i - 1] != ' ' for i in range(len(board))):
        return True

    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get player move
        row = int(input(f"Enter row (0, 1, or 2) for {current_player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for {current_player}: "))

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"{current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_tic_tac_toe()
