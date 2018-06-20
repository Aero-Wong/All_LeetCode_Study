"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
 

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        #判断根为空
        if (root == None):
            return []
        #左边移
        arr += self.inorderTraversal(root.left)
        #压入数组
        arr.append(root.val)
        arr += self.inorderTraversal(root.right)
        
        return arr
 