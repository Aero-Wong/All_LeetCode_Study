"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

import os
import sys

def main():
    #nums = [2, 7, 11, 15]
    #target = 9
    #nums = [2,5,5,11]
    #target = 10
    nums = [-1,-2,-3,-4,-5]
    target = -8
    #nums = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,78]
    #target = 
    arr = []

    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            print(i,nums[i],j,nums[j])
            if(nums[i] + nums[j] == target):
                arr.append(i)
                arr.append(j)

    print(arr)
    return arr


if __name__ == '__main__':
    main()
    