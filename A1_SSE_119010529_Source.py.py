import random

count = 0
table8 = ['1','2','3','4','5','6','7','8',' ']
table15 = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','  ']
random.shuffle(table8)
random.shuffle(table15)
directions = list(str(input("Enter four letter to move Left, Right, Up, Down repeatedly:")))
version = int(input("Enter puzzle type (1 or 2):"))

def inversion():                                #inversion is counted to check solvable function
    inversions = 0                              #it counts the numbers bigger than the number before
    if version == 1:
        table8 = ['1','2','3','4','5','6','7','8',' ']
        table8.remove(' ')
        for a in range(0,len(table8)):
            for b in range(0,len(table8)-1):
                if a>b and table8[a]>table8[b]:
                    inversions += 1
    elif version == 2:
        table15 = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','  ']
        table15.remove('  ')
        for a in range(0,len(table15)):
            for b in range(0,len(table15)-1):
                if a>b and table15[a]>table15[b]:
                    inversions += 1
    return inversions

inversions = inversion()                        #this is to define the variable to be used in solvable function

def solvable(inversions):                       #a function to check whether the upcoming table is solvable or not
    if version == 1 and inversion()%2 != 0:     #I put the more detailed information in the text file
        return True       
    elif version == 2:
        blank = table15.index('  ')
        if blank < 4 or 7 < blank < 12 and inversion() % 2 != 0:
            return True
        elif 3 < blank < 8 or 11 < blank and inversion() % 2 == 0:
            return True
    else:
        return False

def displayTable():                             #displaying the table with numbers from list separated by a space
    for i in range(0,len(model)):
        if i%r == r-1:
            print(model[i])
        else:
            print(model[i], ' ', end='')

def play():                                     #function to slide the numbers by exchanging the value index on the list
    if move == directions[0]:
        blank = model.index(blankSpace)
        if blank % r != r-1:
            model[blank], model[blank+1] = model[blank+1], model[blank]
        displayTable()
    elif move == directions[1]:
        blank = model.index(blankSpace)
        if blank % r != 0:
            model[blank], model[blank-1] = model[blank-1], model[blank]
        displayTable()
    elif move == directions[2]:
        blank = model.index(blankSpace)
        if blank < (r-1)/r*len(model):
            model[blank], model[blank+r] = model[blank+r], model[blank]
        displayTable()
    elif move == directions[3]:
        blank = model.index(blankSpace)
        if blank > r-1:
            model[blank], model[blank-r] = model[blank-r], model[blank]
        displayTable()
    else:
        print("Error")

def option():                               #function to give out moves option that user can make
    Left = ["Left", directions[0]]
    Right = ["Right", directions[1]]
    Up = ["Up", directions[2]]
    Down = ["Down", directions[3]]
    movesOption = [Left, Right, Up, Down]
    if blank % r == 0:
        movesOption.remove(Right)
    if blank % r == (r-1):
        movesOption.remove(Left)
    if blank > (r-1)/r*len(model):
        movesOption.remove(Up)       
    if blank < r:
        movesOption.remove(Down)
    print("Slide available:", *movesOption, sep = '')

while True:                                 #while True is used to loop the codes
    if version == 1:                        #(in case after finishing puzzles, the user want to repeat another game)
        model = table8
        r = 3
        blankSpace = ' '
        print("Welcome to 3x3 puzzle! \nYour task is to order the numbers below:")
        while solvable(inversions) != True:             #this loop will keep shuffling the list until it is solvable
            random.shuffle(model)
            break
        displayTable()                                  #diplaying the solvable table
        while model != ['1','2','3','4','5','6','7','8',' ']:               #looping until the numbers ordered well
            count += 1                                                      #counting user's moves
            blank = model.index(blankSpace)
            option()                                                        #giving user moves option
            move = input()
            if move in directions:
                play()
            elif move == 'quit':                                            #user can quit in the middle of playing
                print("You have given up")
                break
        if model == ['1','2','3','4','5','6','7','8',' ']:
            print("You have finished in", count, "moves! \n Type 'restart' to play another game or type 'quit' to end the game")
            feedback = input()                                  #taking input from user whether to repeat or quit the game
    elif version == 2:                              #similar to version 1 puzzle
        model = table15
        r = 4
        blankSpace = '  '
        print("Welcome to 4x4 puzzle! \nYour task is to order the numbers below:")
        while solvable(inversions) != True:
            random.shuffle(model)
            break
        displayTable()
        while model != [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','  ']:
            count += 1
            blank = model.index(blankSpace)
            option()
            move = input()
            if move in directions:
                play()
            elif move == 'quit':
                print("You have given up")
                break
        if model == [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','  ']:
            print("You have finished in", count, "moves! \n Type 'restart' to play another game or type 'quit' to end the game")
            feedback = input()
    if feedback == 'quit':
        break