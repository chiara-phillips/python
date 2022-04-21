############
# Name: Chiara Phillips
# UID: 804562889
# Date: 4/7/2019
############
# Purpose: To Introduce Computer Programming
# Step 1: Welcome the user and prompt them to enter their name to store in a variable.
name = input("Why hello there! What is your name? ")
# Step 2: Greet the user with their stored input name.
print("Well, it's nice to meet you {}!".format(name))
# Step 3: Explain the program's functionality.
print("Welcome to EMDAS! EMDAS is a simple Python program that can perform basic arithmetic using exponents, "
      "multiplication, division, addition, and subtraction using any two numbers of your choosing!")
# Step 4: Get the first number and store it as a variable.
variable1 = int(input("First things first. Choose a number, any number! "))
# Step 5: Get the second number and store it as a different variable.
variable2 = int(input("You know the deal. Choose a second number now! "))
# Step 6: Explain that EMDAS will calculate exponents of the first number to the power of the second.
print("Time for my magic! First I'll show you that I know my exponents "
      "by calculating {} to the power of {}! Drumroll please...".format(variable1,variable2))
# Step 7: Give the answer to the exponent problem.
print("...It's", variable1**variable2,"! Ta-da!")
# Step 8: Prompt the multiplication operation.
print("I can also do multiplication with your numbers: {} multiplied by {} "
      "is".format(variable1,variable2), str(variable1*variable2)+".")
# Step 9: Prompt the division operation.
print("You can bet that I can divide with your numbers too! {} divided by {} "
      "is".format(variable1,variable2), str(variable1/variable2)+".")
# Step 10: Prompt the addition operation.
print("In addition, I can add your numbers! {} plus {} is".format(variable1,variable2), str(variable1+variable2)+".")
# Step 11: Prompt the subtraction operation.
print("Now, for my last act, let's subtract the second number from the first!"
      " {} - {} is".format(variable2,variable1), str(variable2-variable1)+"!")
# Step 12: Close out and conclude
print("It's been a pleasure. Thanks for taking some time to get to know me! Hope you've enjoyed my mad math skills!")


