graph = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
start, end = 5, 2
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