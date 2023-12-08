#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq

graph = {
    's': {'b': 4, 'c': 3},
    'b': {'s': 4, 'f': 5, 'e': 12},
    'f': {'b': 5, 'g': 16},
    'c': {'s': 3, 'e': 10, 'd': 7},
    'd': {'c': 7, 'e': 2},
    'e': {'b': 12, 'c': 10, 'd': 2, 'g': 5},
    'g': {'f': 16, 'e': 5}
}

heuristics = {
    's': 14,
    'b': 12,
    'f': 11,
    'c': 11,
    'd': 6,
    'e': 4,
    'g': 0
}

def astar(start, goal):
    open_list, closed_list, parent = [(heuristics[start], 0, start)], set(), {}

    while open_list:
        _, cost, current = heapq.heappop(open_list)
        if current == goal:
            path = [current]
            while current in parent:
                path.append(current := parent[current])
            return path[::-1]

        closed_list.add(current)

        for neighbor, edge_cost in graph[current].items():
            if neighbor not in closed_list:
                new_cost = cost + edge_cost
                heapq.heappush(open_list, (new_cost + heuristics[neighbor], new_cost, neighbor))
                parent[neighbor] = current

    return None

start_node = 's'
goal_node = 'g'

path = astar(start_node, goal_node)

if path:
    print("Optimal Path:", " -> ".join(path))
else:
    print("No path found.")



# In[ ]:




