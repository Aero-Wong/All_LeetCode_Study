"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

import os
import sys


def main():
    #digits = [1,2,3]
    #digits = [4,3,2,1]
    digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]

    arr = []
    num = 0
    tmp = 0
    for i in range(0,len(digits)):
        num = num * 10 + digits[i]
        print("default",num)
    num += 1
    print("+1",num)
    num = list(str(num))
    for i in range(len(num)):
        arr.append(int(num[i]))
        print(arr)
"""    
    while(num != 0):
        tmp = num % 10
        num = num / 10
        num = int(num)
        arr.append(tmp)
        print(num)
        print(arr)
    arr.reverse()
    print(arr)
"""
"""        
    num += 1
    print(num)
    tmp = list(num)
    print(tmp)
"""

 
if __name__ == '__main__':
    main()
    