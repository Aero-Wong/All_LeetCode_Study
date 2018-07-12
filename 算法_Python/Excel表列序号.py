"""
Given a column title as appear in an Excel sheet, 
return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""

import os
import sys

def main():
    #s = "A"
    #s = "AB"
    s = "ZY"

    tmp = 1
    num = 0

    list(s)
    dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
            "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
            "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

    for i in range(len(s),1,-1):
        num += (dict.get(s[i-1]) - dict.get("A") + 1) * tmp
        tmp *= 26

    return num

"""  
    list(s)
    print(s)

    num1 = 0
    num2 = 0
    strs = ""
    j = 0
    abc = 0
    i = len(s)
    dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
            "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
            "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    
    print("i:",i,"j:",j)
    while(i > 0):
        strs = s[i-1]
        abc = 25 * j
        print(strs)
        num1 = dict.get(strs) + abc
        print("abc:",abc,"num1:",num1,"i:",i,"j:",j)
        abc = 0
        j += 1
        i -= 1      

    print("num:",num2)
    return num2 
"""



if __name__ == '__main__':
    main()