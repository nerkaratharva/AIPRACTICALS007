from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            return (jug1, jug2)

        # Fill Jug 1
        if jug1 < jug1_capacity:
            fill_jug1 = (jug1_capacity, jug2)
            if fill_jug1 not in visited:
                visited.add(fill_jug1)
                queue.append(fill_jug1)

        # Fill Jug 2
        if jug2 < jug2_capacity:
            fill_jug2 = (jug1, jug2_capacity)
            if fill_jug2 not in visited:
                visited.add(fill_jug2)
                queue.append(fill_jug2)

        # Empty Jug 1
        if jug1 > 0:
            empty_jug1 = (0, jug2)
            if empty_jug1 not in visited:
                visited.add(empty_jug1)
                queue.append(empty_jug1)

        # Empty Jug 2
        if jug2 > 0:
            empty_jug2 = (jug1, 0)
            if empty_jug2 not in visited:
                visited.add(empty_jug2)
                queue.append(empty_jug2)

        # Pour from Jug 1 to Jug 2
        if jug1 > 0 and jug2 < jug2_capacity:
            pour_jug1_to_jug2 = (max(jug1 - (jug2_capacity - jug2), 0), min(jug2 + jug1, jug2_capacity))
            if pour_jug1_to_jug2 not in visited:
                visited.add(pour_jug1_to_jug2)
                queue.append(pour_jug1_to_jug2)

        # Pour from Jug 2 to Jug 1
        if jug2 > 0 and jug1 < jug1_capacity:
            pour_jug2_to_jug1 = (min(jug1 + jug2, jug1_capacity), max(jug2 - (jug1_capacity - jug1), 0))
            if pour_jug2_to_jug1 not in visited:
                visited.add(pour_jug2_to_jug1)
                queue.append(pour_jug2_to_jug1)

    return None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

result = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
if result:
    print("Solution found:")
    print(f"Jug 1: {result[0]}, Jug 2: {result[1]}")
else:
    print("No solution found.")


