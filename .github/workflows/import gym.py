import gym
import numpy as np
import random
from gym import spaces
from space_manufacturing_forecaster import SpaceManufacturingForecaster

class MarketShockTradingEnv(gym.Env):
    def __init__(self, historical_data, num_agents=3):
        super(MarketShockTradingEnv, self).__init__()
        self.historical_data = historical_data
        self.current_step = 0
        self.balance = 100000
        self.num_agents = num_agents
        self.manufacturing_forecaster = SpaceManufacturingForecaster()
        self.predicted_budget = []
        self.surplus_investment = 0
        self.investment_risk_factor = 1.0
        self.investment_portfolio = {"bonds": 0, "stocks": 0, "crypto": 0}
        self.manufacturing_history = []
        
        # Action Space: Buy/Sell/Hold decisions for assets
        self.action_space = spaces.MultiDiscrete([3] * 3)
        
        # Observation Space: Market data, space manufacturing forecasts, investment trends, and trading positions
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(33 + num_agents,), dtype=np.float32)
    
    def fetch_real_time_market_data(self):
        return {
            "bond_yield": random.uniform(1.5, 3.5),
            "stock_index": random.uniform(3000, 4000),
            "crypto_volatility": random.uniform(1.0, 5.0),
            "inflation_rate": random.uniform(0.01, 0.05),
            "market_volatility": random.uniform(1.0, 3.0)
        }
    
    def step(self, action):
        self.take_action(action)
        self.current_step += 1
        done = self.current_step >= len(self.historical_data)
        
        market_data = self.fetch_real_time_market_data()
        manufacturing_data = self.manufacturing_forecaster.fetch_space_manufacturing_data()
        regional_manufacturing_scores = [event['3D_printing_growth'] for event in manufacturing_data]
        avg_manufacturing_efficiency = np.mean(regional_manufacturing_scores) if regional_manufacturing_scores else 0
        resource_output = np.mean([event['resource_output'] for event in manufacturing_data]) if manufacturing_data else 0
        
        self.manufacturing_history.append([avg_manufacturing_efficiency, resource_output, market_data['inflation_rate'], market_data['market_volatility'], np.mean([event['asteroid_mining_investment'] for event in manufacturing_data])])
        if len(self.manufacturing_history) > 30:
            self.manufacturing_history.pop(0)
        
        predicted_efficiency = self.manufacturing_forecaster.predict_space_manufacturing_efficiency(self.manufacturing_history) if len(self.manufacturing_history) >= 30 else 0
        
        reward = sum(self.investment_portfolio.values()) + (predicted_efficiency * 1000)
        next_state = self._next_observation(market_data, predicted_efficiency, resource_output)
        return next_state, reward, done, {}
    
    def take_action(self, actions):
        asset_classes = ["bonds", "stocks", "crypto"]
        for i, asset in enumerate(asset_classes):
            if actions[i] == 0:
                self.investment_portfolio[asset] -= self.investment_portfolio[asset] * 0.1
            elif actions[i] == 2:
                self.investment_portfolio[asset] += self.surplus_investment * 0.3
        self.surplus_investment = max(0, self.surplus_investment - sum(self.investment_portfolio.values()))
        return self.investment_portfolio
    
    def _next_observation(self, market_data, predicted_efficiency, resource_output):
        obs = np.zeros(33 + self.num_agents)
        obs[6] = self.balance
        obs[7:12] = list(market_data.values())
        obs[12] = predicted_efficiency  # Space manufacturing efficiency forecast
        obs[13] = resource_output  # Resource extraction trends
        obs[14] = np.mean([event['asteroid_mining_investment'] for event in self.manufacturing_forecaster.fetch_space_manufacturing_data()])  # Investment in space mining
        obs[15:] = np.random.uniform(-5000, 5000, self.num_agents)  # Initial agent spending actions
        return obs
