# ============= Solution of Problem statement 6 ===================

"""
Author: Pankaj(GoSu)
Date: 5 june 2021
Purpose: Practice problem

"""
# ============ Number Guessing Game ===================
while(True):
    import random
    import getpass  # With this module we give input as a password which is not visible to other person.
    print("\t \t Welcome To! \n \t \tNumber Guessing Game ")
    a = int(input("Enter first number :\n"))
    b = int(input("Enter second number :\n"))
    lst = []
    for i in range(a, b + 1):  # making a list , which contain integer value from a to b
        lst.append(i)
    print(lst)
    r = random.choice(lst)  # Choosing random value from this list "lst"

    # print(r) # For testing our generated value
    print(f"Your range of Guessing is between {a} and {b}")
    print("==============Player 1 Turn================\n")
    i = 1  # initializing player 1 attempt.
    while True:
        player1_inp = int(
            getpass.getpass(
                "Enter Number Don't worry Your number is not visible to your friend \n"
            )
        )
        # player1_inp = int(input(" Enter Number "))
        if player1_inp == r:

            print(f"Your Guess is right and you took {i} attempt\n")
            break
        elif player1_inp > r:
            print("Your Guess is greater then that number please guess smaller one\n")
            i += 1
        elif player1_inp < r:
            print("Your Guess is lesser then that number please guess greater number\n")
            i += 1

    print(f"Your range of Guessing is between {a} and {b}")
    print("============Player 2 Turn==============\n")
    j = 1  # initializing player 2 attempt.
    while True:
        player2_inp = int(
            getpass.getpass(
                "Enter Number Don't worry Your number is not visible to your friend \n"
            )
        )
        if player2_inp == r:

            print(f"Your Guess is right and you took {j} attempt\n")
            break
        elif player2_inp > r:
            print("Your Guess is greater then that number please guess smaller one\n")
            j += 1
        elif player2_inp < r:
            print("Your Guess is lesser then that number please guess greater number\n")
            j += 1

    if i > j:
        print(f"Player 2 win the game by {i - j} points\n")
    elif j > i:
        print(f"Player 1 win the game by {j - i} points\n")
    else:
        print("Match is Draw\n")
    
    inp = input("Want To play again if yes press [y] or press any key to exit()")
    inp = inp.lower()
    if inp == "y":
        continue
    else:
        break
