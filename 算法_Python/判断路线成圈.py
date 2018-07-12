"""
Initially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""

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

