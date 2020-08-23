import yfinance as yf

def get_stock_info(stock_ticker):
    yf_stock = yf.Ticker(stock_ticker)
    return yf_stock
