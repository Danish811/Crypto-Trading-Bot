import json,websocket
import requests
import os
from binance import Client,BinanceSocketManager
from binance.exceptions import BinanceAPIException

AllTimeLow = {}
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)
#print(api_key,api_secret)
bsm = BinanceSocketManager(client)
cc = 'SOLUSD'
interval = '1m'
close = 0
high = 0
low = 0

def OrderBuy(cc,vol):
    order = client.create_test_order(
    symbol=cc,
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=vol)

def GetStats(cc: str, interval: str): 
   #-> tuple[int, int, int]:
    new1 = "https://testnet.binancefuture.com/en/futures/BTCUSDT"
    stream1 = f'wss://fstream.binance.com/ws/{cc}t@kline_{interval}'
   # POST /fapi/v1/order (HMAC SHA256)
   # socket = f'wss://stream.binance.com:443/ws-api/{cc}t@kline_{interval}'
   # socket2  = f'wss://testnet.binance.vision/ws-api/{cc}t@kline_{interval}'
   # new2 =  "https://testnet.binance.vision/api/v3/exchangeInfo"

    closes, highs, lows = [],[],[]

    def on_message(ws, message):
      json_message = json.loads(message)
      candle = json_message['k']
      is_candle_closed = candle['x']
      close = candle['c']
      high = candle['h']
      low = candle['l']
      vol = candle['v']
     # ls = []

      if is_candle_closed:
        #if close<=AllTimeLow: 
        #return low,high,close
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        AllTimeLow[cc] = min(AllTimeLow[cc],low)
        print("closes:" , closes)
        print("highs:" ,highs)
        print("lows:" ,lows)
        #print(vol)
      else:
        OrderBuy(cc,100) 
        print('buying')
        
    def on_close(ws,ys,zs):
       print('Connection Closed')

    ws = websocket.WebSocketApp(stream1, on_message = on_message, on_close = on_close)
    ws.run_forever()




#def OrderSell(cc:str,vol:int,price:int):