# Consumption Patterns

This subcategory within the economic category focuses on modeling various aspects of consumer behavior. It includes two specific behaviors: Consumer Preference Adaptation and Income-Dependent Consumption. These models are designed to simulate how consumers adapt their preferences and spending based on external factors such as market trends, social influences, and income levels.

## Behaviors

### Consumer Preference Adaptation
- **File**: `consumer_preference_adaptation.py`
- **Description**: This behavior models the evolution of consumer preferences influenced by market trends and social factors. It represents the dynamic nature of consumer choices in response to external stimuli.
- **Usage**: Instantiate the `ConsumerPreferenceAdaptation` class with initial preferences and influence factors, then use the `update_preference` method to simulate preference changes.

### Income-Dependent Consumption
- **File**: `income_dependent_consumption.py`
- **Description**: This model simulates consumption decisions based on the consumer's income level and the prevailing economic conditions. It reflects the fundamental economic principle that consumer spending is closely tied to income.
- **Usage**: Create an instance of the `IncomeDependentConsumption` class with a specific income level. Use the `decide_consumption` method to determine consumption amounts under different economic conditions.

## Instructions for Use
1. Import the required class from the respective Python file.
2. Create an instance of the class with the necessary initial parameters.
3. Call the methods provided by the class to simulate the respective behavior.
4. Utilize the test cases within each file to validate the behavior under different scenarios.
