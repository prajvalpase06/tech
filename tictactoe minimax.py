def displayBoard(board):
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print(board[7] + ' |' + board[8] + ' |' + board[9])

def freeSpace(position):
    if board[position] == ' ':
        return True
    else:
        return False
        
def insertLetter(letter, position):
    if freeSpace(position):
        board[position] = letter
        displayBoard(board)
        if (checkForDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else: 
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return

def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
        else:
            return True

def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichLetterWOn(l):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == l):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == l):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == l ):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == l):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == l):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == l):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == l):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == l):
        return True
    else:
        return False

def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(user, position)
    return

def compMove():
    bestScore = -900
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = comp
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(comp , bestMove)
    return

def minimax(board, depth, isMaxsimizing):
    if (checkWhichLetterWOn(comp)):
        return 1
    elif (checkWhichLetterWOn(user)):
        return -1
    elif checkForDraw():
        return 0
    if isMaxsimizing:
        bestScore = -700
        for key in board.keys():
            if board[key] == ' ':
                board[key] = comp
                score = minimax(board, depth+1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 700
        for key in board.keys():
            if board[key] == ' ':
                board[key] = user
                score = minimax(board, depth+1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

user = 'O'
comp = 'X'

print ("1 2 3 ")
print ("4 5 6 ")
print ("7 8 9 ")
print("\n")

print("The computer goes first! ")

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
    print("\n")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")