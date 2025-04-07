import time
import csv

class DynamicLiquidityPool:


    """
    A class to represent a dynamic liquidity pool for staking tokens and distributing rewards.

    Attributes:
    -----------
    stakes : dict
        A dictionary to store the amount of tokens staked by each user.
    rewards : dict
        A dictionary to store the rewards earned by each user.
    liquidity_pool : float
        The total amount of liquidity available in the pool.
    withdrawal_requests : dict
        A dictionary to store withdrawal requests with unlock times.
    pool_lock_period : int
        The lock period (in seconds) for withdrawal requests.
    base_yield : float
        The base annual yield for staking.
    utilization_factor : float
        A factor to determine dynamic yield scaling based on pool utilization.

    Methods:
    --------
    stake_tokens(user, amount):
        Stakes a specified amount of tokens for a user.
    request_withdrawal(user, amount):
        Requests a withdrawal of a specified amount of tokens for a user.
    withdraw_tokens(user):
        Withdraws tokens for a user if the lock period has expired.
    calculate_dynamic_yield():
        Calculates the dynamic yield based on pool utilization.
    distribute_rewards():
        Distributes rewards to users based on their stakes and the dynamic yield.
    get_stake(user):
        Returns the amount of tokens staked by a user.
    get_rewards(user):
        Returns the rewards earned by a user.
    get_liquidity_pool():
        Returns the total liquidity available in the pool.
    get_dynamic_yield():
        Returns the current dynamic yield.
    generate_csv_report():
        Generates a CSV report of all withdrawal requests.
    """
    def __init__(self):
        self.stakes = {}
        self.rewards = {}
        self.liquidity_pool = 100000  # Initial pool liquidity
        self.withdrawal_requests = {}
        self.pool_lock_period = 3 * 24 * 60 * 60  # 3-day lock period
        self.base_yield = 0.05  # 5% annual yield
        self.utilization_factor = 0.3  # Determines dynamic yield scaling

    def stake_tokens(self, user, amount):
        if user not in self.stakes:
            self.stakes[user] = 0
        self.stakes[user] += amount
        self.liquidity_pool += amount  # Increase liquidity pool
        return self.stakes[user]

    def request_withdrawal(self, user, amount):
        if user not in self.stakes or self.stakes[user] < amount:
            return None
        unlock_time = time.time() + self.pool_lock_period
        self.withdrawal_requests[user] = {"amount": amount, "unlock_time": unlock_time}
        return {"user": user, "unlock_time": unlock_time}

    def withdraw_tokens(self, user):
        if user not in self.withdrawal_requests:
            return {"error": "No withdrawal request found"}
        if time.time() < self.withdrawal_requests[user]["unlock_time"]:
            return {"error": "Tokens are still locked"}
        amount = self.withdrawal_requests[user]["amount"]
        if self.liquidity_pool >= amount:
            self.stakes[user] -= amount
            self.liquidity_pool -= amount
            del self.withdrawal_requests[user]
            return {"user": user, "withdrawn_amount": amount}
        return {"error": "Insufficient liquidity in the pool"}

    def calculate_dynamic_yield(self):
        utilization_ratio = 1 - (self.liquidity_pool / (sum(self.stakes.values()) + self.liquidity_pool))
        adjusted_yield = self.base_yield * (1 + self.utilization_factor * utilization_ratio)
        return max(0.01, adjusted_yield)  # Ensuring a minimum of 1% yield

    def distribute_rewards(self):
        dynamic_yield = self.calculate_dynamic_yield()
        for user, stake in self.stakes.items():
            reward = stake * dynamic_yield
            self.rewards[user] = self.rewards.get(user, 0) + reward
        return self.rewards

    def get_stake(self, user):
        return self.stakes.get(user, 0)

    def get_rewards(self, user):
        return self.rewards.get(user, 0)

    def get_liquidity_pool(self):
        return self.liquidity_pool

    def get_dynamic_yield(self):
        return self.calculate_dynamic_yield()

    def generate_csv_report(self):
        filename = "withdrawal_logs.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["user", "amount", "unlock_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user, request in self.withdrawal_requests.items():
                writer.writerow({
                    "user": user,
                    "amount": request["amount"],
                    "unlock_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(request["unlock_time"]))
                })
        return filename
