"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

import os
import sys

def main():
    nums = [1,2,3]

    arr = [[]]

    for i in nums:
        print(i)
        arr.extend([[i]+j for j in arr])
        print(arr)

    print(arr)
    return arr

"""
    for i in nums:
        for j in arr:
            arr.extend([[i] + j])
            #print(arr)
"""
   

if __name__ == '__main__':
    main()
    