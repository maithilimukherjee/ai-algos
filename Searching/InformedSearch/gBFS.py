import heapq

def greedy_best_first_search(problem, heuristic):
    """
    Greedy Best-First Search.
    problem must define:
      - INITIAL_STATE
      - GOAL_TEST(state)
      - ACTIONS(state)
      - CHILD_NODE(state, action)
    heuristic: function h(state) that estimates cost from state to goal.
    """

    # Priority queue ordered by h(n)
    frontier = []
    start_node = (problem.INITIAL_STATE, [], 0)
    heapq.heappush(frontier, (heuristic(start_node[0]), start_node))

    explored = set()

    while frontier:
        _, (state, path, cost) = heapq.heappop(frontier)

        if problem.GOAL_TEST(state):
            return path

        explored.add(state)

        for action in problem.ACTIONS(state):
            child_state, step_cost = problem.CHILD_NODE(state, action)
            if child_state not in explored:
                child_path = path + [action]
                heapq.heappush(frontier, (heuristic(child_state), (child_state, child_path, cost + step_cost)))

    return None  # failure

class GraphProblem:
    def __init__(self):
        self.INITIAL_STATE = 'Arad'
        self.goal = 'Bucharest'
        self.graph = {
            'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
            'Sibiu': ['Fagaras', 'Rimnicu'],
            'Zerind': ['Oradea'],
            'Timisoara': ['Lugoj'],
            'Fagaras': ['Bucharest'],
            'Rimnicu': ['Pitesti'],
            'Pitesti': ['Bucharest'],
            'Oradea': [],
            'Lugoj': [],
            'Bucharest': []
        }

        # Straight-line distance heuristic (example values)
        self.hSLD = {
            'Arad': 366, 'Sibiu': 253, 'Zerind': 374, 'Timisoara': 329,
            'Fagaras': 176, 'Rimnicu': 193, 'Pitesti': 100,
            'Oradea': 380, 'Lugoj': 244, 'Bucharest': 0
        }

    def GOAL_TEST(self, state):
        return state == self.goal

    def ACTIONS(self, state):
        return self.graph.get(state, [])

    def CHILD_NODE(self, state, action):
        return action, 1  # step cost = 1 for simplicity

    def heuristic(self, state):
        return self.hSLD.get(state, float('inf'))
