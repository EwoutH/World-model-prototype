class IncomeDependentConsumption:
    """
    Simulates consumption choices based on varying income levels and economic conditions.
    
    This model is based on the economic principle that consumer spending is influenced by
    their income and the prevailing economic conditions. It demonstrates a basic form of
    consumption behavior in response to these factors.
    
    Attributes:
        income_level (float): The income level of the consumer.
    
    Methods:
        decide_consumption(economic_conditions): Decides the consumption amount based on
                                                 the economic conditions.
    """

    def __init__(self, income_level):
        self.income_level = income_level

    def decide_consumption(self, economic_conditions):
        """
        Decide the amount of consumption based on income level and economic conditions.
        
        Args:
            economic_conditions (str): The current economic conditions ('favorable' or 'unfavorable').
        
        Returns:
            float: The amount dedicated to consumption.
        """
        if economic_conditions == 'favorable':
            return self.income_level * 0.3  # Example: 30% of income for consumption
        else:
            return self.income_level * 0.2  # Example: 20% of income for consumption

# Tests for IncomeDependentConsumption
def test_income_dependent_consumption():
    # Test instance creation
    idc = IncomeDependentConsumption(1000)
    assert idc.income_level == 1000
    
    # Test consumption decision
    consumption_favorable = idc.decide_consumption('favorable')
    assert consumption_favorable == 1000 * 0.3
    consumption_unfavorable = idc.decide_consumption('unfavorable')
    assert consumption_unfavorable == 1000 * 0.2

if __name__ == "__main__":
    test_income_dependent_consumption()
    print("All tests passed for IncomeDependentConsumption.")
