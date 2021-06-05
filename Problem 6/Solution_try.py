
import random 
import getpass # With this module we give input as a password which is not visible to other person.
a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))
lst =[]
for i in range(a,b+1): # making a list , which contain integer value from a to b
    lst.append(i)
print(lst)
r = random.choice(lst) # Choosing random value from this list "lst"

# print(r) # For testing our generated value
print(f"Your range of Guessing is between {a} and {b}\n")
print("Player 1 Turn\n")
i = 1 # initializing player 1 attempt.
while(True):
    player1_inp = int(getpass.getpass("Enter Number Don't worry Your number is not visible to your friend "))
    # player1_inp = int(input(" Enter Number "))
    if (player1_inp == r):
        print(f"Your Guess is right and you took {i} attempt")
        break
    elif(player1_inp > r):
        print("Your Guess is greater then that number please guess smaller one")
        i += 1
    elif(player1_inp < r):
        print("Your Guess is lesser then that number please guess greater number")
        i += 1
print(f"Your range of Guessing is between {a} and {b}\n")
print("Player 2 Turn\n")
j = 1 # initializing player 2 attempt.
while(True):
    player2_inp = int(getpass.getpass("Enter Number Don't worry Your number is not visible to your friend "))
    if (player2_inp == r):
        print(f"Your Guess is right and you took {j} attempt")
        break
    elif(player2_inp > r):
        print("Your Guess is greater then that number please guess smaller one")
        j += 1
    elif(player2_inp < r):
        print("Your Guess is lesser then that number please guess greater number")
        j += 1

if (i>j):
    print(f"Player 2 win the game by {i - j} points")
elif (j>i):
    print(f"Player 1 win the game by {j - i} points")
else:
    print("Match is Draw")
