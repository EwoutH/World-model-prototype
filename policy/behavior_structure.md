## Policy Document: Behavior Structure
The goal of this policy document is to provide a clear and structured framework for creating behaviors and functions in the context of Agent-Based Modeling (ABM). The aim is to build a library of data, behaviors, and environment components that seamlessly integrate with each other. This library will empower users to easily import specific behaviors into their own Agent and Model objects using Mixin. This document outlines the guidelines for designing and structuring behaviors and functions.

### Behavior and Function Overview
In the context of ABM, we distinguish between behaviors and functions based on their operational characteristics.

- **Function**: A function operates in a stateless manner, meaning it doesn't rely on the agent or model's state to function. It can take input arguments and return output variables, just like regular Python functions.
- **Behavior**: A behavior operates within the context of an agent's, another agent's, and/or the model's state. It may take this state as input and/or modify it. Behaviors are implemented as classes with a single method bearing the same name as the class/behavior. Generally, behaviors do not require an `__init__` method. Users can incorporate behaviors into existing Agent or Model classes using Mixin.

### Library structure
Behaviors are in Behaviors and functions are organized into three layers of depth:

1. **Main Categories**: The highest level of categorization, providing a broad classification for behaviors and functions.
2. **Subcategories**: Further divisions within main categories, providing more specific groupings based on functionality.
3. **Behavior/Function Modules**: Individual Python files that contain a single behavior or function.

### Structure of a Behavior/Function Module
Each behavior or function module should adhere to the following structure:

1. **Docstring**:
   - One-line description: A concise one-line summary of the behavior or function.
   - Extensive description: A more detailed explanation of its purpose, context and functionality.
   - Scientific sources: References to relevant academic sources, if applicable. May also be included in the extensive description.
   - Arguments and return (for functions) or the states used and modified for each entity (for behaviors).

2. **Imports** (only if necessary): Include necessary Python module imports for the behavior or function.

3. **Boolean Switches**:
   - `is_function`: A boolean switch set to `True` if it's a function, `False` if it's a behavior.
   - `for_agent`: A boolean switch set to `True` if it's meant for the agent step, `False` if it's for the model step.

4. **Function or Class**: Define a single function (for functions) or a single class (for behaviors) with a single method. Deviating from this structure is allowed but should be well-justified and compatible with Mixin.

5. **Tests**: Provide comprehensive tests that can be executed with pytest. These tests should be well-documented and serve as examples. They ensure the correctness and usability of the behavior or function.

### Main Category and Subcategory Readme
Each main category and subcategory should have its own readme file that provides an overview of the contained behaviors and functions, making it easier for users to navigate the library.
