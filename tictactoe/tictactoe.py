# Muhammad Awan
# Game of Tic Tac Toe

import random
import time


def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')


def displayBoardKey():
    time.sleep(1)
    print("The game will look like this. Each number corresponds to that position. "
          "To move to that position, simply enter that number")
    time.sleep(1)
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    drawBoard(board)
    print('This is the format the board will follow...')
    time.sleep(2.5)


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O? ')
        letter = input().upper()

    if letter == 'X' or letter == 'x':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again? (y/n) ')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # across top
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # across middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # across bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # down left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # down middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # down right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal


def getBoardCopy(board):
    secondBoard = []

    for i in board:
        secondBoard.append(i)

    return secondBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'O'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def computerPlayer(theBoard, computerLetter):
    global gameIsPlaying
    move = getComputerMove(theBoard, computerLetter)
    makeMove(theBoard, computerLetter, move)

    if isWinner(theBoard, computerLetter):
        drawBoard(theBoard)
        print('The computer won! You lose')
        gameIsPlaying = False
    else:
        if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('Game is a tie')
            return 'tie'
        else:
            turn = 'player'
            return turn


def humanPlayer(theBoard, playerTwoLetter):
    global gameIsPlaying
    drawBoard(theBoard)
    print("[+] Player 2")
    move = getPlayerMove(theBoard)
    makeMove(theBoard, playerTwoLetter, move)

    if isWinner(theBoard, playerTwoLetter):
        drawBoard(theBoard)
        print('Congrats! Player 2 wins!!')
        gameIsPlaying = False
    else:
        if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('Game is a tie')
            return 'tie'
        else:
            turn = 'player'
            return turn


def getAndReturnStartingPrompt(numPlayers):
    if numPlayers == '1':
        print('\nYou will be versing an AI')
        print('starting game', end='')
        for x in range(1, 5):
            print('.', end="", flush=True)
            time.sleep(1)
        return 'ai'
    else:
        print('\n\nDecide who will be Player 1 and Player 2')
        print('starting game', end='')
        for x in range(1, 5):
            print('.', end="", flush=True)
            time.sleep(1)
        print('\n[!] Asking Player (1)')
        return 'human'


def getTurnPrompt(player, vs):
    if player == 'computer' and vs == 'ai':
        print('The', player, 'will go first.')
    else:
        if player == 'computer':
            player = 'player 2'
        else:
            player = 'player 1'

        print(player, 'will go first.')


def playing(numPlayers):
    displayBoardKey()
    playerPrompt = getAndReturnStartingPrompt(numPlayers)

    while True:
        theBoard = [' '] * 10
        playerLetter, secondLetter = inputPlayerLetter()

        turn = whoGoesFirst()
        getTurnPrompt(turn, playerPrompt)

        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                print("[+] Player 1")
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Congrats! You won!!!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                if playerPrompt == 'ai':
                    turn = computerPlayer(theBoard, secondLetter)
                else:
                    turn = humanPlayer(theBoard, secondLetter)
                if turn == 'tie':
                    break

        if not playAgain():
            break


def main():
    print('Welcome to Tic Tac Toe')
    numPlayers = input('How may players will be playing? (1 or 2): ')

    while numPlayers not in '1 2'.split():
        numPlayers = input('How many players will be playing? (1 or 2): ')

    playing(numPlayers)


if __name__ == "__main__":
    main()
