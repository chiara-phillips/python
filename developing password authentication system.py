###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 4/14/2019
############
# Purpose: Developing a Password Authentication System using Control Flow and Functions

# Define the Function with two variables: the first being for the password and the second for the maximum # of attempts.
def passwordProtect(passcode, max_attempts):
    attempts = 0
    # Tell the user that a password is required and that they have limited attempts.
    print("THIS IS A PASSWORD PROTECTED AREA. YOU ARE ALLOWED {} ATTEMPTS UNTIL I "
          "DECLARE YOU AN INTRUDER.".format(max_attempts))
    # Begin the while statement for the limited attempts.
    while attempts < max_attempts:
        # Prompt the user to input the password.
        userguess = input("INPUT PASSWORD NOW: ")
        # Each time the user makes an attempt, ensure that the attempt number will increase by one.
        attempts = attempts + 1
        # If the user types the right password, tell them they have access and end the loop.
        if userguess == passcode:
            print("*sound of bricks moving* ACCESS GRANTED. WELCOME BACK.")
            break
        # If the user types the incorrect password and still has at least one attempt remaining, tell them to try again.
        elif attempts < max_attempts:
            print("HMM. YOU'RE MAKING ME SUSPICIOUS. TRY AGAIN. YOU HAVE {} ATTEMPTS "
                  "LEFT.".format(max_attempts - attempts))
        # If the user uses up all 5 attempts without entering the correct password, tell them and terminate the program.
        else:
            print("CODE RED! MAXIMUM ATTEMPTS EXCEEDED! WE HAVE DETERMINED YOU TO BE AN INTRUDER. YOU'RE LOCKED OUT.")
            exit()

# Call the function to demonstrate.
passwordProtect("opensesame",5)