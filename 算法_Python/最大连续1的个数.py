"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

import sys
import os

def main():
    #nums = [1,1,0,1,1,1] # 3
    #nums = [1,0,1,1,0,1] # 2
    nums = [1] # 1

    tmp = 0
    top = 0

    for i in nums:
        if(i == 1):
            tmp += 1
            if(tmp >= top):
                top = tmp
        else:
            tmp = 0

    print(top,tmp)
    return top

"""   
    for i in nums:
        if(i == 1):
            print(tmp)
            tmp += 1
        if(i == 0):
            if(top < tmp):
                top = tmp
            tmp = 0

    print(tmp,top)
    if(tmp > top):
        return tmp
    else:
        return top
        """

if __name__ == '__main__':
    main()
    