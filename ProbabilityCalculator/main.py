import copy
import random

class Hat:
    def __init__(self, **kwargs):  # Convert keyword args to list
        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):  # Add each ball to separate string in the list
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):  # Fixed: was self.content, should be self.contents
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls

        drawn_balls = [] # Draw random balls without replacement
        for _ in range(num_balls):
            random_index = random.randint(0, len(self.contents) - 1)
            drawn_ball = self.contents.pop(random_index)
            drawn_balls.append(drawn_ball)

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1

        success = True
        for color, expected_count in expected_balls.items():
            if drawn_count.get(color, 0) < expected_count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments

if __name__ == "__main__":
    hat1 = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat1,
                        expected_balls={'red': 2, 'green': 1},
                        num_balls_drawn=5,
                        num_experiments=2000)
    print(f"Probability: {probability}")

    hat1 = Hat(yellow=3, blue=2, green=6)
    print(f"Hat1 contents: {hat1.contents}")

    hat2 = Hat(red=5, orange=4)
    print(f"Hat2 contents: {hat2.contents}")

    drawn = hat1.draw(3)
    print(f"Drawn balls: {drawn}")
    print(f"Remaining in hat1: {hat1.contents}")
