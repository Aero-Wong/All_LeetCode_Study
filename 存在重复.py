import os
import sys

def main():
    #nums = [1,2,3,1]
    #nums = [1,2,3,4]
    nums = [1,1,1,3,3,4,3,2,4,2]

    nums.sort()
    print(nums)
    tmp = 0
    for i in range(1,len(nums)):
        if(nums[i] == nums[i-1]):
            tmp += 1
            print(tmp)
    
    if(tmp > (len(nums)) / 2):
        print("true")
    else:
        print("false")
        

"""
    num = 0
    for i in range(0,len(nums)):
        tmp = 0
        for j in range(0,len(nums)):
            print(i,nums[i],j,nums[j])
            if(nums[i] == nums[j] and i != j):
                tmp += 1
    if(tmp == 0):
        print("False")
    else:
        print("True")
"""

"""    
    num = 0
    tmp = 0
    for i in nums:
        num = num ^ i
        print(num)
        print("true")
        return True
    
    print("False")
    return False
"""

    
if __name__ == '__main__':
    main()