
"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
"""

import sys
import os

def main():
    #s = "leetcode"
    #s = ""
    s = "aa"
    #return 0.
    #s = "loveleetcode"
    #return 2.

    s1 = {}

    for i in s:
        if s1.get(i):
            print("i:",i,"s1:",s1)
            continue
        else:
            s1[i] = s.count(i)
        if(s1[i] == 1):
            print(s.find(i))
            return s.find(i)
    print(-1)
    return -1

"""    
    s1 = []

    if(s != ""):
        s1 = list(s)
        print("列表:",s1)
    else:
        print(-1)

    for i in range(0,len(s1)):
        tmp = 0
        for j in range(0,len(s1)):
            if(s1[i] == s1[j]):
                print("i:",i,"s1:",s1[i],"j:",j,"s1:",s1[j])
                tmp += 1
                print("tmp:",tmp)
        if(tmp == 1):
            print(i)
    print(-1)
"""

"""    
    tmp = ''
    arr = []
    s1 = []
    s2 = []
    arr1 = []

    if(s != ""):
        s2 = list(s)
        s1 = list(s)
        s2.sort()
        print("列表:",s2)
        tmp = s2[0]
        print("字母:",tmp)
    else:
        print(-1)

    for i in range(1,len(s2)):
        print("序号:",i)
        print("s1:",s2[i])
        if(tmp != s2[i]):
            tmp = s2[i]
        elif(tmp == s2[i]):
            arr.append(s2[i])
            print(arr)
            print(i)
        else:
            print(-1)
    print(arr)
    print(s1)
    
    for i in range(0,len(s1)):
        tmp = 0
        for j in range(0,len(arr)):
            if(s1[i] == arr[j]):
                print(i,s1[i],j,arr[j])
                tmp += 1
                print(tmp)
        if(tmp == 0 ):
            print(i)
    
    print(-1)
"""
"""
    if(len(s) == 0):
        return -1
    for i in range(len(s)):  
        if s[i] not in s[i+1:]:  
            print(i)
            return i 
"""
            
"""
    i = 0
    while(i < len(s)):
        if(s[i] == s[i + 1]):
            print(i)
            return i - 1
        elif(s[i] != s[i + 1]):
            i += 1
        else:
            print(-1)
            return -1
"""

if __name__ == '__main__':
    main()
    