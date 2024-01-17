def topologicalSort(jobs, deps):
    visited = [False for _ in range(len(jobs) + 1)]
    graph = create_graph(jobs, deps)
    print(graph)
    ans = []
    for job in jobs: 
        dfs(job, visited, graph, ans)
       
    print(ans)

def dfs(job, visited, graph, ans):
  for node in graph[job]:
      if not visited[node]:
        dfs(node, visited, graph, ans) 
  visited[job] = True
  if job not in ans:
    ans.append(job)

def create_graph(jobs, deps): 
  graph = { k :[] for k in range(1, len(jobs) + 1 )}
  for n1, n2 in deps: 
    graph[n2].append(n1)
  return graph  
 

jobs = [1, 2, 3, 4]
deps = [
    [1, 2],
    [1, 3],
    [3, 2],
    [4, 2],
    [4, 3]
  ]
print(topologicalSort(jobs,deps))

