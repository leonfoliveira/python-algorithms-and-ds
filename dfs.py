# Avoid visiting nodes more than once
# Not necessary for threes
visited = set()
graph = []

# Traverse a graph by depth
def dfs(node):
	global visited
	visited.add(node)
	for child in graph[node]:
		if child not in visited:
			dfs(child)
