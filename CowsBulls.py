"""
reate a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
 1234
  2 cows, 0 bulls
 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""
import random

def guessCowsBulls (userInput, number):
    cows = 0
    bulls = 0
    length = len(number)

    for i in range(0,length):
        if number[i] == userInput[i]:
            cows += 1
        elif userInput[i] in number:
            bulls += 1
    print("# Cows: ",cows)
    print("# Bull: ",bulls)

    return userInput == number

def generateRandomNumber():
    ran = ""
    i = 0
    while i < 4:
        ran += str(random.randrange(9))
        i += 1
    return ran


randomNumber = generateRandomNumber();
userInput = ""
trials = 0
again = 0
while again == 0:
    while len(userInput) != 4:
        userInput = input("Please enter a 4 digit number ")

    again = guessCowsBulls(userInput, randomNumber)
    trials += 1
    print("\n# Trials: ",trials)

    if again != 0:
        print("Congratulations! You guessed the number")
    else:
        again = int(input("Do you want to play again 0:YES 1:NO: "))
        userInput = ""
