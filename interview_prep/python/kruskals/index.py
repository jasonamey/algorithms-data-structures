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

  def isConnected(self, n1, n2):
    root1 = self.find(n1)
    root2 = self.find(n2)
    return root1 != -1 and root1 == root2 
 
def kruskals(graph):
  edge_list = []
  for idx in range(len(graph)):
      for edge in graph[idx]:
        edge_list.append([idx,edge[0],edge[1]])
  sorted_edge_list = sorted(edge_list, key=lambda x: x[2])
  sorted_edge_list = sorted_edge_list[0::2]
  edges_set = UnionFind(len(graph))
  ans = [[] for _ in range(len(graph))]
  for edge in sorted_edge_list:
    if not edges_set.isConnected(edge[0], edge[1]):
      edges_set.union(edge[0], edge[1])
      ans[edge[0]].append([edge[1], edge[2]])
      ans[edge[1]].append([edge[0], edge[2]])
  return ans

edges = [
    [
      [1, 3],
      [2, 5]
    ],
    [
      [0, 3],
      [2, 10],
      [3, 12]
    ],
    [
      [0, 5],
      [1, 10]
    ],
    [
      [1, 12]
    ]
  ]

# edges = [
#     #0
#     [
#       [1, 1],
#       [2, 2]
#     ],
#     #1
#     [
#       [4, 2],
#       [2, 4],
     
#     ],
#     #2
#     [
#       [0, 2],
#       [1, 4],
#       [4, 3],
#       [3, 1]
#     ],
#     # 3
#     [
#       [2, 1],
#       [4, 7],
#       [5, 5]
#     ],
#     #4
#      [
#       [1, 2],
#       [6, 4],
#       [5, 2],
#       [3, 7],
#       [2, 3]
#     ],
#     # 5
#      [
#       [7, 1],
#       [4, 2],
#       [3, 5],
#     ],
#     # 6
#      [
#       [7, 8],
#       [4, 4]
#     ],
#     # 7
#      [
#       [5, 1],
#       [6, 8]
#     ],
#   ]
