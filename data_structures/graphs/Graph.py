import sys

class Graph: 
    def __init__(self, size): 
        self.adj = [[] for _ in range(size)]
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
class Path:
    def __init__(self, graph, v):
        self.graph = graph 
        self.v = v
        self.visited = [False for _ in range(len(graph.adj))]
        self.paths = self.get_paths()
          
    def dfs(self, v, paths):
        self.visited[v] = True
        for w in self.graph.adj[v]:
            if not self.visited[w]: 
                self.dfs(w, paths)
                paths[w] = v

    def get_paths(self):
        paths = [None for i in range(len(graph.adj))]
        paths[self.v] = -1
        self.dfs(self.v, paths)
        return paths
    
    def has_path_to(self, v):
        return self.paths[v] is not None
    
    def path_to(self,v):
        if self.has_path_to(v):
          path = [v]
          vertex = self.paths[v]
          path.append(vertex)
          while self.paths[vertex] != -1:
              vertex = self.paths[vertex]
              path.append(vertex)
          path.reverse()
          return path
        else:
            raise Exception("no path exists")
              
def create_graph(input):
    edges = input.split('\n')
    graph = Graph(int(edges[0]))
    for i in range(1, len(edges)):
        v, w = tuple(map(int,edges[i].split()))
        graph.addEdge(v,w)
    return graph

if __name__ == "__main__": 
  #python3 Graph.py < data/graph_one.txt
  input_string = sys.stdin.read()
  graph = create_graph(input_string)
  path = Path(graph, 8)
  print(path.path_to(7))
