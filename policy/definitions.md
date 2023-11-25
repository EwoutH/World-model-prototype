## Definitions
A few definitions currently used in this repository:

- **Entity**: An Agent or Model instance or object. In ABM, entities represent individual actors or components in the simulation.
- **State**: A variable from an Agent or Model that can change during a simulation. States store information about the entity's characteristics or attributes.
- **Behavior**: A behavior is an action or operation that uses and/or influences an entity's state in some way. Behaviors are typically implemented as classes and can modify the state of the entity they are associated with.
- **Function**: In contrast to a behavior, a function operates in a stateless manner. It does not rely on the state of an entity to perform its task. Functions can take input arguments and return output variables, similar to regular Python functions.
