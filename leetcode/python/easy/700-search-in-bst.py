# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        if (root.val == val):
            return root
        elif (root.left is None and root.right is None):
            return None
        elif (root.left and val < root.val):
            return self.searchBST(root.left, val)
        else:
            if (root.right and val > root.val): 
                return self.searchBST(root.right, val)

