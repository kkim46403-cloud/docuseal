import requests

TOKEN = "你的token"
CHAT_ID = "你的chat_id"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}
    return float(requests.get(url, params=params).json()["price"])

def run():
    btc = get_price("BTCUSDT")
    eth = get_price("ETHUSDT")

    msg = f"""📊 行情播报

BTC: {btc}
ETH: {eth}
"""
    send(msg)

if __name__ == "__main__":
    run()