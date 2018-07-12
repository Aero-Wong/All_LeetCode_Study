"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""

import os
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    tmp = 0
    if(p == null and q == null):
        return True

    if(p and q):
        if(p.val == q.val):
            return true
        p.right = self.isSameTree(p.right, q.right)
        p.left =  self.isSameTree(p.left, q.left)
 
    else:
        print("false")
        return False

def main():
    p = [1,2,1]
    q = [1,1,2]
    p = [1,2]
    q = [1,null,2]
    p = [1,2,3]
    q = [1,2,3]
    isSameTree(self, p, q)
        
if __name__ == '__main__':
    main()
    