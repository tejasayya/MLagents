class SimpleReflexAgent:
    def perceive(self, state):
        # Convert the input state into a dictionary with meaningful attributes
        if state == 'd': #dirty room
            return {'cleanliness': 'dirty', 'obstacle': False, 'occupied': False}
        elif state == 'o': #obstacle
            return {'cleanliness': 'clean', 'obstacle': True, 'occupied': False}
        elif state == 'p': #occupied room
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': True}
        elif state == 'c': #clean room
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': False}

    def decide_action(self, state):
        # Check the current state's attributes to determine the next action
        if state['cleanliness'] == 'dirty': # if the room is dirty, clean it
            return 'clean'
        elif state['obstacle']: # if there's an obstacle, avoid it
            return 'avoid_obstacle'
        elif state['occupied']: # if the room is occupied, wait
            return 'wait'
        else: # if none of the above conditions are met, move to the next room
            return 'move_to_next_room'

    def perform_action(self, action):
        print(f"Performing action: {action}")

def main():
    agent = SimpleReflexAgent()
    while True:
        state = input("Enter the state of the room (d/o/p/c): ")
        perceived_state = agent.perceive(state)
        action = agent.decide_action(perceived_state)
        agent.perform_action(action)

if __name__ == "__main__":
    main()