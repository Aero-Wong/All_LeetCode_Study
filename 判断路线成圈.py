import os
import sys

def main():
    moves = "UD"
    #moves = "LL"

    x = 0
    y = 0
    tmp = 0
    for i in moves:
        print(i)
        if(i == "U"):
            y += 1
        if(i == "D"):
            y -= 1
        if(i == "R"):
            x += 1
        if(i == "L"):
            x -= 1
    print(x,y)
    if(x == 0 and y == 0):
        print("true")
        return True
    else:
        print("false")
        return False


if __name__ == '__main__':
    main()

