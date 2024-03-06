# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest 
# path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root) -> int:
        if not root: 
            return 0
        count = 1
        q = [root]
        while q: 
            for _ in range(len(q)):
                node = q.pop(0) 
                if not node.left and not node.right: 
                    return count
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            count += 1