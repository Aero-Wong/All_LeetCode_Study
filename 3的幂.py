"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

import os
import sys

def main():
    n = 0

    tmp = 0

    if(n <= 0):
        print("false")
        return False

    if(n == 1):
        print("true")
        return True

    while(n % 3 == 0):
        tmp += 1
        n /= 3

    if(n == 1):
        print("true")
        return True
    else:
        print("false")
        return False

    print("false")
    return False

"""
    tmp1 = 0
    tmp2 = 0
    for i in range(120):
        num = 1
        for j in range(i):
            num *= 3
        tmp1 += 1
        print(num)
        print(tmp1, tmp2)
"""

"""    if(n < 1):
        print("false")
        return False

    elif(n == 1 or n == 3):
        print("true")
        return True
 
    
    elif(n % 3 == 0):
        if(n % 5 != 0):
            print("true")
            return True 
        else:
            print("false")
            return False
    else:
        print("False")
        return False
"""
 

if __name__ == '__main__':
    main()


