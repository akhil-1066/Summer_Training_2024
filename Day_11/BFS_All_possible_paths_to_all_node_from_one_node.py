graph = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
start = 5
all_nodes = []
def allnodes(node = start):
    if node not in all_nodes:
        all_nodes.append(node)
        for nextnode in graph[node]:
            allnodes(nextnode)
allnodes()
for end in all_nodes[1:]:
    end = 2
    paths = []
    def Traversal(Node = start, visited = [], path = []):
        if Node not in visited:
            if Node == end:
                paths.append(path[:] + [Node])
                return
            for node in graph[Node]:
                Traversal(node, visited + [Node], path + [Node])
    Traversal()
    for path in paths:
        print(*path, sep = '->')    
