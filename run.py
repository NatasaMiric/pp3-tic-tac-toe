board = [' ']*9


def display_board(board):
    """
    Displays the board.

    Parameters:
    -----------
    board : list of int
        List of numbers from 0 to 8.
    """

    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


def run_game():

    while not is_board_full():
        display_board(board)        
        user_input = input("\nPlease enter a number (1-9): ")
        user_input = int(user_input)
        board[user_input - 1] = 'X'


def is_board_full():
    """
    Checks if the board has empty cells and returns True, otherwise False.
    """
    for value in board:
        if value == ' ':
            return False
    return True


run_game()    