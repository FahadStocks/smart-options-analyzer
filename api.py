import requests
import json

class StockDataFetcher:
    def __init__(self, yahoo_api_key, alpha_vantage_api_key):
        self.yahoo_api_key = yahoo_api_key
        self.alpha_vantage_api_key = alpha_vantage_api_key

    def fetch_yahoo_stock_data(self, symbol):
        url = f'https://yfapi.net/v6/finance/quote?symbols={symbol}'
        headers = {'x-api-key': self.yahoo_api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def fetch_alpha_vantage_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.alpha_vantage_api_key}'
        response = requests.get(url)
        return response.json()

    def fetch_options_chains(self, symbol):
        # Dummy implementation, needs actual data source
        return {"options": ["option1","option2"]}

    def calculate_volatility(self, stock_data):
        # A simple volatility calculation based on historical prices
        historical_prices = stock_data.get('Time Series (Daily)', {}).values()
        returns = [float(price['4. close']) for price in historical_prices]
        volatility = np.std(returns)
        return volatility

    def arabic_support(self):
        # Add Arabic translations for UI or other text
        return {'greeting': 'مرحبا', 'fetching_data': 'جارٍ جلب البيانات...'}

# Example of using the StockDataFetcher
# fetcher = StockDataFetcher('your_yahoo_api_key', 'your_alpha_vantage_api_key')
# stock_data = fetcher.fetch_yahoo_stock_data('AAPL')
# print(stock_data)