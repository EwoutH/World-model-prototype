class ConsumerPreferenceAdaptation:
    """
    Models the evolution of consumer preferences over time based on external influences.
    
    This behavior is grounded in the theory of consumer behavior, where preferences are
    not static but evolve due to factors like market trends, advertising, and social interactions.
    The model uses a simple linear combination of these influences to update the preference.
    
    Attributes:
        preference (float): The initial consumer preference level.
        market_influence (float): Factor determining how much market trends affect preferences.
        social_influence (float): Factor determining the influence of social trends on preferences.
    
    Methods:
        update_preference(market_trend, social_trend): Updates the preference based on market
                                                       and social trends.
    """

    def __init__(self, initial_preference, market_influence_factor, social_influence_factor):
        self.preference = initial_preference
        self.market_influence = market_influence_factor
        self.social_influence = social_influence_factor

    def update_preference(self, market_trend, social_trend):
        """
        Update the consumer preference based on market and social trends.
        
        Args:
            market_trend (float): The current market trend indicator.
            social_trend (float): The current social trend indicator.
        
        Returns:
            float: The updated preference level.
        """
        self.preference = (self.preference 
                           + market_trend * self.market_influence 
                           + social_trend * self.social_influence)
        return self.preference

# Tests for ConsumerPreferenceAdaptation
def test_consumer_preference_adaptation():
    # Test instance creation
    cpa = ConsumerPreferenceAdaptation(0.5, 0.3, 0.2)
    assert cpa.preference == 0.5
    assert cpa.market_influence == 0.3
    assert cpa.social_influence == 0.2
    
    # Test preference update
    updated_pref = cpa.update_preference(0.1, 0.2)
    assert updated_pref == 0.5 + 0.1 * 0.3 + 0.2 * 0.2

if __name__ == "__main__":
    test_consumer_preference_adaptation()
    print("All tests passed for ConsumerPreferenceAdaptation.")
