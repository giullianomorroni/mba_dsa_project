#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

#PERSONAL DATA
import json
import pickle
from os import listdir
from os.path import isfile
import pandas as pd

age = 35
monthly_income = 8000
innitial_allocation = 15000
objective = ''

#FINANCIAL DATA
time_keep_investing = 10 # 5, 10, 15, 20> years
preferable_sector = []
acceptance_risk = 0 # 0, 10, 35, 50 percent
liquidity = 2 #2, 10, 20 ,30. 40 > dias
products_not_interested = []
allocation_in_low_risk = 80 # 100, 80, 60, 30, 20, 0 %
acceptance_maturity = 6 # 1, 6, 12, 24, 36 months


# SELECTED PRODUCTS
best_profitability = {'acoes': [], 'fundos': []}
best_sharpe = {'acoes': [], 'fundos': []}


def select_stocks():
	df = pd.DataFrame(columns=['Name', 'Type', 'Segment', 'Volatility', 'Profitability', 'Sharpe'])
	_dir = '../data_original/acoes/'
	files = listdir(_dir)

	for paper in files:
		original_file = _dir + paper
		if not isfile(original_file) or 'DS_Store' in paper:
			continue

		file_handler = open(original_file, 'rb')
		data = pickle.load(file_handler)
		file_handler.close()

		if data['less_than_2_yrs']:
			continue

		data = {
			'Name': paper, 'Type': 'acoes', 'Segment': None,
			'Volatility': data['yearly_volatility'],
			'Profitability': data['accumulated_profitability'],
			'Sharpe': data['sharpe']
		}

		df = df.append(data, ignore_index=True)

	_profitability = df.sort_values('Profitability', ascending=False).head(30)
	for idx, vlu in _profitability.iterrows():
		best_profitability['acoes'].append(vlu['Name'])

	_sharpe = df.sort_values('Sharpe', ascending=False).head(30)
	for idx, vlu in _sharpe.iterrows():
		best_sharpe['acoes'].append(vlu['Name'])


def select_funds():
	df = pd.DataFrame(columns=['Name', 'Type', 'Segment', 'Volatility', 'Profitability', 'Sharpe'])
	_dir = '../data_original/fundos/'
	files = listdir(_dir)

	for paper in files:
		original_file = _dir + paper
		if not isfile(original_file) or 'DS_Store' in paper:
			continue

		file_handler = open(original_file, 'rb')
		data = pickle.load(file_handler)
		file_handler.close()

		if data['less_than_2_yrs']:
			continue

		data = {
			'Name': paper,
			'Type': 'fundos',
			'Segment': None,
			'Volatility': data['timeframe']['last_24_months']['volatility'],
			'Profitability': data['timeframe']['last_24_months']['profitability'],
			'Sharpe': data['timeframe']['last_24_months']['sharpe_ratio']
		}

		df = df.append(data, ignore_index=True)

	_profitability = df.sort_values('Profitability', ascending=False).head(30)
	for idx, vlu in _profitability.iterrows():
		best_profitability['fundos'].append(vlu['Name'])

	_sharpe = df.sort_values('Sharpe', ascending=False).head(30)
	for idx, vlu in _sharpe.iterrows():
		best_sharpe['fundos'].append(vlu['Name'])


select_stocks()
select_funds()
print('best_profitability', best_profitability)
print('best_sharpe', best_sharpe)