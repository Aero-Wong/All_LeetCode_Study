"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""

import os
import sys

def main():
    a = 1
    #b = -1
    b = 2

    sums = sum([a,b])

    print(sums)
    return sums
    
"""
    tmp1 = 0
    tmp2 = 0
    sums = 0

    tmp1 = a ^ b
    tmp2 = (a&b) << 1
    sums = sum([tmp1,tmp2])
 
    print(sums)
    return sums
"""
 
"""
    for i in range(a):
        arr.append(1)
    for j in range(b):
        arr.append(1)

    i = 0
    while(i < len(arr)):
        if(arr[i] == 1):
            tmp += 1
        if(arr[i] == -1):
            tmp -= 1
        i += 1

    print(tmp)
    return tmp
"""
    
if __name__ == '__main__':
    main()
    