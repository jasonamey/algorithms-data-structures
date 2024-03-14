# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        if not root or (not root.left and not root.right):
            return 0
        q = [root]
        diameter = 0
        while q:
            node = q.pop()
            left = 0
            right = 0
            if node.left:
                left = 1 + self.heightOfNode(node.left)
                q.append(node.left)
            if node.right:
                right = 1 + self.heightOfNode(node.right)
                q.append(node.right)
            test = left + right
            diameter = test if test > diameter else diameter
        return diameter

    def heightOfNode(self, node):
        right = 0 if not node.right else self.heightOfNode(node.right) + 1
        left = 0 if not node.left else self.heightOfNode(node.left) + 1
        return max(right, left)
