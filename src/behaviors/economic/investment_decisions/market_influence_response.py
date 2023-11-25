
"""Market Influence Response in Investment Decisions.

This module simulates how investors adjust their investment strategies based on market data and trends.
The behavior is grounded in behavioral finance theories that suggest investors are not always rational and
are influenced by psychological factors and market movements.

References:
1. Barberis, N., & Thaler, R. (2003). A survey of behavioral finance. Handbook of the Economics of Finance.
2. Shiller, R. J. (2003). From efficient markets theory to behavioral finance. Journal of Economic Perspectives.

Tests:
1. Test investor responses to upward market trends and validate increased investment amounts.
2. Test investor responses to downward market trends and validate decreased investment amounts.
"""

import random
import unittest

class Investor:
    def __init__(self, sensitivity_to_market):
        self.sensitivity_to_market = sensitivity_to_market
        self.investment_portfolio = []

    def adjust_investment(self, market_data):
        for investment in self.investment_portfolio:
            if market_data['market_trend'] == 'up' and self.sensitivity_to_market > 0.5:
                investment['amount'] *= 1.1
            elif market_data['market_trend'] == 'down' and self.sensitivity_to_market > 0.5:
                investment['amount'] *= 0.9
            print(f"Adjusted investment in {investment['name']} to {investment['amount']}")

    def make_investment(self, investment_option):
        self.investment_portfolio.append({'name': investment_option['name'], 'amount': investment_option['amount']})

def simulate_market_influence():
    market_data = {'market_trend': random.choice(['up', 'down'])}
    investment_options = [{'name': 'Stock A', 'amount': 1000}, {'name': 'Bond B', 'amount': 800}]
    investors = [Investor(random.uniform(0.1, 1.0)) for _ in range(5)]
    for investor in investors:
        investor.make_investment(random.choice(investment_options))
        investor.adjust_investment(market_data)

class TestMarketInfluenceResponse(unittest.TestCase):
    def test_upward_market_trend(self):
        investor = Investor(0.6)
        investor.make_investment({'name': 'Stock A', 'amount': 1000})
        investor.adjust_investment({'market_trend': 'up'})
        self.assertEqual(investor.investment_portfolio[0]['amount'], 1100)

    def test_downward_market_trend(self):
        investor = Investor(0.6)
        investor.make_investment({'name': 'Stock A', 'amount': 1000})
        investor.adjust_investment({'market_trend': 'down'})
        self.assertEqual(investor.investment_portfolio[0]['amount'], 900)

if __name__ == "__main__":
    simulate_market_influence()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
