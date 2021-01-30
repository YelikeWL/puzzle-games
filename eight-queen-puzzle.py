'''The classic Eight Queens puzzle is to place eight queens on a chessboard 
such that no two queens can attack each other (i.e., no two queens are in the
same row, same column, or same diagonal). There are many possible solutions. Write a
program that displays one such solution.'''

def duplicate(q):
    if len(q) == len(set(q)):
        return True
    else:
        return False

def diagonal(q):
    for a in range(7, 0, -1):
        for b in range(a):
            if abs((q[a]-q[b])/(a-b)) == 1:
                return False
    return True

for c0 in range(8):
    for c1 in range(8):
        for c2 in range(8):
            for c3 in range(8):
                for c4 in range(8):
                    for c5 in range(8):
                        for c6 in range(8):
                            for c7 in range(8):
                                q = [c0, c1, c2, c3, c4, c5, c6, c7]
                                if duplicate(q) and diagonal(q) == True:
                                    save = q
    break
for i in range(8):
    print("| "*(save[i]) + "|Q" + "| "*(7-save[i])+'|')
