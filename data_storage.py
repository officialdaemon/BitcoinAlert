import csv
from datetime import datetime
import os

def initialize_file(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "BTC Price", "Volatility Index"])

def save_data(filename, price, volatility_index):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, price, volatility_index])
