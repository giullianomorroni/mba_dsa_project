#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

from os import listdir
from os.path import isfile
import pickle

headers = {}

original_dir = '../data_original/info_money/data/'
modificated_dir = '../info_money/data/'

files = listdir(original_dir)

for file in files:
    original_file = original_dir + file
    if not isfile(original_file) or 'DS_Store' in file:
        continue

    file_handler = open(original_file, 'rb')
    data = pickle.load(file_handler)
    file_handler.close()

    close_values = []
    min_values = []
    max_values = []
    volume_values = []

    keys = list(data.keys())
    keys.reverse()

    for key in keys:
        close_values.append((data[key]['close'], key))
        min_values.append((data[key]['min'], key))
        max_values.append((data[key]['max'], key))
        volume_values.append((data[key]['volume'], key))

    aux_close_moving_avg = []
    for close, date in close_values:
        aux_close_moving_avg.append(close)
        if len(aux_close_moving_avg) < 20:
            continue
        moving_avg = sum(aux_close_moving_avg)/20
        data[date]['moving_average'] = moving_avg

        aux_close_moving_avg = aux_close_moving_avg[1:]

    modificated_file = modificated_dir + file
    handler = open(modificated_file, 'wb')
    pickle.dump(data, handler)
    handler.close()
