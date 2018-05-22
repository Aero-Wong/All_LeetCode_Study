import sys

def main():
    #nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    tmp = 0

    for i in range(1,len(nums)):
        if(nums[i] != nums[tmp]):
            tmp += 1
            nums[tmp] = nums[i]
            print(nums,tmp)
            
    del nums[tmp+1:len(nums)]

    print(nums)
    print(tmp)
    return tmp

if __name__ == '__main__':
    main()
    