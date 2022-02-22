def printBoard(board):                                      #function to print the board
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):                                      # to check if the position entered is empty
    if board[position] == ' ':
        return True
    else:
        return False


def Letter_Insertion(letter, position):                         # fucntion to input the character
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if win_Check():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        Letter_Insertion(letter, position)
        return


def win_Check():                                                                        # winning conditions (diagonals, vertical and horizontal rows)
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


def ReturnWinning(mark):                                                            # checks which players wins
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:          
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():                                                                        # function to check whether the game is draw
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():                                                                           # declares player move
    position = int(input("Enter the position for 'O':  "))
    Letter_Insertion(player, position)
    return


def compMove():                                                                                  # declares computer move
    bestScore = -800
    bestMove = 0
    for key in board.keys():    
        if (board[key] == ' '):
            board[key] = bot                                                         # if space is empty, enter the character in that space 
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    Letter_Insertion(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):                                                # MINIMAX ALGORITHGM FOR CHECKING ALL POSIBILITIES AND PLAYING THE BEST MOVE
    if (ReturnWinning(bot)):                                                               #Here the computer is maximising player
        return 1                                                                           
    elif (ReturnWinning(player)):                                                          # Here the human is minimizing player
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)                        # recursive function, to carry out branching and getting all possible outcomes and paths
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',                                # initializing empty board
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck.")                    
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


while not win_Check():                          # run the loop (or game) till the winning conditions are met
    compMove()                                  # computer -> first move followed by player 
    playerMove()
    print("\n")
    print("1, 2, 3 ")
    print("4, 5, 6 ")
    print("7, 8, 9 ")
    print("\n")