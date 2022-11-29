""" Generates random number """
import random
import os

BOARD = [' ']*9
USER_SELECTION = []
COMPUTER_SELECTION = []

WIN_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]


def display_board():
    """
    Displays the board.
    """
    print(BOARD[0] + '|' + BOARD[1] + '|' + BOARD[2])
    print('-+-+-')
    print(BOARD[3] + '|' + BOARD[4] + '|' + BOARD[5])
    print('-+-+-')
    print(BOARD[6] + '|' + BOARD[7] + '|' + BOARD[8])


def run_game():
    """
    This is a function that runs the game until the board is full.

    Gets user and computer input and checks if it is a valid and if not
    displays error messages.

    After each move checks if player wins or is it a tie.
    """
    while not is_board_full():
        print("\nPlease enter a number (1-9): \n")
        display_board()
        try:
            user_input = input()
            if user_input.isnumeric() is False:
                print("\nInput must be a number between 1 and 9.\n")
                continue

            user_input = int(user_input)

            if user_input_between_one_and_nine(user_input) is False:
                print("\nYour input number is not between 1 and 9.\n")
                continue

            if is_cell_empty(BOARD[user_input - 1]) is False:
                print("\nThis place is already taken. Choose another spot.\n")
                continue

            BOARD[user_input - 1] = 'X'
            USER_SELECTION.append(user_input)
            if check_if_game_over():
                break
            computer_input = generate_computer_input()
            COMPUTER_SELECTION.append(computer_input)
            if check_if_game_over():
                break
            clear_screen()
        except ValueError:
            print("\nInvalid input. Please try again\n")
    display_board()


def is_board_full():
    """
    Checks if the board has empty cells and returns True, otherwise False.
    """
    for value in BOARD:
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
        if not BOARD[int(computer_input - 1)] in {'X', 'O'}:
            BOARD[computer_input - 1] = 'O'
        else:
            computer_input = generate_computer_input()
    return computer_input


def check_win():
    """
    Returns True if the player wins the game.
    """
    # Solution from stackoverflow
    # https://stackoverflow.com/questions/33203038/nested-loops-in-nested-lists
    if any([set(w).issubset(set(COMPUTER_SELECTION))
           for w in WIN_COMBINATIONS]):
        print("\n*** Game over ***\n")
        print("Your opponent beat you!\n")
        return True
    if any([set(w).issubset(set(USER_SELECTION)) for w in WIN_COMBINATIONS]):
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


def check_if_game_over():
    """
    Return true if user or computer win the game or if it's a tie.
    """
    return check_win() or check_tie()


def init():
    """
    Resets global variables for restarting the game.
    """
    global BOARD
    global USER_SELECTION
    global COMPUTER_SELECTION
    USER_SELECTION = []
    COMPUTER_SELECTION = []
    BOARD = [' ']*9


def restart_game():
    """
    Restarts the game.
    """
    while True:
        print("\nWould you like to play again?")
        print("\nEnter 'y' for YES or 'n' for NO:")
        user_choice = input().strip().lower()
        if user_choice == 'y':
            clear_screen()
            init()
            run_game()
        elif user_choice == 'n':
            clear_screen()
            print("\n")
            print("Thank you for playing!\n")
            break
        else:
            print("Invalid answer. Press 'y' to start and 'n' to quit.")


def display_instructions():
    """
    Displays the game instructions.
    """
    print(
        "\nGAME RULES:\n"
        "\nPlayer 1 and player 2, represented by X and O, take turns "
        "marking the spaces on a 3*3 board.\n"
        "The player who succeeds in placing "
        "three of their marks in a horizontal, "
        "vertical, or diagonal row wins.\n"

        "Make your move by entering a number 1-9"
        " to the available square.\n"
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
    print("WELCOME TO TIC-TAC-TOE!")
    print("----------------------------")
    print("Enter your name:")
    name = ''
    while True:
        name = input()
        if name.isalpha():
            break
        print("Please use the letters to input your name!")
    print("\n")
    print(f"Welcome {name}!")
    print("\nLet's play!")
    display_instructions()
    run_game()
    restart_game()


if __name__ == '__main__':
    main()
