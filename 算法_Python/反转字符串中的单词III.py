"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


import sys
import os

def main():
    s = "Let's take LeetCode contest"

    strs = s.split()
    arr = []

    for i in range(len(strs)):
        arr.append(strs[i][::-1])

    print(' '.join(arr))
    return ' '.join(arr)

if __name__ == '__main__':
    main()
    