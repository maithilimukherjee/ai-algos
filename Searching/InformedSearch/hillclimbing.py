import random

def hill_climbing(problem, max_iterations=1000):
    """
    Hill Climbing Algorithm.
    problem must define:
      - initial_state()
      - neighbors(state)
      - value(state)  (objective function to maximize)
    """
    current = problem.initial_state()
    for _ in range(max_iterations):
        neighbors = problem.neighbors(current)
        if not neighbors:
            break

        # Choose the neighbor with the highest value
        next_state = max(neighbors, key=lambda s: problem.value(s))

        if problem.value(next_state) <= problem.value(current):
            # No improvement → stop
            break

        current = next_state

    return current

class QuadraticProblem:
    def __init__(self):
        self.range = list(range(-10, 11))  # possible states

    def initial_state(self):
        return random.choice(self.range)

    def neighbors(self, state):
        # neighbors are +/- 1 step
        return [s for s in [state-1, state+1] if s in self.range]

    def value(self, state):
        return -(state**2) + 10  # objective function

problem = QuadraticProblem()
solution = hill_climbing(problem)
print("Best solution found:", solution, "with value:", problem.value(solution))
