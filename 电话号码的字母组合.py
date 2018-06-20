"""

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

import sys
import os

def main():
    digits = "23"

    dict = {1:[],
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}

    arr = []
    arr1 = dict[3]
    arr2 = dict[2]
    num = int(digits)
    arr = arr1 * arr2
    print(arr)



if __name__ == '__main__':
    main()