""" Generates random number """
import random
import os

board = [' ']*9
user_selection = []
computer_selection = []

WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]


def display_board():
    """
    Displays the board.
    """
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


def run_game():
    """
    This is a function that runs the game until the board is full.

    Gets user and computer input and checks if it is a valid and if not
    displays error messages.

    After each move calls for check win and check tie function.
    """
    while not is_board_full():
        display_board()
        try:
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
            user_selection.append(user_input)
            if check_game():
                break
            computer_input = generate_computer_input()
            computer_selection.append(computer_input)
            if check_game():
                break
            clear_screen()
        except ValueError:
            print("\nInvalid input. Please try again\n")
    print("Thank you for playing!\n")
    display_board()


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


def check_win():
    """
    Returns True if the player wins the game.
    """
    computer_selection.sort()
    user_selection.sort()
    if any([set(w).issubset(set(computer_selection))
           for w in WIN_COMBINATIONS]):
        print("\n*** Game over ***\n")
        print("Your opponent beat you!\n")
        return True
    if any([set(w).issubset(set(user_selection)) for w in WIN_COMBINATIONS]):
        print("\n*** Congratulations ***\n")
        print("You are the WINNER!\n")
        return True
    return False


def check_tie():
    """
    Returns True if it'a tie.
    """
    if is_board_full() and not check_win():
        print("\nGame over!It'a tie!\n")
        return True
    return False


def check_game():
    """
    Return true if user or computer win the game or if it's a tie.
    """
    return check_win() or check_tie()


def display_instructions():
    """
    Displays the game instructions.
    """
    print(
        "\nRULES:\n"
        "\nPlayer 1 and player 2, represented by X and O, take turns "
        "marking the spaces on a 3*3 board.\n"
        "The player who succeeds in placing "
        "three of their marks in a horizontal, "
        "vertical, or diagonal row wins.\n"

        "Make your move by entering a number 1-9"
        " to the available spot.\n"
        "You have the X symbol assigned to you to play,"
        " while the computer has the symbol O."
        " The number will correspond to the board position as illustrated:\n"
        "\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n"
    )
    print("------------------------------------------------------------")


def clear_screen():
    """
    Clears the console.
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Main function that executes the program.
    """
    print("----------------------------")
    print("Welcome to Tic Tac Toe Game!")
    print("----------------------------")
    print("What's you name?")
    name = ''
    while True:
        name = input()
        if name.isalpha():
            break
        print("Please use the letters to input your name!")
    print("----------------------------")
    print('')
    print(f"Welcome {name}!")
    print("Let's play!")
    display_instructions()
    run_game()


if __name__ == '__main__':
    main()

