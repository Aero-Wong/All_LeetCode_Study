"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

import sys
import os

def main():
    num = 38
    
    sums = num

    while(sums >= 10):
        sums = 0
        while(num > 0):
            sums += num % 10
            num //= 10
            print(sums,num)
        num = sums

    print(sums)
    return sums

if __name__ == '__main__':
    main()
    