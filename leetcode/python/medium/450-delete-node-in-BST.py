class Solution:
    def deleteNode(self, root, key):
        root = self.deleteHelper(root, key)
        return root
    
    def deleteHelper(self, node, key):
        if not node:
            return None
        if node.val == key:
            if not node.left and not node.right: 
                return None 
            if node.left and not node.right:
                return node.left
            if node.right and not node.left: 
                return node.right
            else:
                newVal = self.findSuccessor(node.right)
                node.val = newVal
                node.right = self.deleteHelper(node.right, newVal) 
                return node

        if node.val > key: 
            node.left = self.deleteHelper(node.left, key)
        if node.val < key: 
            node.right = self.deleteHelper(node.right, key)
        return node
    
    def findSuccessor(self, node):
        while (node.left): 
            node = node.left
        return node.val