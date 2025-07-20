import requests
from time import sleep

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

while True:
    try:
        response = requests.get(url)
        data = response.json()
        print("Now BTC/USDT:", data['price'])
    except Exception as e:
        print("Veri alınamadı:", e)
    sleep(5)
