import heapq

class Point(object): 
  def __init__(self, point, distance): 
    self.point = (point, distance)
  def __lt__(self, other): 
    return self.point[1] < other.point[1]
  def __str__(self): 
    return f"Point is {self.point[0]} with distance {self.point[1]}"

def dijkstra(end,graph):
  visited = [False for _ in range(len(graph))]
  distances = [float("inf") for _ in range(len(graph))]
  distances[0] = 0 
  pq = [Point(0,0)]
  heapq.heapify(pq)
  while len(pq) > 0: 
    idx, point_distance = heapq.heappop(pq).point
    visited[idx] = True
    for edge in graph[idx]:
      if not visited[edge[0]]:
        test_distance = edge[1] + point_distance  
        distances[edge[0]] = min(distances[edge[0]], test_distance)
        heapq.heappush(pq, Point(edge[0], distances[edge[0]]))
  return distances[end]

def dijkstra_start(start,graph):
  visited = [False for _ in range(len(graph))]
  distances = [float("inf") for _ in range(len(graph))]
  distances[start] = 0 
  pq = [Point(start,0)]
  heapq.heapify(pq)
  while len(pq) > 0: 
    idx, point_distance = heapq.heappop(pq).point
    visited[idx] = True
    for edge in graph[idx]:
      if not visited[edge[0]]:
        test_distance = edge[1] + point_distance  
        distances[edge[0]] = min(distances[edge[0]], test_distance)
        heapq.heappush(pq, Point(edge[0], distances[edge[0]]))
  for i in range(len(distances)):
    if distances[i] == float("inf"): 
      distances[i] = -1 
  return distances

g = [
  [
    [1, 7]
  ],
  [
    [2, 6],
    [3, 20],
    [4, 3]
  ],
  [
    [3, 14]
  ],
  [
    [4, 2]
  ],
  [],
  []
]

assert dijkstra_start(0, g) == [0, 7, 13, 27, 10, -1]