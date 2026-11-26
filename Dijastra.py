
# Dijkstra's Algorithm

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 4, 'D': 3},
    'D': {'B': 1, 'C': 3}
}

start = input("Enter starting node: ")
end = input("Enter destination node: ")

distance = {node: float('inf') for node in graph}
distance[start] = 0

visited = []
previous = {}

while len(visited) < len(graph):

    current = None

    for node in graph:
        if node not in visited:
            if current is None or distance[node] < distance[current]:
                current = node

    if current is None or distance[current] == float('inf'):
        break

    visited.append(current)

    for neighbour, cost in graph[current].items():

        new_distance = distance[current] + cost

        if new_distance < distance[neighbour]:
            distance[neighbour] = new_distance
            previous[neighbour] = current

# Display shortest path

if distance[end] == float('inf'):
    print("No path found")

else:
    path = []
    node = end

    while node != start:
        path.append(node)
        node = previous[node]

    path.append(start)
    path.reverse()

    print("Shortest path:", " -> ".join(path))
    print("Minimum cost:", distance[end])
