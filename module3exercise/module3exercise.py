""" generates a random number between 1 and 10, and asks the user to guess what it is
"""
'''
Modify this program so that it:
1) allows the user as many tries as she needs in order to guess the secret random number, and
2) gives the user feedback that tells her if her guess is too high or too low.
'''


import random  # needed to use randint()
secretNumber = random.randint(1,10)
print('The secret number is = ', secretNumber)

userInput = input('Pick a number between 1 and 10: ')
userGuess = int (userInput)

while userGuess != secretNumber:
    if userGuess < secretNumber:
        print('your guess is too low\n')
    elif userGuess > secretNumber:
        print('your guess is too high\n')
    userInput = input('Pick a number between 1 and 10: ')
    userGuess = int(userInput)

print ('You got it')
