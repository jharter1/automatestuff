import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Concentrate ye daft bastard'
    elif answerNumber == 6:
        return 'My reply is no'
    elif answerNumber == 7:
        return 'Outlook bad'
    elif answerNumber == 8:
        return 'Doubt'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)