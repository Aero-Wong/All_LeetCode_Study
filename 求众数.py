"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

import os
import sys

def main():
    nums = [3,2,3]
    #nums = [2,2,1,1,1,2,2]

    num = 0
    tmp = 0

    nums.sort()
    print(nums)

    for i in range(1,len(nums)):
        if(nums[i] == nums[i-1]):
            num = nums[i]
            

if __name__ == '__main__':
    main()