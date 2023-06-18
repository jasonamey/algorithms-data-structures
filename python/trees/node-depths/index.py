#INCORRECT SO FAR
def nodeDepths(root):
  depths = helper(root.left) + helper(root.right)
  return depths

def helper(tree, depth):
  if (tree is None):
    return 0
  return 1 + helper(tree.left) + helper(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None