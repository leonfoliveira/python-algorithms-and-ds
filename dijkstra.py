from collections import *
from heapq import *

graph = []

def dijkstra(source):
	heap = []
	dist = defaultdict(lambda: float('inf'))
	visited = set()
	
	heappush(heap, (0, source))
	dist[source] = 0
	while len(heap) > 0:
		node = heappop(heap)[1]
		visited.add(node)
		for child_dist, child in graph[node]:
			if child not in visited and dist[child] > dist[node] + child_dist:
				dist[child] = dist[node] + child_dist
				heappush(heap, (dist[child], child))
	
	return dist
