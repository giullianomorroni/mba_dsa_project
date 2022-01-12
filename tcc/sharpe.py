#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import math
import statistics

import profit

"""
O valor retornado (Índice Sharpe) diz que para cada 1 ponto de risco
o ativo retornou X de percentual se comparado com um ativo livre
de risco. Ou seja, se o retorno for negativo, então seria mais
prudente não arriscar nesse produto, pois a voltailidade é alta
para o possível retorno. Se o valor é próximo de 1 então vale a pena
ter um ativo livre de risco também, acima de 2 pode-se dizer que começa
a valer a pena correr o risco.
"""


def calculate_sharpe(values, market_index):
	daily_profit = profit.calculate_daily(values)

	daily_volatility = statistics.stdev(daily_profit)
	yearly_volatility = daily_volatility * math.sqrt(252)

	monthly_profitability = profit.calculate_monthly(values)
	accumulated_profitability = sum(monthly_profitability)

	sharpe = (accumulated_profitability - market_index) / yearly_volatility

	print('daily_profit', daily_profit)

	print('daily_volatility', daily_volatility)
	print('yearly_volatility', yearly_volatility)

	print('monthly_profitability', monthly_profitability)
	print('accumulated_profitability', accumulated_profitability)

	print('sharpe', sharpe)

	print('initial investment', values[0][0], ' return', values[len(values) - 1][0] - values[0][0])

	return sharpe, yearly_volatility, accumulated_profitability
