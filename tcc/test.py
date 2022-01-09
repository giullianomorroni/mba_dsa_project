#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

from os import listdir
from os.path import isfile
import pickle
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from tcc import sharpe


# files = listdir('../info_money/data/')
#
# for file in files:
#     paper = file
#     print(paper)
#     file = '../info_money/data/' + file
#     if not isfile(file) or 'DS_Store' in file:
#         continue
#     file_handler = open(file, 'rb')
#     data = pickle.load(file_handler)
#     file_handler.close()
#
#     keys = list(data.keys())
#     keys.reverse()
#
#     moving_average_values = []
#     close_values = []
#
#     for key in keys:
#         value = data[key]
#
#         if 'moving_average' not in value:
#             moving_average_values.append(value['close'])
#             close_values.append(value['close'])
#             continue
#
#         moving_average_values.append(value['moving_average'])
#         close_values.append(value['close'])
#
#     selic = 9
#     sharpe.calculate_sharpe(close_values, market_index=selic)

t = []
v = 10
for x in range(0, 100):
    t.append(v)
    v += 1

print(t)
sharpe.calculate_sharpe(t, 10)
