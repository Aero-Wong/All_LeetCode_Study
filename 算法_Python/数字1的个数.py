"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:
Input: 13
Output: 6 
Explanation: 
Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

import sys
import os

def main():
    #n = 13
    #n = 1 # 1
    #n = 10 # 2
    #n = 100 # 21
    #n = 1000 # 301
    n = 10000 # 4001
    #n = 100000 # 50001
    #n = 1000000 # 估 600001
    #n = 10000000 # 估 7000001

    tmp = 0

    for i in range(0,n+1):
        tmp += str(i).count("1")

    print(tmp)
    return tmp

"""
    tmp = 0
    arr = []
    
    for i in range(n + 1):
        arr = list(map(int, str(i)))
        arr.sort()
        tmp += arr.count(1)
        arr = []
    
    print(tmp)
    return tmp
"""
"""    
    arr = []
    j = 0
    tmp = 0
    Num = 0

    if(n <= 10000):
        Num = n
    if(n > 10000):
        Num = n // 10000

    for i in range(Num + 1):
        j = i
        while(j > 0):
            if(j % 10 == 1):
                tmp += 1
                if i not in arr:
                    arr.append(i)
            j //= 10

    print(arr)
    print(tmp)
"""

if __name__ == '__main__':
    main()
