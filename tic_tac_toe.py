#!/usr/bin/env python3


# Creates a new empty game board.
def create_empty_board():

    rows = dict()

    for i in range(3):
        rows["row" + str(i)] = [' ',' ',' ']

    return rows


# Displays the game board to the user via the terminal.
def display_board(rows):

    print("\n")

    for _, value in rows.items():
        print(value)


# Update board.
def update_board(rows, user, choice):

    # Logic variables.
    first_row = [1, 2, 3]
    second_row = [4, 5, 6]

    available_rows = ["row0", "row1", "row2"]
    current_row = ""

    if choice in first_row:
        current_row = available_rows[0]
    elif choice in second_row:
        current_row = available_rows[1]
    else:
        current_row = available_rows[2]

    if user == "X":
        rows[current_row][(choice - 1) % 3] = "X"
    else:
        rows[current_row][(choice - 1) % 3] = "O"


# Ask the user for input, check and then return the result as int.
def user_input(user):

    # Placeholder value for the input.
    user_choice = ""

    # List of accepted values and a boolean value.
    accepted_values = range(1, 10)
    choice_in_accepted_values = False

    # Error checking for the input.
    while user_choice.isdigit() == False or choice_in_accepted_values == False:

        print("\n")
        user_choice = input("User {} - Please enter a number (1-9): ".format(user))

        # Digit and range check.
        if user_choice.isdigit() == False:
            print("Please enter a valid number!")
        else:
            if int(user_choice) in accepted_values:
                choice_in_accepted_values = True
            else:
                print("Please enter a valid number!")

    return int(user_choice)


# Check for win.
def check_for_win(rows, playing_user):

    x_win_detected = False
    o_win_detected = False

    # Check the first row horizontally.
    if rows["row0"][0] == "X" and rows["row0"][1] == "X" and rows["row0"][2] == "X":
        x_win_detected = True
    elif rows["row0"][0] == "O" and rows["row0"][1] == "O" and rows["row0"][2] == "O":
        o_win_detected = True

    # Check the second row horizontally.
    if rows["row1"][0] == "X" and rows["row1"][1] == "X" and rows["row1"][2] == "X":
        x_win_detected = True
    elif rows["row1"][0] == "O" and rows["row1"][1] == "O" and rows["row1"][2] == "O":
        o_win_detected = True

    # Check the third row horizontally.
    if rows["row2"][0] == "X" and rows["row2"][1] == "X" and rows["row2"][2] == "X":
        x_win_detected = True
    elif rows["row2"][0] == "O" and rows["row2"][1] == "O" and rows["row2"][2] == "O":
        o_win_detected = True

    # Check the first row vertically.
    if rows["row0"][0] == "X" and rows["row1"][0] == "X" and rows["row2"][0] == "X":
        x_win_detected = True
    elif rows["row0"][0] == "O" and rows["row1"][0] == "O" and rows["row2"][0] == "O":
        o_win_detected = True

    # Check the second row vertically.
    if rows["row0"][1] == "X" and rows["row1"][1] == "X" and rows["row2"][1] == "X":
        x_win_detected = True
    elif rows["row0"][1] == "O" and rows["row1"][1] == "O" and rows["row2"][1] == "O":
        o_win_detected = True

    # Check the third row vertically.
    if rows["row0"][2] == "X" and rows["row1"][2] == "X" and rows["row2"][2] == "X":
        x_win_detected = True
    elif rows["row0"][2] == "O" and rows["row1"][2] == "O" and rows["row2"][2] == "O":
        o_win_detected = True

    # Check for oblique win.
    if rows["row0"][0] == "X" and rows["row1"][1] == "X" and rows["row2"][2] == "X":
        x_win_detected = True
    elif rows["row0"][0] == "O" and rows["row1"][1] == "O" and rows["row2"][2] == "O":
        o_win_detected = True

    # Check for oblique win.
    if rows["row2"][0] == "X" and rows["row1"][1] == "X" and rows["row0"][2] == "X":
        x_win_detected = True
    elif rows["row2"][0] == "O" and rows["row1"][1] == "O" and rows["row0"][2] == "O":
        o_win_detected = True

    # Notify user and return true.
    if x_win_detected == True:

        print("\n\nPlayer X won the game!\n\n")
        return True
    
    if o_win_detected == True:

        print("\n\nPlayer O won the game!\n\n")
        return True

    # If no win, return false.
    return False


# List of player names.
users = ["X", "O"]

# Game logic variables.
playing_user = users[0]
max_total_rounds = 9
current_rounds = 0
win = False

# Create and store the game board.
board = create_empty_board()

# Game loop.
while current_rounds < max_total_rounds and win == False:

    # Update the currently playing user.
    playing_user = users[current_rounds % 2]

    # Ask for user input.
    current_user_input = user_input(playing_user)

    # Update the game board based on the user input.
    update_board(board, playing_user, current_user_input)

    # Display the new game board.
    display_board(board)

    # Check for win.
    win = check_for_win(board, playing_user)

    # Update the rounds counter.
    current_rounds = current_rounds + 1

else:
    # Check for draw.
    if win == False:
        print("\n\nDraw!\n\n")