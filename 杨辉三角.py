"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

import os
import sys

def main():
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    #numRows = 5
    numRows = 3

    arr = []

    for i in range(numRows):
        a = [1] * (i + 1)
        arr.append(a)
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]  
            
    print(arr)
    return arr  
 

if __name__ == '__main__':
    main()
    