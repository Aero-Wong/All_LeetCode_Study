"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

import os
import sys

def main():
    #word = "USA"
    word = "FlaG"

    str1 = word
    str2 = word.lower()

    if(str1 == word.upper()):
        return True
    elif(str1 == word.lower()):
        return True
    elif(str1 == str2.title()):
        return True
    else:
        return False

    """
    t = word
        t1 = word.upper()
        t2 = word.lower()
        t3 = t2.title() #首字母大写
        return  t==t1 or t==t2 or t==t3
    """

if __name__ == '__main__':
    main()
    