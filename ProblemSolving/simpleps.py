from collections import deque

class simpleProblemSolvingAgent:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def formulate_problem(self):
        # Each action is stored as (label, function)
        return {
            "actions": [
                ("+1", lambda x: x + 1),
                ("-1", lambda x: x - 1),
            ]
        }

    def search(self, problem):
        queue = deque([(self.start, [])])
        visited = set()

        while queue:
            state, path = queue.popleft()

            # Goal test
            if state == self.goal:
                return path

            if state in visited:
                continue
            visited.add(state)

            # Expand successors
            for label, action in problem["actions"]:
                new_state = action(state)
                new_path = path + [label]   # store the label instead of the function
                queue.append((new_state, new_path))

        return None

    def execute(self):
        problem = self.formulate_problem()
        solution = self.search(problem)
        return solution


# Example run
agent = simpleProblemSolvingAgent(0, 5)
solution = agent.execute()
print("Solution found with actions:", solution)
