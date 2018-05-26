"""
Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

import os
import sys
import random

def main():
    nums = [1,2,3]

    random.shuffle(nums)
    print(nums)

    nums.sort()
    print(nums)


if __name__ == '__main__':
    main()
    