graph = {5: {7: 4, 3: 2}, 7: {5: 4, 4: 2, 3: 3}, 4: {7: 2, 8: 4, 2: 1}, 3: {5: 2, 7: 3, 8: 7}, 8: {3: 7, 4: 4, 2: 2}, 2: {4: 1, 8: 2}}
start, end = 5, 2
queue = [start, ]
min_cost = {key: float('inf') for key in graph}
min_cost_list = {}
min_cost[start] = 0
visited = []
i = 0
while i < len(queue):
    Node = queue[i]
    visited.append(Node)
    for node in graph[Node]:
        if node not in visited:
            queue.append(node)
            mincost = float('inf')
            for next_node in graph[node]:
                if min_cost[next_node] < mincost:
                    mincost = min_cost[next_node] + graph[node][next_node]
                    parent_node = next_node
            min_cost[node] = mincost
            min_cost_list[node] = parent_node
    i += 1
ans = [end]
mincost = min_cost[end]
while start != end:
    end = min_cost_list[end]
    ans.append(end)
print('Min Cost Path: ', end = '')
print(*ans[::-1], sep = '-> ')
print('Min Cost:',mincost)