/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

include "stdio.h"

int* twoSum(int* nums, int numsSize, int target) {
    int *arr = malloc(sizeof(int)*2);
    for(int i = 0; i < numsSize - 1; i++)
    {
        for(int j = i + 1; j < numsSize; j++)
        {
            if(nums[i] + nums[j] == target)
            {
                arr[0] = i;
                arr[1] = j;
                return arr;
            }
        }
    }
    return arr;
}

int main(void)
{
    int nums = [2, 7, 11, 15];
    int target = 9;
    int numsSize = 4;

    twoSum(nums,numsSize,target);
}