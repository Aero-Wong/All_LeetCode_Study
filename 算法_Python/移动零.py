"""
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

import os
import sys


def main():
    nums = [0,1,0,3,12]

    tmp = 0
    
    for i in range(0,len(nums)):
        print(i,nums[i])
        if(nums[i] != 0):
            nums[tmp] = nums[i]
            tmp += 1
        print(nums)
        
    for j in range(tmp,len(nums)):
        nums[j] = 0
    
    print(nums)
    return nums

if __name__ == '__main__':
    main()
    