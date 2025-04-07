import numpy as np
import random
import gym
from gym import spaces
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

class SpaceEnergyForecaster:
    # ...existing code...

class MarketShockTradingEnv(gym.Env):
    # ...existing code...

@app.route('/reset', methods=['POST'])
def reset():
    # ...existing code...

@app.route('/step', methods=['POST'])
def step():
    # ...existing code...

if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(debug=True, port=5000)).start()
