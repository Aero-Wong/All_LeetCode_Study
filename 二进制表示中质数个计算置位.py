"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""

import sys
import os

def main():
    L = 6;R = 10
    #L = 10;R = 15
    #L = 1;R = 10000

    tmp = 0
    nums_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for i in range(L,R+1):
        bin_nums = bin(i)
        str(bin_nums)
        nums = bin_nums.count('1')
        print(nums,bin_nums)

        if nums in nums_list:
            tmp += 1
  
    print(tmp)
    return tmp

if __name__ == '__main__':
    main()
    