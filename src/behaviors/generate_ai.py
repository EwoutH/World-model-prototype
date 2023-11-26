import openai
import time
from economic_behaviors import behaviors  # This is a list of dictionaries with behavior information


# Function to generate Python code for a specific behavior
def generate_behavior_code(behavior_name, theory, description, behavior_type, requires_state, entity):
    # Convert behavior name to appropriate class and method/function names
    behavior_without_dash = behavior_name.replace("-", " ")
    class_name = ''.join(word.title() for word in behavior_without_dash.split())
    method_name = '_'.join(word.lower() for word in behavior_without_dash.split())

    # Determine the code structure based on behavior type
    if behavior_type:  # If it's a behavior
        code_structure = (f"Define a single class named {class_name} with a single method named {method_name}. "
                          f"The behavior should be able to be added to a {entity} with Mixin.")
        modified = "Agent/Model states used and/or modified."
    else:  # If it's a function
        code_structure = f"Define a single Python function named {method_name}."
        modified = "Input arguments and return values"

    prompt = f"""
Write a Python module for a {behavior_name} behavior that can be used in an Agent-Based Model (ABM).

- Behavior Name: {behavior_name}
- Theoretical Basis: {theory}
- Short description: {description}
- Behavior be added to a: (Mesa) {entity}
- Requires State from Other Agents or Model: {requires_state}

The output should be Python code with the following structure:
1. Docstring:
   - One-line description: Concise summary of the behavior.
   - Extensive description: Detailed explanation of its purpose and functionality.
   - Scientific sources: References to {theory} (if known, don't make up).
   - {modified}

2. Imports: Necessary Python module imports.

3. Boolean Switches:
   - `is_function`: {'True' if not behavior_type else 'False'}
   - `for_agent`: {'True' if entity == 'Agent' else 'False'}

4. {code_structure}

5. Tests: pytest-compatible tests for the behavior.

Python Code:
"""

    # response = openai.Completion.create(
    #     model="gpt-3.5-turbo",
    #     prompt=prompt,
    #     max_tokens=2000
    # )
    # return response
    return prompt

# OpenAI API Key Setup
openai.api_key = 'your_api_key_here'



# Generating code for each behavior
responses = []
for behavior in behaviors[:3]:
    responses.append(generate_behavior_code(behavior['name'], behavior['theory'], behavior["description"], behavior['behavior'], behavior['requires_state'], behavior['entity']))
    # wait 25 seconds between requests to avoid OpenAI API rate limit
    #time.sleep(25)
print(f"Generated code for {len(responses)} behaviors.\n")
print(f"First response:\n{responses[0]}")
# print(responses[0]['choices'][0]['text'])
