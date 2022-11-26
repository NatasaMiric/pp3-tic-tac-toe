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
        if user_input.isnumeric() is False:
            print("\nInput must be a number between 1 and 9\n")
            continue
        
        user_input = int(user_input) 
        if user_input_between_one_and_nine(user_input) is False:
            print("\nYour input number is not between 1 and 9.\n")
            continue           
        board[user_input - 1] = 'X'


def is_board_full():
    """
    Checks if the board has empty cells and returns True, otherwise False.
    """
    for value in board:
        if value == ' ':
            return False
    return True


def user_input_between_one_and_nine(user_input):
    """
    Returns True if user inputs a valid number.

    Parameters:
    -----------
    user_input : int
        User input from 1 to 9.
    """    
    if 1 <= user_input <= 9:
        return True
    return False


run_game()
