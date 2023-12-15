import solara
from mesa_interactive import MesaInteractive
from mesa_interactive.components.grid import create_grid
from mesa_interactive.util import slide
from habitat_model import HabitatModel

grid = create_grid("type")
app = MesaInteractive(
    HabitatModel,
    {"n_prey": 25, "n_predators": 5, "food_probability": slide(0, 1, 0.05, default=0.25)},
    components=[
        grid,
    ],
    show_dataframe="model",
)

# Run in terminal with solara run src/habitat/habitat_viz.py