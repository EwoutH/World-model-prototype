import numpy as np
import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid, PropertyLayer
from mesa.datacollection import DataCollector

class HabitatModel(Model):
    def __init__(self, n_prey, n_predators, food_probability):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.running = True
        self.food_layer = PropertyLayer("food", 32, 32, default_value=False, dtype=bool)
        self.grid = MultiGrid(32, 32, True, property_layers=self.food_layer)

        self.food_probability = food_probability
        self._init_food()

        # Create prey agents
        for _ in range(n_prey):
            a = Prey(self.next_id(), self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Create predator agents
        for _ in range(n_predators):
            a = Predator(self.next_id(), self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Prey": lambda m: self.count_type(m, Prey),
                             "Predator": lambda m: self.count_type(m, Predator)},
            agent_reporters={"Health": lambda a: a.health,
                                "Energy": lambda a: a.energy,
                                "Age": lambda a: a.age,
                                "Lust": lambda a: a.lust})

    def _init_food(self):
        # Initialize grid with food using PropertyLayer functionality
        condition = lambda val: np.random.random_sample(val.shape) < self.food_probability
        self.food_layer.set_cells(True, condition)

    def remove_food(self, pos):
        # Efficiently remove food from a cell
        self.food_layer.set_cell(pos, False)

    def spread_food(self, pos, n):
        # Spread food to neighboring cells
        neighbors = self.grid.get_neighborhood(pos, moore=True, include_center=False)
        for neighbor in random.sample(neighbors, min(n, len(neighbors))):
            if not self.has_food(neighbor):
                self.food_layer.set_cell(neighbor, True)

    def has_food(self, pos):
        # Check if a cell has food
        return self.food_layer.data[pos]

    def step(self):
        self.schedule.step()
        # Spread food from existing food patches
        for pos in self.food_layer.select_cells(lambda val: val):
            self.spread_food(pos, n=2)


class Animal(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.type = str(self.__class__.__name__)
        self.sleep = random.uniform(0.25, 0.75)
        self.energy = random.uniform(0.25, 0.75)
        self.health = random.uniform(0.5, 1.0)
        self.age = random.randint(0, 10)
        self.lust = random.uniform(0.25, 0.75) if self.age > 2 else 0.0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def reproduce(self):
        pass

    def eat(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def step(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

class Prey(Animal):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def eat(self):
        # Example: Prey eats if on a cell with food
        if self.model.has_food(self.pos):
            self.energy += 0.1  # Increment energy
            self.model.remove_food(self.pos)  # Remove food from grid

    def step(self):
        self.move()
        self.eat()
        self.reproduce()


class Predator(Animal):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def hunt(self):
        # Find nearby prey
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=True)
        for neighbor in neighbors:
            if isinstance(neighbor, Prey):
                # Attempt to catch the prey
                if self.random.random() < 0.5:  # Example success rate
                    self.model.grid.remove_agent(neighbor)  # Remove prey from grid
                    self.eat()  # Eat the prey
                    break

    def eat(self):
        # Specific implementation for predator eating (e.g., after a successful hunt)
        self.energy += 0.2  # Example increment


    def step(self):
        self.move()
        if self.energy < 0.5:
            self.hunt()
        else:
            self.eat()
        self.reproduce()

# model1 = HabitatModel(25, 5, 0.25)
# model1.step()
# print(agents := model1.grid.coord_iter())
# for agent in agents:
#     print(agent)