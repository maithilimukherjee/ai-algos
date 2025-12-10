import math, random

def simulated_annealing(problem, schedule):
    current = problem.initial_state()

    for t in range(1, 10000):
        T = schedule(t)
        if T == 0:
            return current

        neighbors = problem.neighbors(current)
        if not neighbors:
            return current

        next_state = random.choice(neighbors)
        deltaE = problem.value(next_state) - problem.value(current)

        if deltaE > 0:
            current = next_state
        else:
            if random.random() < math.exp(deltaE / T):
                current = next_state

    return current


class QuadraticProblem:
    def __init__(self):
        self.range = list(range(-50, 51))  # wider search range

    def initial_state(self):
        return random.choice(self.range)

    def neighbors(self, state):
        return [s for s in [state - 1, state + 1] if s in self.range]

    def value(self, state):
        # minimize f(x) = x^2 + 10x - 24
        # so maximize -f(x)
        return -(state**2 + 10*state - 24)


def schedule(t):
    return max(0.001, 100 / t)


problem = QuadraticProblem()
solution = simulated_annealing(problem, schedule)

print("best x:", solution)
print("f(x) =", solution**2 + 10*solution - 24)
