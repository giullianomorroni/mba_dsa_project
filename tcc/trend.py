#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import numpy as np


def calculate_trend(values, cycle, observation_by_cycle=5):
    """
    :param observation_by_cycle:
    :param values all values in an array shape
    :param cycle an int value determining the cycle to group values
    :param observation_by_cycle number of observations to use in the cycle:
    :return up_trending(True if percent grater than 65%), result (mean calculated for cycles):
    """

    means_cycle = []
    for idx in range(0, len(values), cycle):
        _mean = np.mean(values[idx:idx + observation_by_cycle])
        means_cycle.append(_mean)

    result = []
    for idx, vl in enumerate(means_cycle):
        if idx == 0:
            continue
        is_up_trending = means_cycle[idx-1] < means_cycle[idx]
        result.append(is_up_trending)

    total = len(result)
    up = result.count(True)

    up_trending = (up * 100 / total) > 70
    return up_trending, result

