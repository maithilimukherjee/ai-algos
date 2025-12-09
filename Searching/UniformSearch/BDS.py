from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # queues for forward and backward search
    forward_q = deque([start])
    backward_q = deque([goal])

    # visited sets
    forward_visited = {start: None}
    backward_visited = {goal: None}

    while forward_q and backward_q:
        # expand forward
        current_f = forward_q.popleft()
        for neighbor in graph.get(current_f, []):
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current_f
                forward_q.append(neighbor)

                if neighbor in backward_visited:
                    return build_path(neighbor, forward_visited, backward_visited)

        # expand backward
        current_b = backward_q.popleft()
        for neighbor in graph.get(current_b, []):
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current_b
                backward_q.append(neighbor)

                if neighbor in forward_visited:
                    return build_path(neighbor, forward_visited, backward_visited)

    return None


def build_path(meeting_node, forward_visited, backward_visited):
    # build forward path
    path_f = []
    node = meeting_node
    while node is not None:
        path_f.append(node)
        node = forward_visited[node]
    path_f.reverse()

    # build backward path
    path_b = []
    node = backward_visited[meeting_node]
    while node is not None:
        path_b.append(node)
        node = backward_visited[node]

    return path_f + path_b
