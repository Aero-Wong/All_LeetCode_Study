import os
import sys

def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    cross = []  
    tmp = 0
    if(len(nums1) > len(nums2)):
        for i in range(0,len(nums2)):
            for j in range(0,len(nums1)):
                print(i,nums2[i],j,nums1[j])
                if(nums2[i] == nums1[j]):
                    cross.append(nums2[i])
                    j += 1
                    if(i<len(nums2)):
                        i += 1
                    print(cross,i,j)

    elif(len(nums1) < len(nums2)):
        for i in range(0,len(nums2)):
            print(i,nums2[i])

    print(cross)
    return cross

if __name__ == '__main__':
    main()