import requests

def fetch_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["price"]) 
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
