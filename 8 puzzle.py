#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_pos = np.argwhere(goal_state == value)[0]
                distance = abs(i - goal_pos[0]) + abs(j - goal_pos[1])
                total_distance += distance
    return total_distance

# Generate all possible moves for a given state
def generate_moves(state):
    moves = []
    empty_pos = np.argwhere(state == 0)[0]
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_pos = empty_pos + move
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_state = state.copy()
            new_state[empty_pos[0], empty_pos[1]] = state[new_pos[0], new_pos[1]]
            new_state[new_pos[0], new_pos[1]] = 0
            moves.append(new_state)
    return moves

# Steepest ascent hill-climbing algorithm
def steepest_ascent(initial_state, goal_state):
    current_state = initial_state.copy()
    level = 1
    while True:
        print("\nLevel:", level)
        print("Current State:\n", current_state)
        current_distance = manhattan_distance(current_state, goal_state)
        print("Heuristic Value:", current_distance)
        
        best_next_state = None
        best_next_distance = float("inf")
        for move in generate_moves(current_state):
            move_distance = manhattan_distance(move, goal_state)
            if move_distance < best_next_distance:
                best_next_state = move
                best_next_distance = move_distance
        
        if best_next_distance >= current_distance:
            print("\nReached local maximum. Final state:\n", current_state)
            break
        
        current_state = best_next_state
        level += 1


initial_state = np.array([[5,0,8],
                          [4,2,1],
                          [7,3,6]])

goal_state = np.array([[1,2,3],
                       [4,5,6],
                       [7, 8,0]])

# Solve the puzzle using steepest ascent
steepest_ascent(initial_state, goal_state)





# In[ ]:




