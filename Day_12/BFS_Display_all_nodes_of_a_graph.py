graph = {10: [7, 4], 7: [10, 5, 9], 4: [10, 5], 5: [7, 4, 6], 9: [7, 2], 6: [5], 2: [9]}
visited = []
queue = [5]
i = 0
while i < len(queue):
    node = queue[i]
    for nextnode in graph[node]:
        if nextnode not in queue:
            queue.append(nextnode)
            
    i += 1
print(*queue)