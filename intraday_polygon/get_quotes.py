#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
API_KEY = 'nUzWGoBZKaEkgRGNfLPr3THLFvgutPz_'

import requests, pickle, pandas, time, json, datetime

nasdaq = pandas.read_csv('../tcc/data/Tickers_Nasdaq_100.csv', delimiter=';')

quotes = {}
for idx, value in nasdaq.iterrows():
    try:
        ticker = value['TICKER']
        url = 'https://api.polygon.io/v2/aggs/ticker/{0}/range/1/day/2019-12-01/2021-12-01?adjusted=true&sort=asc&apiKey={1}'.format(
            ticker, API_KEY)

        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(response.status_code, data)

        ticker = data['ticker']
        results = data['results']
        for r in results:
            volume = r['v']
            close = r['c']
            date_milis = r['t']
            date = datetime.datetime.fromtimestamp(date_milis / 1000).strftime('%d/%m/%Y')

            quotes[date] = {
                'close': close,
                'volume': volume
            }

        handler = open('./data/{0}.history'.format(ticker.lower()), 'wb')
        pickle.dump(quotes, handler)
        handler.close()

        time.sleep(25)
    except Exception as ex:
        print(ex, ticker)
