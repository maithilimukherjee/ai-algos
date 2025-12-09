class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def path(self):
        result = []
        node = self
        while node is not None:
            result.append(node.state)
            node = node.parent
        return result[::-1]


def dfs(problem, initial_state, goal_state):
    frontier = [Node(initial_state)]
    explored = set()

    while frontier:
        node = frontier.pop()  # stack behavior

        if node.state == goal_state:
            return node.path()

        explored.add(node.state)

        for neighbor in problem.get(node.state, []):
            if neighbor not in explored and all(n.state != neighbor for n in frontier):
                frontier.append(Node(neighbor, node))

    return None
