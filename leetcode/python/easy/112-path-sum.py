# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all 
# the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
      if root == None: 
        return False  
      newSum = targetSum - root.val
      if (root.left == None and root.right == None):
          if (newSum == 0):
              return True
          else: 
              return False
      left = self.hasPathSum(root.left, newSum) if root.left else False
      right = self.hasPathSum(root.right, newSum) if root.right else False
      return left or right


