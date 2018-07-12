"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1
Input: [3,0,1]
Output: 2

Example 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

import os
import sys

def main():
    #nums = [3,0,1]
    #nums = [9,6,4,2,3,5,7,0,1]
    #nums = [0,1]
    nums = [0]

    nums.sort()
    i = 0
    tmp = 1

    while(i < len(nums)):
        print(i,nums[i])
        if(nums[i] != i):
            print(i)
            return i
            
        if(tmp == len(nums)):
            print(tmp)
            return tmp

        print("tmp:",tmp,i)
        tmp += 1
        i += 1

if __name__ == '__main__':
    main()
