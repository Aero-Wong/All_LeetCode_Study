"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

import os
import sys

def main():
    #n = 3
    #n = 5
    #n = 10
    n = 7
    #n = 3241

    tmp = 0       
    num = 0
    while(n // 5):
        print(n)
        tmp = n // 5
        print(tmp)
        num += tmp
        print(num)
        n = tmp
        print(n)
    print(num)
    return num
 
"""
    tmp = 0
    num = 0
    while(n > 0):
        num = n // 5
        tmp += num
        n = n // 5
        print(num,tmp,n)

    print(tmp)
    return tmp
"""


"""    
    num = 1
    tmp = 0
    for i in range(1,n+1):
        print("i:",i)
        num *= i
        print(num)

    while(num > 0 and num % 10 == 0):
        print(num)
        if(num % 10 == 0):
            tmp += 1
            print(tmp)
        num = num // 10

    print(tmp)
    return tmp
"""

if __name__ == '__main__':
    main()