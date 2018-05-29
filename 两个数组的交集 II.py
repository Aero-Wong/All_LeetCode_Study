import os
import sys

def main():
    #nums1 = [1, 2, 2, 1]
    #nums2 = [2, 2]
    #nums2 = [2]
    nums1 = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
    nums2 = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]

    cross = []
    tmp = 0
    i = 0

    nums1.sort()
    nums2.sort()

    print(nums1)
    print(nums2)

    while(i < len(nums1)):
        print("i:",i)
        j = 0
        while(j < len(nums2)):
            print("j:",j)
            print("nums1[i]:",nums1[i],"nums2[j]:",nums2[j])
            if(nums1[i] == nums2[j] and tmp <= len(nums2)):
                cross.append(nums2[j])
                tmp += 1
                print(cross)
                break
            j += 1
        i += 1
    print(cross)

"""    
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
    """

if __name__ == '__main__':
    main()