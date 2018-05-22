import os
import sys


def main():
    nums = [0,1,0,3,12]
    tmp = 0
    for i in range(0,len(nums)):
        print(i,nums[i])
        if(nums[i] != 0):
            nums[tmp] = nums[i]
            tmp += 1
        print(nums)
        
    for j in range(tmp,len(nums)):
        nums[j] = 0
    
    print(nums)
    return nums

if __name__ == '__main__':
    main()
    