from sys import stdin
from Graph import create_graph

class ConnectedComponents:
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False for _ in range(len(graph.adj))]
    self.components = [None for _ in range(len(graph.adj))]
    self.find_components()
  
  def find_components(self):
    component = 0 
    for v in range(len(self.graph.adj)):
      if not self.visited[v]:
        self.dfs(v, component)
        component += 1

  def dfs(self, v, component):
    self.visited[v] = True
    self.components[v] = component
    for w in self.graph.adj[v]:
      if not self.visited[w]:
        self.dfs(w, component)
  
  def get_num_components(self):
    return len(set(self.components))

if __name__ == "__main__":
  input_string = stdin.read()
  graph = create_graph(input_string)
  connected_components = ConnectedComponents(graph)