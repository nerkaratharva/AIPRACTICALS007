import random

# Define your objective function. This function should return a score that the algorithm tries to maximize.
def objective_function(solution):
    # For demonstration purposes, let's use a simple example: maximizing the sum of a list of numbers.
    return sum(solution)

# Define the hill climbing algorithm
def hill_climbing(max_iterations, problem_size):
    # Generate an initial random solution
    current_solution = [random.randint(0, 100) for _ in range(problem_size)]
    current_score = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generate a neighbor solution by slightly perturbing the current solution
        neighbor_solution = current_solution[:]
        index_to_change = random.randint(0, problem_size - 1)
        neighbor_solution[index_to_change] += random.randint(-10, 10)
        
        # Calculate the score of the neighbor solution
        neighbor_score = objective_function(neighbor_solution)

        # If the neighbor solution is better, move to it
        if neighbor_score > current_score:
            current_solution = neighbor_solution
            current_score = neighbor_score

    return current_solution, current_score

if __name__ == "__main__":
    max_iterations = 1000
    problem_size = 10

    best_solution, best_score = hill_climbing(max_iterations, problem_size)

    print("Best Solution:", best_solution)
    print("Best Score:", best_score)


