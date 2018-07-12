"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
American keyboard

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

import os
import sys

def main():
    words = ["Hello", "Alaska", "Dad", "Peace"]

    line1 = ['q','Q','w','W','e','E','r','R','t','T','y','Y','u','U','i','I','o','O','p','P']
    line2 = ['a','A','s','S','d','D','f','F','g','G','h','H','j','J','k','K','l','L']
    line3 = ['z','Z','x','X','c','C','v','V','b','B','n','N','m','M']
    
    arr = []
    j = ''
    l1 = 0
    l2 = 0
    l3 = 0

    for i in range(len(words)):
        j = words[i]
        j = list(j.lower())
        print(j,words[i])
        for h in range(len(j)):
            print(j[h],l1,l2,l3,len(j))
            if j[h] in line1:
                l1 += 1
            elif j[h] in line2:
                l2 += 1
            elif j[h] in line3:
                l3 += 1
        if(len(j) == l1 or len(j) == l2 or len(j) == l3):
            arr.append(words[i])
        l1 = 0
        l2 = 0
        l3 = 0

    print(arr)
    return arr 
  
if __name__ == '__main__':
    main()
    