# volatility_calculator.py
from collections import deque
import numpy as np

# Initialize price history
price_history = deque(maxlen=20)

def add_price(price):
    price_history.append(price)

def calculate_volatility():
    if len(price_history) < 2:
        return 0  # Not enough data to calculate volatility
    log_returns = np.diff(np.log(price_history))
    volatility = np.std(log_returns)
    return volatility
