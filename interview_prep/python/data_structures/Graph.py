# class Graph: 
#     def __init__(self): 
#         self.nodes = {} 
#     def __repr__(self): 
#         return str(self.nodes)
#     def add(self, node_one, node_two):
#         if node_one in self.nodes: 
#             if node_two not in self.nodes[node_one]:
#                 self.nodes[node_one].append(node_two)
#         else: 
#             self.nodes[node_one] = [node_two]
#         if node_two in self.nodes:
#             if node_one not in self.nodes[node_two]:
#                 self.nodes[node_two].append(node_one)
#         else: 
#             self.nodes[node_two] = [node_one]
#     def size(self):
#         return len(self.nodes)
#     def explore_nodes(self):
#         max_node = max(list(self.nodes.keys()))
#         visited = [False for _ in range(max_node + 1)]
#         history = []
#         def dfs(node):
#             if visited[node]:
#                 return 
#             visited[node] = True
#             history.append(node)
#             for neighbor in self.nodes[node]:
#                 dfs(neighbor)
#         dfs(0)
#         return(history)
        
# g = Graph()
# g.add(4,3)
# a =[[0,1],[1,2],[1,3],[1,4],[2,3],[2,6],[4,5],[4,8],[3,4],[6,7]]
# for edge in a: 
#     g.add(*edge)
# print(g.explore_nodes())

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def __str__(self):
        return str(self.graph)
    def add(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def solution(self, s,e):
        visited = [False for _ in range(len(self.graph) + 1)]
        prev = [None for _ in range(len(self.graph) + 1)]
        def bfs(node):
            q = []
            q.append(node)
            visited[node] = True
            while (q):
                new_node = q.pop(0)
                for neighbor in self.graph[new_node]:
                    if not visited[neighbor]:
                        q.append(neighbor)
                        prev[neighbor] = new_node
                        visited[neighbor] = True
        bfs(s)  
        return prev        
           
g = Graph()
a = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[1,11]]

for edge in a:
    g.add(*edge)
print(g.solution(1,11))