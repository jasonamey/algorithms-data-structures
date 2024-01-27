import heapq
import sys

class Prims: 
  def __init__(self, graph, start):
    self.graph = graph
    self.start = start
    self.tree = self.solve()

  def __str__(self):
    result = ""
    for edge in list(self.tree):
      result += f"{edge}\n"
    return result.strip()
   
  def solve(self):
    tree = set() 
    visited = [False for _ in range(self.graph.size)]
    edges = []
    heapq.heapify(edges)
    edge = self.graph.edges[self.start][0]
    while not all(visited):
      while visited[edge.v] and visited[edge.w]: 
        edge = heapq.heappop(edges)
      if not visited[edge.v]:
        visited[edge.v] = True
        tree.add(edge)
        for edge_test in self.graph.edges[edge.v]:
          heapq.heappush(edges, edge_test)
      if not visited[edge.w]:
        visited[edge.w] = True
        tree.add(edge)
        for edge_test in self.graph.edges[edge.w]:
          heapq.heappush(edges, edge_test)
    return tree
        
class Edge: 
  def __init__(self, v, w, weight):
    self.v = v
    self.w = w
    self.weight = weight 

  def __lt__(self, other):
    return self.weight < other.weight
  
  def __str__(self): 
    return f"({self.v}, {self.w}, {self.weight})"

class Graph: 
  def __init__(self, edges):
    self.size = self.calculate_size(edges)   
    self.edges = self.create_adj_list(edges)
                    
  def __str__(self): 
    graph = ""
    for idx in range(len(self.edges)):
      edge_list = ""
      for edge in self.edges[idx]:
        edge_list += f"({edge.v} {edge.w} {edge.weight})"  
      graph += f"{idx}: {edge_list}\n"
    return graph.strip()

  def create_adj_list(self, edges):
    adj_list = [[] for _ in range(self.size)]
    for edge in edges:
      adj_list[edge.v].append(edge)
      adj_list[edge.w].append(edge)
    return adj_list 
  
  def calculate_size(self,edges):
    vertexes = set()
    for edge in edges:
      vertexes.update([edge.v, edge.w])
    return len(vertexes)

def create_graph(input,num): 
  raw_input = input.split("\n")
  data = []
  for item in raw_input:
    data.append(Edge(*(map(int,item.split()))))
  graph = Graph(data)
  return graph

if __name__ == "__main__":
  input_string = sys.stdin.read().strip()
  graph = create_graph(input_string, 1)
  prims = Prims(graph, 0)
  assert len(prims.tree) == graph.size - 1


