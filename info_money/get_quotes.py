#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
import json
from os import listdir
from os.path import isfile

import requests, pickle, pandas, time

from tcc import trend, sharpe


def download_data():
    ibovespa = pandas.read_csv('../data_original/tickers/Tickers_Ibovespa.csv', delimiter=';')
    for idx, value in ibovespa.iterrows():
        try:
            ticker = value['TICKER']

            params = {
                "page": 0,
                "numberItems": 505,
                "initialDate": "01/12/2019",
                "finalDate": "01/12/2021",
                "action": "more_quotes_history",
                "quotes_history_nonce": "38093cc80f",
                "symbol": ticker
            }

            headers = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            }

            response = requests.post(url='https://www.infomoney.com.br/wp-admin/admin-ajax.php', headers=headers, data=params)
            if response.status_code != 200:
                print(response.status_code, response.text)
                exit()

            text = json.loads(response.text)
            quotes = {}
            for data in text:
                #open = float(data[1].replace('.', '').replace(',', '.'))
                #variation = float(data[3].replace('.', '').replace(',', '.'))
                date = data[0]['display'].replace('\\', '')
                close = float(data[2].replace('.', '').replace(',', '.'))
                minimum = float(data[4].replace('.', '').replace(',', '.'))
                maximum = float(data[5].replace('.', '').replace(',', '.'))
                volume = data[6].replace('.', '').replace(',', '.')

                if 'M' in volume:
                    volume = volume.replace('M', '')
                    volume = float(volume) * 1000000
                elif 'B' in volume:
                    volume = volume.replace('B', '')
                    volume = float(volume) * 1000000000
                elif 'K' in volume:
                    volume = volume.replace('K', '')
                    volume = float(volume) * 1000

                quotes[date] = {
                    'close': close,
                    'min': minimum,
                    'max': maximum,
                    'volume': volume
                }

            handler = open('./data/{0}.history'.format(ticker.lower()), 'wb')
            pickle.dump(quotes, handler)
            handler.close()

            time.sleep(25)
        except Exception as ex:
            print(ex, ticker)


def sharpe_calc():
    acoes_dir = '../data_original/acoes/'
    files = listdir(acoes_dir)

    selic_2019 = 4.5
    selic_2020 = 2.0
    market_idx_reference = selic_2019 + selic_2020 / 2

    for file in files:
        original_file = acoes_dir + file
        if not isfile(original_file) or 'DS_Store' in file:
            continue

        file_handler = open(original_file, 'rb')
        data = pickle.load(file_handler)
        file_handler.close()

        close_values = []

        prices_ = data['prices']
        keys = list(prices_.keys())
        keys.reverse()
        for key in keys:
            close_values.append((prices_[key]['close'], key))

        # less than two years
        data['less_than_2_yrs'] = False
        if len(close_values) < 450:
            data['less_than_2_yrs'] = True
            continue

        aux = []
        moving_avg = []
        for close, date in close_values:
            aux.append(close)
            if len(aux) < 20:
                continue
            result = sum(aux) / 20
            moving_avg.append(result)
            data['prices'][date]['moving_average'] = result
            # move uma cada para frente
            aux = aux[1:]

        uptrend, trend_result = trend.calculate_trend(moving_avg, 20, 4)
        data['is_up_trend'] = uptrend
        data['trend_calculated_values'] = trend_result

        # profit.calculate_profitability()
        _sharpe, _yearly_volatility, _accumulated_profitability = sharpe.calculate_sharpe(close_values,
                                                                                          market_idx_reference)
        data['sharpe'] = _sharpe
        data['yearly_volatility'] = _yearly_volatility
        data['accumulated_profitability'] = _accumulated_profitability

        modificated_file = acoes_dir + file
        handler = open(modificated_file, 'wb')
        pickle.dump(data, handler)
        handler.close()
