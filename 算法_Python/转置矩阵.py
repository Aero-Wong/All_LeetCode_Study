"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

import os
import sys

def main():
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    #A = [[1,2,3],
    #     [4,5,6]]

    print(zip(*A))
    return zip(*A)

"""   
    arr = [[]for i in A[0]]

    for i in A:
        for j in range(len(i)):
            arr[j].append(i[j])

    print(arr)
    return arr
"""


if __name__ == '__main__':
    main()