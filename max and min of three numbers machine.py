###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 4/21/2019
############


# Define the function that accepts three number parameters.
def high_low_num_machine(a, b, c):
    # Welcome user to the function
    print("When you enter three different numbers, I'll tell you which one is the minimum and which is the maximum!")
    # If the first number is smaller than the other two numbers, print that it is the minimum.
    # If not, move on to the next line.
    if (a < b) and (a < c):
        print("{} is the minimum".format(a))
    # If the second number is smaller than the other two numbers, print that it is the minimum.
    # If not, move on to the next line.
    elif (b < a) and (b < c):
        print("{} is the minimum".format(b))
    # If the third number is smaller than the other two numbers, print that it is the minimum.
    elif (c < a) and (c < b):
        print("{} is the minimum".format(c))
    # If the first number is larger than the other two numbers, print that it is the maximum.
    # If not, move on to the next line.
    if (a > b) and (a > c):
        print("and {} is the maximum. Tee hee.".format(a))
    # If the second number is larger than the other two numbers, print that it is the maximum.
    # If not, move on to the next line.
    elif (b > a) and b > c:
        print("and {} is the maximum. Tee hee.".format(b))
    # If the third number is larger than the other two numbers, print that it is the maximum.
    # If not, move on to the next line.
    elif (c > a) and (c > b):
        print("and {} is the maximum. Tee hee.".format(c))


# Call the function with the guesses
high_low_num_machine(4, 7, 10)