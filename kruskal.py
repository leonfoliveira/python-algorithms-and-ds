root = []
graph = []

def findset(node):
	if root[node] == node:
		return node
	root[node] = findset(root[node])
	return root[node]

def initset():
	root = [i for i in range(len(graph))]

def kruskal():
	initset()
	graph.sort()
	
	tree = []
	total = 0
	for node in range(len(graph)):
		source, destiny, weight = graph[node]
		
		source_root = findset(source)
		destiny_root = findset(destiny)
		if source_root != destiny_root:
			root[source_root] = destiny_root
			total += weight
			tree[source].append(destiny)
