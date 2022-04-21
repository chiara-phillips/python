###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 4/21/2019
############


# Define the Function
def num_machine(n):
    # Welcome the user to the machine
    print("Welcome to the Even or Odd Machine! Enter a number and I'll return if it is even or odd.")
    # Prompt the user to input a number
    n = input("Please input a number here: ")
    # If the number divided by two has a remainder, print that the number is an odd number.
    if (int(n) % 2) == 1:
        print("Odd")
        # Exit the function so it doesn't rerun.
        exit()
    # If the number divided by two does not have a remainder, print that the number is an even number.
    else:
        print("Even")
        # Exit the function so it doesn't rerun.
        exit()


# Call an odd number.
num_machine(3)
# Call an even number.
num_machine(6)

