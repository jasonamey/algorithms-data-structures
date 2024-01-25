import sys
from Graph import create_graph
from collections import deque

class BreadthFirstPaths:
  def __init__(self, graph, v):
    self.v = v
    self.graph = graph
    self.visited = [False for _ in range(len(graph.adj))]
    self.distance = [None for _ in range(len(graph.adj))]
    self.paths = [-1 for _ in range(len(graph.adj))]
    self.bfs()

  def bfs(self):
    q = deque()
    q.append(self.v)
    distance = 0
    while q: 
      num_items = len(q)
      for i in range(0, num_items):
        item = q.popleft()
        self.visited[item] = True
        self.distance[item] = distance
        for w in self.graph.adj[item]:
          if not self.visited[w]:
            self.paths[w] = item
            q.append(w)
      distance += 1

if __name__ == "__main__":
  #python3 BreadthFirstPaths.py < graph_one.txt
  input_string = sys.stdin.read()
  graph = create_graph(input_string)
  bfp = BreadthFirstPaths(graph, 0)
 


  