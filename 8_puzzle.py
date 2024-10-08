def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i = (state[i][j] - 1) // 3
                goal_j = (state[i][j] - 1) % 3
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    neighbors.append(swap(state, i, j, i - 1, j))
                if i < 2:
                    neighbors.append(swap(state, i, j, i + 1, j))
                if j > 0:
                    neighbors.append(swap(state, i, j, i, j - 1))
                if j < 2:
                    neighbors.append(swap(state, i, j, i, j + 1))
    return neighbors

def swap(state, i1, j1, i2, j2):
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def dfs_with_manhattan(initial_state, goal_state, visited=None):
    if visited is None:
        visited = set()

    if initial_state == goal_state:
        return [initial_state]

    visited.add(str(initial_state))
    neighbors = sorted(get_neighbors(initial_state), key=lambda x: manhattan_distance(x, goal_state))

    for neighbor in neighbors:
        if str(neighbor) not in visited:
            path = dfs_with_manhattan(neighbor, goal_state, visited)
            if path:
                return [initial_state] + path

    return None

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Take user input for initial state
initial_state = []
for i in range(3):
    row = input(f"Enter row {i + 1} (space-separated values): ").split()
    initial_state.append([int(x) for x in row])

solution = dfs_with_manhattan(initial_state, GOAL_STATE)
if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
