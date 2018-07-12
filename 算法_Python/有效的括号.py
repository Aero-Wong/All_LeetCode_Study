"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

import os
import sys

def main():
    s = "()"
    #s = "()[]{}"
    #s = "(]"
    #s = "([)]"
    #s = "{[]}"

    i = 0
    tmp = 0
    arr = []
    s = list(s)

    while(i < len(s)):
        if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
            arr.append(s[i])
            tmp += 1
            i += 1
        elif(s[i] == '(' or s[i] == ']' or s[i] == '}'):
            if(tmp > 1):
                arr.append(s[i])
                i += 1
            
 
if __name__ == '__main__':
    main()
    