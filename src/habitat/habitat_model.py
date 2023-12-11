from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class HabitatModel(Model):
    def __init__(self, n_prey, n_predators):
        self.schedule = None
        self.running = True
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid

        # Create prey agents
        for i in range(n_prey):
            a = Prey(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Create predator agents
        for i in range(n_predators):
            a = Predator(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()


class Animal(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


class Prey(Animal):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass


class Predator(Animal):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        pass
