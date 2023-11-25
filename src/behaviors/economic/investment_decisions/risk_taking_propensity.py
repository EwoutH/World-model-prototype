
"""Risk-Taking Propensity in Investment Decisions.

This module simulates investor behavior with respect to risk-taking in investment decisions.
The behavior is based on the theory that investors have varying levels of risk tolerance,
which influences their choice of investments. Risk tolerance is often linked to factors
like age, income, investment goals, and market conditions.

References:
1. Markowitz, H. (1952). Portfolio Selection. The Journal of Finance.
2. Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. Econometrica.

Tests:
1. Test different levels of risk tolerance and validate the corresponding investment decisions.
2. Ensure that investors with higher risk tolerance select riskier investments.
"""

import random
import unittest

class Investor:
    def __init__(self, risk_tolerance):
        self.risk_tolerance = risk_tolerance
        self.investment_portfolio = []

    def make_investment_decision(self, investment_options):
        for option in investment_options:
            if option['risk_level'] <= self.risk_tolerance:
                self.investment_portfolio.append(option)
                print(f"Invested in {option['name']} with risk level {option['risk_level']}")

def simulate_investors():
    investment_options = [
        {'name': 'Stock A', 'risk_level': 0.7},
        {'name': 'Bond B', 'risk_level': 0.3},
        {'name': 'Stock C', 'risk_level': 0.9}
    ]
    investors = [Investor(random.uniform(0.1, 1.0)) for _ in range(5)]
    for investor in investors:
        investor.make_investment_decision(investment_options)

class TestRiskTakingPropensity(unittest.TestCase):
    def test_high_risk_tolerance(self):
        investor = Investor(0.9)
        investor.make_investment_decision([{'name': 'Stock C', 'risk_level': 0.8}])
        self.assertIn({'name': 'Stock C', 'risk_level': 0.8}, investor.investment_portfolio)

    def test_low_risk_tolerance(self):
        investor = Investor(0.2)
        investor.make_investment_decision([{'name': 'Stock A', 'risk_level': 0.7}])
        self.assertNotIn({'name': 'Stock A', 'risk_level': 0.7}, investor.investment_portfolio)

if __name__ == "__main__":
    simulate_investors()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
