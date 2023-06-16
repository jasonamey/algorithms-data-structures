class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    helper(root, 0, sums)
    return sums

def helper(tree, curSum, sums): 
    if tree.left is None and tree.right is None: 
        sums.append(curSum + tree.value)
        return 
    else: 
        if tree.left is not None: 
            helper(tree.left, curSum + tree.value, sums)
        if tree.right is not None: 
            helper(tree.right, curSum + tree.value, sums)