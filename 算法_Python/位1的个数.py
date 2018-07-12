"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

import os
import sys

def main():
    n = 11
    #n = 128
    #n = 8388608

    num = n
    tmp = 0
    while(num):
        print(num)
        num = num & (num-1)
        #num &= (num -1)
        tmp += 1
        print(num,tmp)
    
    print(tmp)
    return tmp
"""
    i = 0
    num = n
    tmp = 0

    while(i < n):
        print(i,num,tmp)
        if(num % 2 == 1):
            tmp += 1
        num /= 2
        num = int(num)
        i += 1

    print(tmp)
    return tmp
"""
if __name__ == '__main__':
    main()

