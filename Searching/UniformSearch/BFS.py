from collections import deque

def breadth_first_search(problem):
    """
    Breadth-First Search algorithm.
    problem must define:
      - INITIAL_STATE
      - GOAL_TEST(state)
      - ACTIONS(state)
      - CHILD_NODE(state, action)
    """

    # Node structure: (state, path, path_cost)
    node = (problem.INITIAL_STATE, [], 0)

    if problem.GOAL_TEST(node[0]):
        return node[1]  # return path

    frontier = deque([node])   # FIFO queue
    explored = set()

    while frontier:
        state, path, cost = frontier.popleft()  # shallowest node
        explored.add(state)

        for action in problem.ACTIONS(state):
            child_state, child_cost = problem.CHILD_NODE(state, action)
            child_path = path + [action]

            if child_state not in explored and all(cs != child_state for cs, _, _ in frontier):
                if problem.GOAL_TEST(child_state):
                    return child_path
                frontier.append((child_state, child_path, child_cost))

    return None  # failure if frontier empty



class GraphProblem:
    def __init__(self):
        # Start at node 'A', goal is 'G'
        self.INITIAL_STATE = 'A'
        self.goal = 'G'
        # Graph adjacency list
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['G'],
            'F': [],
            'G': []
        }

    def GOAL_TEST(self, state):
        return state == self.goal

    def ACTIONS(self, state):
        return self.graph.get(state, [])

    def CHILD_NODE(self, state, action):
        # Each edge has cost 1
        return action, 1


# Run BFS
if __name__ == "__main__":
    problem = GraphProblem()
    solution = breadth_first_search(problem)
    print("Solution path:", solution)
