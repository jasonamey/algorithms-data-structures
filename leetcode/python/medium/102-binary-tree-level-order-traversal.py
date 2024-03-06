# Given the root of a binary tree, return the level order traversal of its nodes'
# values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
      order = []
      q = []
      q.append(root)
      while q:
        level = []
        newQ = []
        for node in q:
          level.append(node.val)
          if node.left: 
            newQ.append(node.left)  
          if node.right: 
            newQ.append(node.right)
        q = newQ
        order.append(level)
      return order

s = Solution()

#         0 
#     1       2
#   3   4   5
# tree structure : 
nodes = [TreeNode(val) for val in [0,1,2,3,4,5]]

nodes[0].left = nodes[1]
nodes[0].right = nodes[2]

nodes[1].left = nodes[3]
nodes[1].right = nodes[4]

nodes[2].left = nodes[5]

#

order = s.levelOrder(nodes[0])

assert order == [[0], [1, 2], [3, 4, 5]]
     