graph = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8 ,2], 3: [5, 7, 8], 8: [3, 4, 2], 2: [4, 8]}
start, end = 5, 2
paths = []
queue = [(start, [])]
i = 0
while i < len(queue):
    Node, path= queue[i]
    if Node not in path:
        if Node == end:
            paths.append(path + [Node])
            i += 1
            continue
        for node in graph[Node]:
            queue.append((node, path + [Node]))
    i += 1
for path in paths:
    print(*path, sep = '->')  