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
        interval : string
            Time interval (in minutes) between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min.

        Returns
        -------
        times, open_prices, high_prices, low_prices, close_prices, volumes : lists
            Are self-explanatory, a tuple of lists of the following types: [string, float, float, float, float, int]. Returns None if error occured.
        """
        print('Retrieving intraday time series.')
        url = BASE_URL + '/query?function=TIME_SERIES_INTRADAY'
        url += f'&symbol={symbol}'
        url += f'&interval={interval}'
        url += f'&apikey={API_KEY}'

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
        print('Retrieving adjusted daily time series.')
        url = BASE_URL + '/query?function=TIME_SERIES_DAILY_ADJUSTED'
        url += f'&symbol={symbol}'
        url += f'&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
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



    def getSMA(self, symbol, interval, time_period, series_type):
        """
        Returns the simple moving average (SMA) values. Refer to the investopedia article for further details: https://www.investopedia.com/articles/technical/052201.asp

        Parameters
        ----------
        symbol : string
            The string that identifies the equity.
        interval : string
            Time interval between two consecutive data points in the time series. The following values are supported: '1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'.
        time_period : int
            Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., time_period=60, time_period=200).
        series_type : string
            The desired price type in the time series. Four types are supported: 'close', 'open', 'high', 'low'.

        Returns
        -------
        times, smas : lists
            The time points and the calculated simple moving averages.
        """
        print('Retrieving SMA.')
        url = BASE_URL + '/query?function=SMA'
        url += f'&symbol={symbol}'
        url += f'&interval={interval}'
        url += f'&time_period={time_period}'
        url += f'&series_type={series_type}'
        url += f'&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
            series = data['Technical Analysis: SMA']

            # retrieve the data to return
            times = []
            smas = []
            for key, value in series.items():
                times += [f'{key}']
                smas += [float(value['SMA'])]

            # order by increasing age
            times.reverse()
            smas.reverse()

            print('Data retrieved.')

            return times, smas
        except:
            print(f'ERROR: request gone wrong.')



    def getBBANDS(self, symbol, interval, time_period, series_type):
        """
        Returns the Bollinger bands (BBANDS) values. Refer to the investopedia article for further details: https://www.investopedia.com/articles/technical/04/030304.asp.

        Parameters
        ----------
        symbol : string
            The string that identifies the equity.
        interval : string
            Time interval between two consecutive data points in the time series. The following values are supported: '1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'.
        time_period : int
            Number of data points used to calculate each BBANDS value. Positive integers are accepted (e.g., time_period=60, time_period=200).
        series_type : string
            The desired price type in the time series. Four types are supported: 'close', 'open', 'high', 'low'.

        Returns
        -------
        times, real_middle_bands, real_upper_bands, real_lower_bands : lists
            The time points and the middle, upper, and lower Bollinger bands.
        """
        print('Retrieving Bollinger bands.')
        url = BASE_URL + '/query?function=BBANDS'
        url += f'&symbol={symbol}'
        url += f'&interval={interval}'
        url += f'&time_period={time_period}'
        url += f'&series_type={series_type}'
        url += f'&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
            series = data['Technical Analysis: BBANDS']

            # retrieve the data to return
            times = []
            real_middle_bands = []
            real_upper_bands = []
            real_lower_bands = []
            for key, value in series.items():
                times += [f'{key}']
                real_middle_bands += [float(value['Real Middle Band'])]
                real_upper_bands += [float(value['Real Upper Band'])]
                real_lower_bands += [float(value['Real Lower Band'])]

            # order by increasing age
            times.reverse()
            real_middle_bands.reverse()
            real_upper_bands.reverse()
            real_lower_bands.reverse()

            print('Data retrieved.')

            return times, real_middle_bands, real_upper_bands, real_lower_bands
        except:
            print(f'ERROR: request gone wrong.')



    def getRSI(self, symbol, interval, time_period, series_type):
        """
        Returns the relative strength index (RSI) values. Refer to the investopedia article for further details: https://www.investopedia.com/articles/active-trading/042114/overbought-or-oversold-use-relative-strength-index-find-out.asp.

        Parameters
        ----------
        symbol : string
            The string that identifies the equity.
        interval : string
            Time interval between two consecutive data points in the time series. The following values are supported: '1min', '5min', '15min', '30min', '60min', 'daily', 'weekly', 'monthly'.
        time_period : int
            Number of data points used to calculate each RSI value. Positive integers are accepted (e.g., time_period=60, time_period=200).
        series_type : string
            The desired price type in the time series. Four types are supported: 'close', 'open', 'high', 'low'.

        Returns
        -------
        times, rsis : lists
            The time points and the RSI values.
        """
        print('Retrieving RSI values.')
        url = BASE_URL + '/query?function=RSI'
        url += f'&symbol={symbol}'
        url += f'&interval={interval}'
        url += f'&time_period={time_period}'
        url += f'&series_type={series_type}'
        url += f'&apikey={API_KEY}'

        # sending get request and saving the response as response object
        print('Request: ' + url + '.')
        response = requests.get(url)

        try:
            # extracting data in json format
            data = response.json()
            series = data['Technical Analysis: RSI']

            # retrieve the data to return
            times = []
            rsis = []
            for key, value in series.items():
                times += [f'{key}']
                rsis += [float(value['RSI'])]

            # order by increasing age
            times.reverse()
            rsis.reverse()

            print('Data retrieved.')

            return times, rsis
        except:
            print(f'ERROR: request gone wrong.')