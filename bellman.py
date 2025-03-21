import numpy as np

# Define GridWorld parameters
N = 4  # Grid size (4x4)
num_states = N * N
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
reward = -1  # Reward per move
gamma = 1  # No discounting
theta = 1e-4  # Convergence threshold

# Initialize value function
V = np.zeros((N, N))

# Function to get next state given an action
def get_next_state(i, j, action):
    di, dj = action
    new_i, new_j = i + di, j + dj
    if 0 <= new_i < N and 0 <= new_j < N:
        return new_i, new_j  # Valid move
    return i, j  # If out of bounds, stay in place

# Value Iteration Algorithm
while True:
    delta = 0  # Track maximum change
    V_new = np.copy(V)  # Create a copy of the value function
    
    for i in range(N):
        for j in range(N):
            if (i, j) == (N-1, N-1):
                continue  # Skip terminal state
            
            value_sum = 0
            for action in actions:
                next_i, next_j = get_next_state(i, j, action)
                value_sum += (1 / len(actions)) * (reward + gamma * V[next_i, next_j])
            
            V_new[i, j] = value_sum
            delta = max(delta, abs(V_new[i, j] - V[i, j]))
    
    V = V_new  # Update value function
    if delta < theta:
        break  # Convergence condition met

# Print final value function
print(np.round(V, decimals=6))
