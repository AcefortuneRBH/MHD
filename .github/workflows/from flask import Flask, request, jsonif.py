from flask import Flask, request, jsonify
import numpy as np
from gym import spaces
from threading import Thread
import random

app = Flask(__name__)

class RealTimeInvestmentEnv(gym.Env):
    # ...existing code...

@app.route('/reset', methods=['POST'])
def reset():
    env = RealTimeInvestmentEnv(historical_data=[10000] * 12, num_agents=3)
    observation = env.reset()
    return jsonify(observation.tolist())

@app.route('/step', methods=['POST'])
def step():
    data = request.json
    actions = np.array(data['actions'])
    observation, reward, done, info = env.step(actions)
    return jsonify({
        'observation': observation.tolist(),
        'reward': reward,
        'done': done,
        'info': info
    })

if __name__ == '__main__':
    Thread(target=lambda: app.run(debug=True, port=5000)).start()
