# BINANCE TRADEBOT

This tradebot works on Binance.

It's a simple python bot that works with RSI Indicator (Relative Strength Index)

It doesn't guarantee any profit. And I am not responsible for your trades.

If you do your settings well, you can make profit but I don't guarantee anything.

If you combine it with another algorithm, you can be sure it will work better.
## Installation

Install [TA-Lib](https://mrjbq7.github.io/ta-lib/) library.

Install [python-binance](https://github.com/sammchardy/python-binance) library.

Install [numpy](https://numpy.org/install/) library.

Install [websocket](https://pypi.org/project/websocket-client/) library.

And if you want to get messages from tradebot, you can set [telegram-send](https://pypi.org/project/telegram-send/) library. And check [here](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)


## Usage

```python
#THESE ARE JUST SAMPLE SETTINGS. PLEASE BE SURE YOUR OWN SETTINGS!
#set the SOCKET. You can change your pair and time period. 5m means 5 minutes, 1h means 1 hour.
#For example:
#SOCKET = "wss://stream.binance.com:9443/ws/btcbusd@kline_1h"
SOCKET = "wss://stream.binance.com:9443/ws/sxpusdt@kline_5m"
#set your pair. For example:
#TRADE_SYMBOL = 'BTCBUSD'
TRADE_SYMBOL = 'SXPUSDT'
#set how many you want to buy.
TRADE_QUANTITY = 80
#set your rsi period.
RSI_PERIOD = 4
#set your rsi overbought limit.
RSI_OVERBOUGHT = 85
#set your rsi oversold limit.
RSI_OVERSOLD = 18
```
You should put your Binance API settings into apisettings.py

You can get these from Binance.

```python
API_KEY = 'PUT YOUR BINANCE API KEY HERE'
API_SECRET = 'PUT YOUR BINANCE API SECRET HERE'
```
If you want to get messages from tradebot, set the [telegram-send](https://pypi.org/project/telegram-send/) library first. Check [here](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580).
 And then delete the quotes on code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

