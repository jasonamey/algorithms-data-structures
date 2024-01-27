import sys

class EdgeWeight:
  def __init__(self, v, w, weight):
    self.v = v
    self.w = w
    self.weight = weight 

  def __str__(self):
    return f"({self.v}, {self.w}, {self.weight})"
  
  def get_v(self):
    return self.v 
  
  def get_w(self): 
    return self.w
  
  def get_weight(self):
    return self.weight

class EdgeWeightGraph: 
  def __init__(self, size):
    self.edges = [[] for _ in range(size) ]
  
  def __str__(self):
    str_edges = ""
    for i in range(len(self.edges)):
      connections = ""
      for edge in self.edges[i]:
        connections += str(edge) + " "
      str_edges += f"{i}: [{connections.strip()}]\n"
    return str_edges[:-1]
  
  def add_edge(self, v, w, weight):
    edge = EdgeWeight(v,w, weight)
    self.edges[v].append(edge)
    self.edges[w].append(edge)

def create_edge_weight_graph(input):
  def process_edge(item):
    arr = item.split()
    n1, n2 = int(arr[0]), int(arr[1])
    min_n, max_n = min(n1, n2), max(n1, n2)
    return (min_n, max_n, float(arr[2]))
  raw_data = input.split('\n')
  size = int(raw_data[0])
  data = list(map(process_edge, raw_data[1:]))
  ewg = EdgeWeightGraph(size)
  for edge in data:
    ewg.add_edge(*edge)
  return ewg

if __name__ == "__main__":
  graph_input = sys.stdin.read()
  edge_weight_graph = create_edge_weight_graph(graph_input)
