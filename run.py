import random

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
            print("\nInput must be a number between 1 and 9.\n")
            continue
        
        user_input = int(user_input) 

        if user_input_between_one_and_nine(user_input) is False:
            print("\nYour input number is not between 1 and 9.\n")
            continue           
        
        if is_cell_empty(board[user_input - 1]) is False:
            print("\nThis place is already taken. Choose another spot.\n")
            continue
        board[user_input - 1] = 'X'
        computer_input = generate_computer_input()


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


def is_cell_empty(board_location):
    """
    Returns an empty string if cell in the board is empty.

    Parameters:
    -----------   
    board_location : string
        The string which gets returned.
    """
    return board_location == ' '


def generate_computer_input():
    """
    Generate and return a random number.

    The value is between 1 and 9.

    Returns:
    --------
    computer_input : int
        Random number generated.
    """
    computer_input = random.randint(1, 9)
    if not is_board_full():
        if not board[int(computer_input - 1)] in {'X', 'O'}:
            board[computer_input - 1] = 'O'
        else:
            computer_input = generate_computer_input()
    return computer_input


run_game()
