import sys
from Graph import create_graph

class TopologicalSort: 
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False for _ in range(len(self.graph.adj))]
    self.stack = []

  def dfs(self, v): 
    self.visited[v] = True
    for w in self.graph.adj[v]:
      if not self.visited[w]:
        self.dfs(w)
        self.stack.append(w)
  
  def get_top_sort(self):
    for v in range(len(self.graph.adj)):
      if not self.visited[v]:
        self.dfs(v)
        self.stack.append(v)
    return list(reversed(self.stack))

if __name__ == "__main__":
  #python3 TopologicalSearch.py < data/graph_one.txt
  input_string = sys.stdin.read()
  graph = create_graph(input_string)
  t_sort = TopologicalSort(graph)
  print(t_sort.get_top_sort())