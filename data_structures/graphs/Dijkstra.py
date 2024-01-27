import sys

class EWGGraph: 
  def __init__(self, edges):
    self.edges = edges

def process_input_for_edges(input):
  edges = [[] for _ in range(int(input[0]))]
  edges_input = input.split('\n')[1:]
  for edge in edges_input:
    items = edge.split()
    v,w,weight = int(items[0]), int(items[1]), float(items[2])
    edges[v].append((w, weight))
    edges[w].append((v, weight))
  return edges

class Dijkstra: 
  def __init__(self, graph, v):
    self.edges = graph.edges
    self.v = v
    self.distances = self.solve()
  
  def __str__(self):
    answer = ""
    for i, distance in enumerate(self.distances):
      if i == 0:
        continue
      answer += f"distance from {self.v} to {i} is {distance}\n"
    return answer.strip()
    
  def solve(self):
    self.visited = [False for _ in range(len(self.edges))]
    distances = [float("inf") for _ in range(len(graph.edges))]
    distances[self.v] = 0
    q = [self.v]
    while q:
      w = q.pop(0)
      self.visited[w] = True
      for edges in self.edges[w]:
        to = edges[0]
        if not self.visited[to]:
          to_distance = edges[1]
          test = to_distance + distances[w]
          distances[to] = min(test, distances[to])
          q.append(to)
    return distances
      
if __name__ == "__main__":
  #python3 Dijkstra.py < data/ewg.txt
  input_string = sys.stdin.read()
  edges = process_input_for_edges(input_string)
  graph = EWGGraph(edges)
  d = Dijkstra(graph, 0)
  print(d)