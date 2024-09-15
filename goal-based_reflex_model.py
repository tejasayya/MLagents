class GoalBasedReflexAgent:
    def __init__(self):
        self.goals = ['cleanliness', 'obstacle_avoidance', 'minimize_waiting']
        self.internal_model = {'history': []}

    def perceive(self, state):
        if state == 'd':
            return {'cleanliness': 'dirty', 'obstacle': False, 'occupied': False}
        elif state == 'o':
            return {'cleanliness': 'clean', 'obstacle': True, 'occupied': False}
        elif state == 'p':
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': True}
        elif state == 'c':
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': False}

    def decide_action(self, state):
        self.internal_model['history'].append(state)
        #setting priorities for the agent's goals
        goal_priorities = {'cleanliness': 0.5, 'obstacle_avoidance': 0.3, 'minimize_waiting': 0.2}
        if state['cleanliness'] == 'dirty' and goal_priorities['cleanliness'] >= 0.5:
            return 'clean'
        elif state['obstacle'] and goal_priorities['obstacle_avoidance'] >= 0.3:
            return 'avoid_obstacle'
        elif state['occupied'] and goal_priorities['minimize_waiting'] >= 0.2:
            return 'wait'
        else:
            return 'move_to_next_room'

    def perform_action(self, action):
        print(f"Performing action: {action}")
        if action == 'clean':
            self.internal_model['history'][-1]['cleanliness'] = 'clean'
            self.goals[0] = 'achieved'
        elif action == 'avoid_obstacle':
            self.internal_model['history'][-1]['obstacle'] = False
            self.goals[1] = 'achieved'
        elif action == 'wait':
            self.internal_model['history'][-1]['occupied'] = False
            self.goals[2] = 'achieved'

def main():
    agent = GoalBasedReflexAgent()
    while True:
        state = input("Enter the state of the room (d/o/p/c): ")
        perceived_state = agent.perceive(state)
        action = agent.decide_action(perceived_state)
        agent.perform_action(action)
        print(agent.internal_model)
        print(agent.goals)

if __name__ == "__main__":
    main()