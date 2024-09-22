from collections import deque

def grid(r, c):
    """
    Initializes a 2D grid of size r x c with all cells set to 0.

    Parameters:
    r (int): Number of rows.
    c (int): Number of columns.

    Returns:
    list: A 2D list representing the grid.
    """
    return [[0 for _ in range(c)] for _ in range(r)]

def disp_grid(grid):
    """
    Prints the current state of the grid.

    Parameters:
    grid (list): The 2D grid to display.
    """
    for row in grid:
        print(row)

def bfs(grid, start, goal):
    """
    Performs a Breadth-First Search (BFS) to find the shortest path from start to goal.

    Parameters:
    grid (list): The 2D grid where the search is performed.
    start (list): The starting position [row, col].
    goal (list): The goal position [row, col].

    Returns:
    list or None: The shortest path from start to goal as a list of positions, 
                  or None if no path is found.
    """
    r, c = len(grid), len(grid[0])
    queue = deque([start])          # Queue to manage the BFS frontier
    visited = set([tuple(start)])   # Set to track visited positions
    parent = {tuple(start): None}   # Dictionary to reconstruct the path

    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()  # Dequeue the next position to explore
        if current == goal:        # Check if the goal has been reached
            return reconstruct_path(parent, start, goal)
        
        # Get valid neighbors for the current position
        neighbors = get_neighbors(current, r, c, directions)
        for neighbor in neighbors:
            # Avoid obstacles and already visited positions
            if tuple(neighbor) not in visited and grid[neighbor[0]][neighbor[1]] != 'X':
                visited.add(tuple(neighbor))
                queue.append(neighbor)
                parent[tuple(neighbor)] = current

    return None  # Return None if no path is found

def get_neighbors(pos, r, c, directions):
    """
    Generates valid neighboring positions around a given position.

    Parameters:
    pos (list): The current position [row, col].
    r (int): Number of rows in the grid.
    c (int): Number of columns in the grid.
    directions (list): List of direction vectors to explore.

    Returns:
    list: A list of valid neighboring positions.
    """
    neighbors = []
    for direction in directions:
        new_pos = [pos[0] + direction[0], pos[1] + direction[1]]
        # Check if the new position is within grid boundaries
        if 0 <= new_pos[0] < r and 0 <= new_pos[1] < c:
            neighbors.append(new_pos)
    return neighbors

def reconstruct_path(parent, start, goal):
    """
    Reconstructs the path from start to goal using the parent dictionary.

    Parameters:
    parent (dict): Dictionary mapping each position to its predecessor.
    start (list): The starting position [row, col].
    goal (list): The goal position [row, col].

    Returns:
    list: The reconstructed path from start to goal.
    """
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[tuple(current)]
    path.reverse()  # Reverse the path to get it from start to goal
    return path

def display_grid_with_path(grid, path, start, goal):
    """
    Updates and displays the grid with the path marked.

    Parameters:
    grid (list): The 2D grid where the path is marked.
    path (list): The list of positions representing the path.
    start (list): The starting position [row, col].
    goal (list): The goal position [row, col].
    """
    # Mark the path on the grid
    for pos in path:
        if pos != start and pos != goal:
            grid[pos[0]][pos[1]] = 'P'  # Mark path positions with 'P'
    grid[start[0]][start[1]] = 'S'     # Mark start position with 'S'
    grid[goal[0]][goal[1]] = 'G'       # Mark goal position with 'G'
    disp_grid(grid)

def add_obstacles(grid):
    """
    Allows the user to add obstacles to the grid.

    Parameters:
    grid (list): The 2D grid where obstacles will be added.
    """
    # Get the number of obstacles from the user
    while True:
        obs_count = input("Enter number of obstacles: ")
        if obs_count.isdigit() and int(obs_count) > 0:
            obs_count = int(obs_count)
            break
        else:
            print("Please enter a valid number of obstacles.")

    # Allow user to input each obstacle's position
    for _ in range(obs_count):
        while True:
            obs = input("Enter obstacle position as 'row col': ")
            obs_pos = [int(x) for x in obs.split()]
            # Check if the position is within bounds and not already occupied
            if (0 <= obs_pos[0] < len(grid) and 
                0 <= obs_pos[1] < len(grid[0]) and 
                grid[obs_pos[0]][obs_pos[1]] == 0):
                grid[obs_pos[0]][obs_pos[1]] = 'X'  # Mark obstacle with 'X'
                break
            else:
                print("Invalid position or position already occupied. Try again.")

if __name__ == "__main__":
    # Initialize grid size
    print("Enter Grid Size")
    r = int(input("Row size?: "))
    c = int(input("Column size?: "))
    
    # Get valid start and goal positions from the user
    while True:
        start = [int(x) for x in input("Enter START at: ").split()]
        goal = [int(x) for x in input("Enter END at: ").split()]
        if 0 <= start[1] < c and 0 <= start[0] < r and 0 <= goal[1] < c and 0 <= goal[0] < r:
            break
        else:
            print("Either start or end are beyond boundaries")
            continue
    
    # Create the grid and add obstacles
    gridf = grid(r, c)
    add_obstacles(gridf)

    # Mark the start and goal positions
    gridf[start[0]][start[1]] = 'S'
    gridf[goal[0]][goal[1]] = 'G'
    disp_grid(gridf)  # Display the grid with obstacles, start, and goal

    # Perform BFS to find the optimal path
    path = bfs(gridf, start, goal)

    # Display the results
    if path:
        print("\nOptimal path found!")
        display_grid_with_path(gridf, path, start, goal)
        print(f"Path length: {len(path) - 1}")  # Length of the path excluding the start node
        print(f"Cells explored: {len(path)}")  # Number of steps taken to reach the goal
    else:
        print("\nNo path found!")
