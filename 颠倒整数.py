"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

import sys
import os

def main():
    #x = 123
    #x = -123 
    #x = 4321
    #x = 1230
    x = 1534236469

    a = 0
    tmp = 0
    if(x < 0):
        x *= -1
        tmp += 1

    a = int(str(x)[::-1])


    if(-2147483648 < a and a < 2147483647):
        if(tmp == 0):
            print(a)

        if(tmp == 1):
            print(a*-1)
    else:
        print(0)
        return 0


if __name__ == '__main__':
    main()
    