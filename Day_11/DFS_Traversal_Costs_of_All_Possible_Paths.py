graph = {5: [(7, 4), (3, 2)], 7: [(5, 4), (4, 2), (3, 3)], 4: [(7,2), (8, 4) ,(2, 1)], 3: [(5, 2), (7, 3), (8, 7)], 8: [(3, 7), (4, 4), (2, 2)], 2: [(4, 1), (8, 2)]}
start, end = 5, 2
paths = []
path_cost = []
def Traversal(Node = start, visited = [], path = [], cost = 0):
    if Node not in visited:
        if Node == end:
            paths.append(path[:] + [Node])
            path_cost.append(cost)
            return
        for node in graph[Node]:
            pnode, ncost = node
            Traversal(pnode, visited + [Node], path + [Node], cost + ncost)
Traversal()
for i in range(len(paths)):
    print(*paths[i], sep = '->', end = ': ')
    print(path_cost[i])