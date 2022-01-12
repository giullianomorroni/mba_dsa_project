# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # encoding=utf8

from os import listdir
from os.path import isfile
import pickle
import trend
import profit
import sharpe

headers = {}

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
        result = sum(aux)/20
        moving_avg.append(result)
        data['prices'][date]['moving_average'] = result
        #move uma cada para frente
        aux = aux[1:]

    uptrend, trend_result = trend.calculate_trend(moving_avg, 20, 4)
    data['is_up_trend'] = uptrend
    data['trend_calculated_values'] = trend_result

    #profit.calculate_profitability()
    _sharpe, _yearly_volatility, _accumulated_profitability = sharpe.calculate_sharpe(close_values, market_idx_reference)
    data['sharpe'] = _sharpe
    data['yearly_volatility'] = _yearly_volatility
    data['accumulated_profitability'] = _accumulated_profitability

    modificated_file = acoes_dir + file
    handler = open(modificated_file, 'wb')
    pickle.dump(data, handler)
    handler.close()
