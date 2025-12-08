#vacuum toy problem in ai
class VacuumEnvironment:
    def __init__(self, left_dirty=True, right_dirty=True, agent_location="left"):
        self.state = {
            "left": left_dirty,
            "right": right_dirty
        }
        self.agent_location = agent_location

    def percept(self):
        # agent sees (location, whether that square is dirty)
        return self.agent_location, self.state[self.agent_location]

    def execute_action(self, action):
        if action == "suck":
            self.state[self.agent_location] = False
        elif action == "left":
            self.agent_location = "left"
        elif action == "right":
            self.agent_location = "right"


class SimpleVacuumAgent:
    def act(self, percept):
        location, is_dirty = percept

        if is_dirty:
            return "suck"      # clean the current square
        elif location == "left":
            return "right"     # move to the other square
        else:
            return "left"


# run the simulation
env = VacuumEnvironment(left_dirty=True, right_dirty=True, agent_location="right")
agent = SimpleVacuumAgent()

for step in range(5):
    percept = env.percept()
    action = agent.act(percept)
    env.execute_action(action)
    print(f"step {step}: percept={percept}, action={action}, state={env.state}")
