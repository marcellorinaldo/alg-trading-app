import requests

# AlphaVantage API data
# Limits: 5 API requests per minute and 500 requests per day
API_KEY = 'ZY4Y0XKCPYTO1EQG'
BASE_URL = 'https://www.alphavantage.co'


class TradingAPI:
    def __init__(self):
        pass

    def getTimeSeriesIntraday(self, symbol, interval):
        """
        Returns intraday time series of the equity specified, covering extended trading hours where applicable (e.g., 4:00am to 8:00pm Eastern Time for the US market). Returns the most recent 1-2 months of intraday data and is best suited for short-term/medium-term charting and trading strategy development.

        Parameters
        ----------
        symbol : string
            The string that identifies the equity.
        interval : int
            Time interval (in minutes) between two consecutive data points in the time series. The following values are supported: 1, 5, 15, 30, 60.

        Returns
        -------
        times, open_prices, high_prices, low_prices, close_prices, volumes : lists
            Are self-explanatory, a tuple of lists of the following types: [string, float, float, float, float, int]. Returns None if error occured.
        """
        url = BASE_URL + '/query?function=TIME_SERIES_INTRADAY'
        url += f'&symbol={symbol}'
        url += f'&interval={str(interval)}'
        url += f'min&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
            #metadata = data['Meta Data']
            series = data[f'Time Series ({interval}min)']

            # retrieve the data to return
            times = []
            open_prices = []
            high_prices = []
            low_prices = []
            close_prices = []
            volumes = []
            for key, value in series.items():
                times += [f'{key}']
                open_prices += [float(value['1. open'])]
                high_prices += [float(value['2. high'])]
                low_prices += [float(value['3. low'])]
                close_prices += [float(value['4. close'])]
                volumes += [int(value['5. volume'])]

            # order by increasing age
            times.reverse()
            open_prices.reverse()
            high_prices.reverse()
            low_prices.reverse()
            close_prices.reverse()
            volumes.reverse()

            print('Data retrieved.')

            return times, open_prices, high_prices, low_prices, close_prices, volumes
        except:
            print(f'ERROR: request gone wrong.')

    def getTimeSeriesDailyAdjusted(self, symbol):
        """
        Returns raw (as-traded) daily open/high/low/close/volume values, daily adjusted close values, and historical split/dividend events of the global equity specified, covering 20+ years of historical data.

        Parameters
        ----------
        symbol : string
            The string that identifies the equity.

        Returns
        -------
        return times, open_prices, high_prices, low_prices, close_prices, adjusted_close_prices, volumes, dividend_amounts, split_coefficients : lists
            Are self-explanatory, a tuple of lists of the following types: [string, float, float, float, float, int, float, float]. Returns None if error occured.
        """
        url = BASE_URL + '/query?function=TIME_SERIES_DAILY_ADJUSTED'
        url += f'&symbol={symbol}'
        url += f'&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
            #metadata = data['Meta Data']
            series = data['Time Series (Daily)']

            # retrieve the data to return
            times = []
            open_prices = []
            high_prices = []
            low_prices = []
            close_prices = []
            adjusted_close_prices = []
            volumes = []
            dividend_amounts = []
            split_coefficients = []
            for key, value in series.items():
                times += [f'{key}']
                open_prices += [float(value['1. open'])]
                high_prices += [float(value['2. high'])]
                low_prices += [float(value['3. low'])]
                close_prices += [float(value['4. close'])]
                adjusted_close_prices += [float(value['5. adjusted close'])]
                volumes += [int(value['6. volume'])]
                dividend_amounts += [float(value['7. dividend amount'])]
                split_coefficients += [float(value['8. split coefficient'])]

            # order by increasing age
            times.reverse()
            open_prices.reverse()
            high_prices.reverse()
            low_prices.reverse()
            close_prices.reverse()
            volumes.reverse()

            print('Data retrieved.')

            return times, open_prices, high_prices, low_prices, close_prices, adjusted_close_prices, volumes, dividend_amounts, split_coefficients
        except:
            print(f'ERROR: request gone wrong.')
