"""
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
 then sum node values up as the new value of the merged node. 
 Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.
"""

import os
import sys


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        return t1

"""
        if(t1 and t2):
            root = TreeNode(t1.val + t2.val)
            root.left =  self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2
"""

def main():
    null = 0
    t1 = [1,3,2,5]
    t2 = [2,1,3,null,4,null,7]

    Solution.mergeTrees(t1, t2)

if __name__ == '__main__':
    main()
    