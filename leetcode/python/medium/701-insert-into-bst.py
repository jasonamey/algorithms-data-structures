# Definition for a binary tree node.

# You are given the root node of a binary search tree (BST) and a value to insert 
# into the tree. Return the root node of the BST after the insertion. It is 
# guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        root = self.insertHelper(root, val)
        return root

    def insertHelper(self, node, val):
        if node is None: 
            return TreeNode(val)
        elif node.val > val: 
            node.left = self.insertHelper(node.left, val)
        else:
            node.right = self.insertHelper(node.right, val)
        return node
    
    
        