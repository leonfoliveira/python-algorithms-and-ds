from collections import *

graph = []

# Traverse a graph by breadth
def bfs(source, edge_weight):
	queue = deque()
	dist = defaultdict(lambda: float('inf')
	visited = set()
	
	queue.append(source)
	dist[source] = 0
	while len(queue) > 0:
		node = queue.popleft()
		visited.add(node)
		for child in graph[node]:
			if child not in visited and dist[child] > dist[node] + edge_weight:
				dist[child] = dist[node] + edge_weight
				queue.append(child)
	
	return dist
