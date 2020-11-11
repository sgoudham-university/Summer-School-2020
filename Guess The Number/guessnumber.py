# Nested while with while loop
# Try entering a few strings and numbers

# Start program
import random  # Import the random library for use in the program


def initialise_game_variables():
    """Initialise the game variables"""

    # Set constant variables for number of tries has and the max number that the computer can generate
    num_of_tries = 5
    max_number = 5

    return num_of_tries, max_number


def initialise_loop_variables(max_number):
    """Initialise loop variables"""

    computer_num = random.randint(1, max_number)  # Computer generates a random number between 1 and maxNumber variable
    user_number = ""  # Initialise the user number to a string so we enter the loop to check for a valid integer
    counter = 0  # Initialise the counter so we can increment and count the number of tries.

    return computer_num, user_number, counter


def check_number(user_number, computer_num):
    """Check if the number entered by the user was the same as the computer's"""

    found = False  # Initialise the found to False so we enter the loop, but stop once a number is correct

    # We can only compare an integer to an integer so we convert the input string user_number to an integer
    # Check if the correct number or if too low or too high
    if int(user_number) == computer_num:
        print("Success computer number is", computer_num)
        found = True  # Set to found so we exit the while loop
    elif int(user_number) < computer_num:
        print("Your number is too low")
    elif int(user_number) > computer_num:
        print("Your number is too high")

    return found


def guess_number(num_of_tries, max_number):
    """Let the user guess the number"""

    # Get the loop variables initialised
    computer_num, user_number, counter = initialise_loop_variables(max_number)

    # Start while loop with two conditions
    # First condition if we only want the player a set number of tries
    # Second condition we will exit once the computer's number has been found
    while counter < num_of_tries:
        # While loop to get a valid integer
        while not user_number.isdigit():
            user_number = input(f"Choose a number from 1 to {str(max_number)}?\n")

        # When the number is found, stop the program
        if check_number(user_number, computer_num):
            return

        counter += 1  # Increment the counter by one
        user_number = ""  # Reset the user_number to a string so we enter the while loop to check for an integer


def main():
    """Generate a number and let the user guess it"""

    num_of_tries, max_number = initialise_game_variables()
    guess_number(num_of_tries, max_number)


# Execute main method
main()
