import sys
from UnionFind import UnionFind
from EdgeWeightGraph import create_edge_weight_graph, EdgeWeight
import heapq

class Kruskals:
  def __init__(self, graph):
    self.graph = graph
    self.pq = Kruskals.process_graph(graph.edges)
    self.union = UnionFind(graph.size)
    self.answer = Kruskals.solve(self.pq, self.union)
  
  @staticmethod
  def process_graph(edges_list):
    collection = set()
    for edges in edges_list:
      for edge in edges:
        copy = (edge.v, edge.w, edge.weight)
        if edge.v > edge.w:
          copy = (edge.w, edge.v, edge.weight)
        collection.add(copy)
    pq = [EdgeWeight(*item) for item in collection]
    heapq.heapify(pq)
    print(pq)
    return pq
  
  @staticmethod
  def solve(pq, unions):
    ans = []
    while not unions.all_connected():
      edge = heapq.heappop(pq)
      if not unions.connected(edge.v, edge.w):
        unions.union(edge.v, edge.w)
        ans.append(edge)
    return ans

if __name__ == "__main__":
  
  input_string = sys.stdin.read()
  ewg = create_edge_weight_graph(input_string)
  k = Kruskals(ewg)
  for i in k.answer:
    print(i)

  