import numpy as np
import random 

flag = True
d = [["-"] * 3 for i in range(3)]
win = ""
def checkr(i):
    if d[i][0] == d[i][1] == d[i][2] != '-':
        global win
        win = d[i][0]
        return True
    return False

def checkc(i):
    if d[0][i] == d[1][i] == d[2][i] != '-':
        global win
        win = d[0][i]
        return True
    return False

def checkd():
    global win
    if d[0][0] == d[1][1] == d[2][2] != '-':
        win = d[0][0]
        return True
    if d[0][2] == d[1][1] == d[2][0] != '-':
        win = d[0][2]
        return True
    return False

def display():
    print(np.array(d))

def check():
    l=set(d[0]+d[1]+d[2])
    if "-" not in l:
        return True

turn = random.choice(["X", "O"])
print(f"{turn} goes first!")

while flag:
    if turn == "X":
        x = tuple(map(int, input("Enter row and column of X input: ").strip().split()))
        if d[x[0]][x[1]] != '-':
            print("Spot already occupied, pick a new location.")
            continue

        d[x[0]][x[1]] = "X"

        if checkd() or any(checkr(i) for i in range(3)) or any(checkc(i) for i in range(3)):
            print(f"{win} Wins!")
            display()
            break

        display()
        if check():
            print("Tie")
            break

        turn = "O"  

    elif turn == "O":
        y = tuple(map(int, input("Enter row and column of O input: ").strip().split()))
        if d[y[0]][y[1]] != '-':
            print("Spot already occupied, pick a new location.")
            continue

        d[y[0]][y[1]] = "O"

        if checkd() or any(checkr(i) for i in range(3)) or any(checkc(i) for i in range(3)):
            print(f"{win} Wins!")
            display()
            break

        display()
        if check():
            print("Tie")
            break

        turn = "X"  
