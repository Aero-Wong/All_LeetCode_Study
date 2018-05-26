"""
Description:
Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""

import os 
import sys

def zhishu(n):
    
    arr = []

    if(n <= 1):
        #print("0")
        return 0
    else:
        for i in range(1, n):
            #print("num: ", i)
            if(i > 1):
                for j in range(2, i):
                    #print("i: ", i, "j: ", j)
                    if(i != j and i % j == 0):
                        break
                    else:
                        #print(i,"是质数")
                        arr.append(i) 
            if(i == 2):
                arr.append(i)

        arr = list(set(arr))
        #print(len(arr))
        #return len(arr)
    print("一共",len(arr),"个质数，","分别",arr)
   

def main():
    
    for i in range(0):
        zhishu(i)
    
if __name__ == '__main__':
    main()
    