import time
import btc_fetcher
import volatility_calculator
import data_storage
from email_utils import send_email
from datetime import datetime, timedelta

# Setup
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

filename = r"C:\Users\damia\Desktop\Everything\Code\Personal\BitcoinAlert\volatility_data.csv"
volatility_threshold = 0.0012

# Email settings
sender_email = "damian.slaski.official@gmail.com"
sender_password = "grng jhye dnly dcnx"
recipient_emails = "damian.slaski.official@gmail.com"
email_subject = "Bitcoin Volatility Alert"

# Initialize CSV file
data_storage.initialize_file(filename)

# Initialize cooldown variables
last_notification_time = datetime.min  # Set to the earliest possible time

# Cooldown period 
cooldown_period = timedelta(hours=1)

# Fetch data and calculate volatility in a loop
while True:
    btc_price = btc_fetcher.fetch_price(url)
    if btc_price:
        volatility_calculator.add_price(btc_price)
        volatility_index = volatility_calculator.calculate_volatility()
        print(f"Current BTC Price: ${btc_price}")
        print(f"Bitcoin Volatility Index (VIX): {volatility_index}\n")
        data_storage.save_data(filename, btc_price, volatility_index)
        
        # Check if volatility exceeds the threshold and cooldown period has passed
        current_time = datetime.now()
        if volatility_index > volatility_threshold and (current_time - last_notification_time) > cooldown_period:
            email_body = (
                f"Alert!\n\n"
                f"Current BTC Price: ${btc_price}\n"
            )
            send_email(sender_email, sender_password, recipient_emails, email_subject, email_body)
            last_notification_time = current_time
    
    time.sleep(60)

