# Muhammad Awan
# Hangman Game

import random
import json
import time


def setLevel():
    difficulty = input('\nPlease enter difficulty (easy, medium, hard): ')

    global tries

    if difficulty == "easy":
        tries = 7
        print('You have %d tries' % tries)
    elif difficulty == "medium":
        tries = 5
        print('You have %d tries' % tries)
    elif difficulty == "hard":
        tries = 3
        print('You have %d tries' % tries)
    else:
        print('You entered a wrong input.')
        setLevel()


def compareWords():
    global tries, gameOver, wrongWordList, userWord

    userLetter = list(input('Enter a letter: '))

    for letter in userLetter:
        i = 0
        if letter in wrongWordList or letter in userWord:
            print('You already chose that letter')
        elif letter in chosenWord:
            while i < len(chosenWord):
                if letter == chosenWord[i]:
                    userWord[i] = letter
                i += 1
            print('You entered a correct letter!')
        else:
            tries = tries - 1
            wrongWordList.append(letter)
            if tries == 0:
                gameOver = True
            print('Wrong guess! You have %d tries left' % tries)


def checkWin():
    global gameOver

    if set(userWord) == set(chosenWord):
        print('-----------------------------------------------')
        print('You guessed the word!')
        gameOver = True


def tryAgain():
    global gameOver, chosenWord, userWord, wrongWordList

    tryAgainInput = input('Would you like to try again? (y/n) ')
    
    if tryAgainInput.lower() == 'y':
        gameOver = False
        chosenWord = list(random.choice(words))
        userWord = list()
        wrongWordList = list()
        setLevel()
    elif tryAgainInput.lower() == 'n':
        print('\nLet\'s play again next time!')
    else:
        tryAgain()


# main()
words = json.loads(open('wordsList').read())
chosenWord = list(random.choice(words))
userWord = [' '] * len(chosenWord)
wrongWordList = []
gameOver = False
tries = 7
setLevel()

print('Generating word', end='')
for x in range(5):
    print('.', end='', flush=True)
    time.sleep(0.75)

while not gameOver:
    print('\nThe word is %d characters long' % len(chosenWord))
    compareWords()
    if not gameOver:
        print('Correct Guesses:', userWord)
        print('Wrong Guesses:', wrongWordList)
        checkWin()

    if gameOver:
        print('-----------------------------------------------')
        print('\nCorrect word:', ''.join(chosenWord))
        print('Correct Guesses:', userWord)
        print('Wrong Guesses:', wrongWordList)
        tryAgain()
