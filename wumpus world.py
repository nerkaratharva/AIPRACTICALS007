import random
class WumpusWorld:
    def __init__(self, size=4, num_pits=3):
        self.size = size
        self.agent_location = (0, 0)
        self.wumpus_location = self.generate_random_location()
        self.pit_locations = [self.generate_random_location() for _ in range(num_pits)]
        self.gold_location = self.generate_random_location()
        self.has_gold = False
        self.has_arrow = True
        self.is_alive = True
    def generate_random_location(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        return (x, y)
    def move(self, direction):
        if direction == "left" and self.agent_location[0] > 0:
            self.agent_location = (self.agent_location[0] - 1, self.agent_location[1])
        elif direction == "right" and self.agent_location[0] < self.size - 1:
            self.agent_location = (self.agent_location[0] + 1, self.agent_location[1])
        elif direction == "up" and self.agent_location[1] < self.size - 1:
            self.agent_location = (self.agent_location[0], self.agent_location[1] + 1)
        elif direction == "down" and self.agent_location[1] > 0:
            self.agent_location = (self.agent_location[0], self.agent_location[1] - 1)
        self.check_environment()
    def check_environment(self):
        if self.agent_location == self.wumpus_location:
            self.is_alive = False
            print("You were eaten by the wumpus!")
        elif self.agent_location in self.pit_locations:
            self.is_alive = False
            print("You fell into a pit!")
        elif self.agent_location == self.gold_location:
            self.has_gold = True
            print("You found the gold!")
    def shoot(self):
        if self.has_arrow:
            self.has_arrow = False
            if self.agent_location == self.wumpus_location:
                print("You shot and killed the wumpus!")
            else:
                print("You missed the wumpus!")
    def display(self):
        for y in range(self.size - 1, -1, -1):
            for x in range(self.size):
                if (x, y) == self.agent_location:
                    print("A", end="\t")
                elif (x, y) == self.gold_location:
                    print("G", end="\t")
                elif (x, y) == self.wumpus_location:
                    print("W", end="\t")
                elif (x, y) in self.pit_locations:
                    print("P", end="\t")
                else:
                    print("-", end="\t")
            print()
# Example usage:
if __name__ == "__main__":
    game = WumpusWorld()
    while game.is_alive and not game.has_gold:
        game.display()
        action = input("Enter your action (left, right, up, down, shoot): ")
        if action in ["left", "right", "up", "down"]:
            game.move(action)
        elif action == "shoot":
            game.shoot()
    if game.has_gold:
        print("You won the game!")
    else:
        print("Game over!")



