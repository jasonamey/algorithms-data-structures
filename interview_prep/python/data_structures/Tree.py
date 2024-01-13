class Tree: 
    def __init__(self, val): 
        self.val = val 
        self.right = None 
        self.left = None
        
    def __str__(self):
        return f"[val: {self.val} L: {self.left} R: {self.right}]"
        
    def getSum(self): 
        if not self.right and not self.left:
            return self.val 
        left = 0
        right = 0
        if self.left:
            left = self.left.getSum()
        if self.right: 
            right = self.right.getSum()
        return left + right 
        
    def getHeight(self): 
        if not self.left and not self.right: 
            return 0 
        left = 0 
        right = 0 
        if self.left:
            left = 1 + self.left.getHeight()
        if self.right: 
            right = 1 + self.right.getHeight()
        return max(left, right)
                 
a = [0,1,2,3,4,5,6,7,8,9,10]

nodes = [None]
for i in range(1,len(a)): 
    nodes.append(Tree(a[i]))

for idx, node in enumerate(nodes):
    if idx == 0: 
        continue
    if idx * 2 + 1 < len(nodes):
        node.right = nodes[idx * 2 + 1]
    if idx * 2 < len(nodes):
        node.left = nodes[idx * 2]


print(nodes[1].getHeight())
