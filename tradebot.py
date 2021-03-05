import websocket, json, pprint, talib, numpy
import apisettings
#import telegram_send
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/sxpusdt@kline_5m"
TRADE_SYMBOL = 'SXPUSDT'
TRADE_QUANTITY = 80
RSI_PERIOD = 4
RSI_OVERBOUGHT = 85
RSI_OVERSOLD = 18

closes = []
gainlosstotal = 0
in_position = False

client = Client(apisettings.API_KEY, apisettings.API_SECRET, tld='com')
def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("------CREATING ORDER------")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("AN ERROR HAS OCCURRED {}".format(e))
        return False

    return True

    
def on_open(ws):
    print('-------WEBSOCKET CONNECTED-------')

def on_close(ws):
    print('-------WEBSOCKET CONNECTION LOST-------')

def on_message(ws, message):
    global closes, in_position
    
    print('----------DATA----------')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("CANDLE CLOSED. LAST PRICE: {}".format(close))
        closes.append(float(close))
        print("CLOSES")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            RSI = talib.RSI(np_closes, RSI_PERIOD)
            print("-------RSI CALCULATED-------")
            LAST_RSI = RSI[-1]
            print("LAST RSI VALUE IS:  {}".format(LAST_RSI))

            if LAST_RSI > RSI_OVERBOUGHT:
                if in_position:
                    print("----RSI OVERBOUGHT LIMIT EXCEEDED! CREATING SELL ORDER----")
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        print("-----SELL ORDER COMPLETED-----")
                        in_position = False
                    """ FOR TELEGRAM BOT
                        a = float(candle['c'])
                        b = TRADE_QUANTITY
                        totalsellprice = a*b
                        gainloss = totalsellprice - totalbuyprice
                        gainlosstotal = gainlosstotal + gainloss
                        telegram_send.send(messages=["-----SOLD-----\n{} Pieces {}\n"
                        "Unit Price: {}\nTotal Price: {}\nGain/Loss: {}\nTotal Gain/Loss: {}".format(TRADE_QUANTITY,TRADE_SYMBOL,close,totalsellprice,gainloss, gainlosstotal)])
                    """
                else:
                    print("Rsi overbought limit exceeded, but we are not in position.")
            
            if LAST_RSI < RSI_OVERSOLD:
                if in_position:
                    print("Rsi overbought limit exceeded, but we are already in position.")
                else:
                    print("-----RSI OVERSOLD LIMIT EXCEEDED! CREATING BUY ORDER-----")
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        print("-----BUY ORDER COMPLETED-----")
                        in_position = True
                    """ FOR TELEGRAM BOT
                        a = float(candle['c'])
                        b = TRADE_QUANTITY
                        totalbuyprice = a*b
                        telegram_send.send(messages=["-----BOUGHT-----\n{} Pieces {}\n"
                        "Unit Price: {}\nTotal Price: {}".format(TRADE_QUANTITY,TRADE_SYMBOL,close,totalbuyprice)])
                    """               
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()