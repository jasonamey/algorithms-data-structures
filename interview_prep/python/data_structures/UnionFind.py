class UnionFind: 
  def __init__(self, N):
    self.nodes = [-1 for _ in range(N)]
    self.heights = [1 for _ in range(N)]

  def __str__(self):
    return f"nodes: {self.nodes}, heights: {self.heights}"

  def find(self, n):
    if self.nodes[n] == -1:
      return n
    self.nodes[n] = self.find(self.nodes[n])
    return self.nodes[n]

  def union(self, n1, n2):
    root1 = self.find(n1)
    root2 = self.find(n2)
    if self.heights[root1] > self.heights[root2]:
      self.nodes[root2] = root1
      self.heights[root1] += self.heights[root2]
    else : 
      self.nodes[root1] = root2
      self.heights[root2] += self.heights[root1]



    