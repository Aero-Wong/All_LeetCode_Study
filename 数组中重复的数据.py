"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

import os
import sys

def main():
    nums = [4,3,2,7,8,2,3,1]
    #output [2,3]

    num = 0
    arr = []
    nums.sort()
    for i in nums:
        if(num != i):
            num = i
        else:
            arr.append(i)
        print(i,num)
    print(arr)

"""
    num = 0
    arr = []

    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            print(nums[i],nums[j])
            if(nums[i] == nums[j] and i != j):
                arr.append(nums[i])
    print(arr)
"""

"""    
    num = 0
    arr = []

    nums.sort()

    for i in nums:
        num ^= i
        print(num,i)
        if(num == 1):
            arr.append(i)
        print(arr)
"""


if __name__ == '__main__':
    main()