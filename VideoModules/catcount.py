print('How many cats you got?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is many cat.')
    if int(numCats) < 0:
        print('You cannot have less than zero cats.')
    else:
        print('Not so many cat.')
except ValueError:
    print ('That is not a number.')
