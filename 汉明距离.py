"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4

Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

import os
import sys

def main():
    x = 1
    y = 4

    tmp = 0
    num1 = 0
    num2 = 0

    while(0 <= x and y < 2**31):
        num1 = x ^ y
        print("num1:",num1)
        while(num1 != 0):
            tmp += 1
            num2 = num1 -1
            num1 &= num2
            print("tmp:",tmp,"num1:",num1,"num2:",num2)
    print("tmp:",tmp)
    return tmp
            
if __name__ == '__main__':
    main()
    