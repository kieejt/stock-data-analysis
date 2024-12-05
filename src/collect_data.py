import yfinance as yf
import pandas as pd

stocks_info = [
    {"id": 1, "symbol": "AAPL", "name": "Apple Inc."},
    {"id": 2, "symbol": "MSFT", "name": "Microsoft Corporation"},
    {"id": 3, "symbol": "AMZN", "name": "Amazon.com, Inc."},
    {"id": 4, "symbol": "GOOGL", "name": "Alphabet Inc. (Google, Class A)"},
    {"id": 5, "symbol": "GOOG", "name": "Alphabet Inc. (Google, Class C)"},
    {"id": 6, "symbol": "TSLA", "name": "Tesla, Inc."},
    {"id": 7, "symbol": "META", "name": "Meta Platforms, Inc. (Facebook)"},
    {"id": 8, "symbol": "NVDA", "name": "NVIDIA Corporation"},
    {"id": 9, "symbol": "BRK-B", "name": "Berkshire Hathaway Inc. (Class B)"},
    {"id": 10, "symbol": "JPM", "name": "JPMorgan Chase & Co."}
]


def get_stock_data(symbol, start_date="2020-01-01", end_date="2024-01-01"):
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date, end=end_date)
    data.reset_index(inplace=True) 
    data.rename(columns={"open": "open", "high": "high", "low": "low", "close": "close", "adj close": "adjusted_close", 
                          "volume": "volume"}, inplace=True)
    return data

prices = pd.DataFrame()
stocks = pd.DataFrame()
for stock in stocks_info:
    id = 1
    symbol = stock["symbol"]
    stock_id = stock["id"]
    name = stock["name"]
    stocks_data = [{"id": stock_id, "symbol": symbol, "name": name}]
    stocks_data = pd.DataFrame(stocks_data)
    stocks = pd.concat([stocks, stocks_data], ignore_index=True)
    
    print(f"Tải dữ liệu cho {symbol} - {name}...")
    
    data = get_stock_data(symbol)
    
    if data is not None:
        data['Stock_id'] = stock_id
        
        
        prices = pd.concat([prices, data], ignore_index=True)
    else:
        print(f"Không tải được dữ liệu cho {symbol}.")



prices.insert(0, "id", range(1, 1 + len(prices)))
prices = prices[['id','Stock_id','Date', 'Open','High','Low', 'Close','Volume']]
prices.to_csv("prices_data.csv", index=False)

stocks_data = [{"id": stock_id, "symbol": symbol, "name": name}]

stocks.to_csv(f"stocks_data.csv", index=False)


print("Dữ liệu đã được lưu.")
