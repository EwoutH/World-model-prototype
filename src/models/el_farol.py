from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
import random

class BarAgent(Agent):
    def __init__(self, unique_id, model, memory_size, number_strategies):
        super().__init__(unique_id, model)
        self.memory_size = memory_size
        self.number_strategies = number_strategies
        self.strategies = [self.random_strategy() for _ in range(number_strategies)]
        self.best_strategy = self.strategies[0]
        self.attend = False
        self.prediction = 0

    def random_strategy(self):
        return [random.uniform(-1.0, 1.0) for _ in range(self.memory_size + 1)]

    def predict_attendance(self, strategy, subhistory):
        weighted_sum = sum(weight * week for weight, week in zip(strategy[1:], subhistory))
        return 100 * strategy[0] + weighted_sum

    def decide_attendance(self):
        subhistory = self.model.history[:self.memory_size]
        self.prediction = self.predict_attendance(self.best_strategy, subhistory)
        self.attend = self.prediction <= self.model.overcrowding_threshold

    def update_strategy(self):
        best_score = float('inf')
        for strategy in self.strategies:
            score = 0
            for week in range(1, self.memory_size + 1):
                subhistory = self.model.history[week:week + self.memory_size]
                prediction = self.predict_attendance(strategy, subhistory)
                actual_attendance = self.model.history[week - 1]
                score += abs(actual_attendance - prediction)

            if score <= best_score:
                best_score = score
                self.best_strategy = strategy

    def move_to_location(self, location):
        """Move the agent to a specified location."""
        self.model.grid.move_agent(self, location)

    def find_empty_location(self, area_x_min, area_y_min, area_x_max, area_y_max):
        """Find an empty location within a specified area."""
        potential_locations = [(x, y) for x in range(area_x_min, area_x_max)
                               for y in range(area_y_min, area_y_max)
                               if self.model.grid.is_cell_empty((x, y))]
        return random.choice(potential_locations) if potential_locations else None

    def step(self):
        self.decide_attendance()

        if self.attend:
            # Find an empty location in the bar area
            location = self.find_empty_location(self.model.bar_area_x_min,
                                                self.model.bar_area_y_min,
                                                self.model.bar_area_x_max,
                                                self.model.bar_area_y_max)
            if location:
                self.model.grid.move_agent(self, location)
        else:
            # Move to home area
            # Assuming home area is the rest of the grid, adjust the ranges accordingly
            location = self.find_empty_location(0, 0, self.model.bar_area_x_min, self.model.grid.height)
            if location:
                self.model.grid.move_agent(self, location)

        self.update_strategy()


class ElFarolBarModel(Model):
    def __init__(self, N=100, width=35, height=35, memory_size=5, number_strategies=10, overcrowding_threshold=60):
        super().__init__()
        self.num_agents = N
        self.grid = SingleGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.memory_size = memory_size
        self.overcrowding_threshold = overcrowding_threshold
        self.history = [random.randint(0, 100) for _ in range(memory_size * 2)]
        self.attendance = 0

        # Define bar area as top right quadrant
        self.bar_area_x_min = width // 2
        self.bar_area_y_min = height // 2
        self.bar_area_x_max = width
        self.bar_area_y_max = height

        # Create agents and place them in empty cells
        for i in range(self.num_agents):
            agent = BarAgent(i, self, memory_size, number_strategies)
            self.schedule.add(agent)
            self.grid.move_to_empty(agent)

    def step(self):
        self.attendance = 0  # Reset attendance
        self.schedule.step()  # Activate agents

        # Update attendance
        for agent in self.schedule.agents:
            if agent.attend:
                self.attendance += 1

        # Check for overcrowding
        crowded = self.attendance > self.overcrowding_threshold
        # Update history
        self.history.append(self.attendance)
        self.history.pop(0)

        self.running = True  # You can add a condition to stop the model

# Create and run the model
model = ElFarolBarModel()
for i in range(100):
    model.step()
