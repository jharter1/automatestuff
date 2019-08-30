# this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between and including 1 and 20.')

# ask for the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Too low, try again!')
    elif guess > secretNumber:
        print('Too high, big spender!')
    else:
        break   #this condition should indicate the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('No dice, champ. The number I was thinking of was ' + str(secretNumber))