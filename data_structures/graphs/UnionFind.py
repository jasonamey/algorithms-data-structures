class UnionFind: 
  def __init__(self, size): 
    self.nodes = [-1 for _ in range(size)]
    self.heights = [1 for _ in range(size)]

  def union(self, n1, n2):
    root1 = self.find(n1)
    root2 = self.find(n2)
    if self.heights[n1] >= self.heights[n2]:
      self.nodes[root2] = root1
      self.heights[root1] += self.heights[root2]
    else: 
      self.nodes[root1] = root2
      self.heights[root2] += self.heights[root1]
  
  def connected(self, n1, n2): 
    return self.find(n1) == self.find(n2)

  def find(self, n):
    if self.nodes[n] == -1: 
      return n
    else: 
      self.nodes[n] = self.find(self.nodes[n])
    return self.nodes[n]
  
if __name__ == "__main__":
  u = UnionFind(10)
  u.union(0, 1)
  u.union(2, 3)
  u.union(3,4)
  u.union(4,5)
  
  