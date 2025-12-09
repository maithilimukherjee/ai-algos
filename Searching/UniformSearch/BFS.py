from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None


# sample graph
graph = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": [],
    "e": ["f"],
    "f": []
}

print(bfs(graph, "a", "e"))
