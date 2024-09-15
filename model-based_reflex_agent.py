class ModelBasedReflexAgent:
    def __init__(self):
        #Initializing the Internal model with an empty history
        self.internal_model = {'history': []}

    def perceive(self, state):
        if state == 'd': #dirty room
            return {'cleanliness': 'dirty', 'obstacle': False, 'occupied': False}
        elif state == 'o': # Obstacle
            return {'cleanliness': 'clean', 'obstacle': True, 'occupied': False}
        elif state == 'p': # occupied room
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': True}
        elif state == 'c': # clean room
            return {'cleanliness': 'clean', 'obstacle': False, 'occupied': False}

    def decide_action(self, state):
        # adding the current state to the internal model's history
        self.internal_model['history'].append(state)
        if state['cleanliness'] == 'dirty': # If Room is Dirty : Clean
            return 'clean'
        elif state['obstacle']: # if there's an obstacle, avoid it
            return 'avoid_obstacle'
        elif state['occupied']: # if the room is occupied, wait
            return 'wait'
        else:
            # If none of the above conditions are met, check the internal model's history
            previous_states = self.internal_model['history']
            # If the room was previously dirty, move to the next room
            if any(state['cleanliness'] == 'dirty' for state in previous_states):
                return 'move_to_next_room'
            # Otherwise, explore the room
            return 'explore'

    def perform_action(self, action):
        print(f"Performing action: {action}")
        # Update the internal model based on the chosen action
        if action == 'clean': # if cleaning, update the cleanliness attribute
            self.internal_model['history'][-1]['cleanliness'] = 'clean'
        elif action == 'avoid_obstacle': # if avoiding obstacle, update the obstacle attribute
            self.internal_model['history'][-1]['obstacle'] = False
        elif action == 'wait': # if waiting, update the occupied attribute
            self.internal_model['history'][-1]['occupied'] = False

def main():
    #Create an instance of the Model-Based Reflex Agent
    agent = ModelBasedReflexAgent()
    while True:
        # Get the current state of the room from the user
        state = input("Enter the state of the room (d/o/p/c): ")
        # Perceive the current state
        perceived_state = agent.perceive(state)
        # Decide the next action
        action = agent.decide_action(perceived_state)
        # Perform the chosen action
        agent.perform_action(action)
        # Print the updated internal model
        print(agent.internal_model)

if __name__ == "__main__":
    main()