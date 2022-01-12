#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import functools


def calculate_daily(values):
	daily_profit = []

	for idx, _ in enumerate(values):
		if idx == 0:
			continue

		previous_value = values[idx - 1][0]
		actual_value = values[idx][0]
		rd = calculate_profitability(previous_value, actual_value, previous_value)
		daily_profit.append(rd)

	return daily_profit


def calculate_monthly(values):
	working_days_month = 21
	monthly_profit = []
	initial_investment = None

	count = 0
	for idx in range(0, len(values), working_days_month):
		count = idx
		if idx == 0:
			initial_investment = values[idx][0]
			continue

		actual_month = values[idx][0]
		previous_month = values[idx - working_days_month][0]
		rd = calculate_profitability(initial_investment, actual_month, previous_month)
		monthly_profit.append(rd)


	# Como estamos pulando de 21 em 21 os últimos valores pondem ter ficado de fora
	# Este trecho trata de pegar os resquícios do array
	if count < len(values):
		actual_month = values[len(values)-1][0]
		previous_month = values[count][0]
		rd = calculate_profitability(initial_investment, actual_month, previous_month)
		monthly_profit.append(rd)

	return monthly_profit


def calculate_profitability(initial_investment, actual_value, previous_value, taxes=0):
	liquid_prodit = actual_value - previous_value - taxes
	profitability = liquid_prodit * 100 / initial_investment
	return profitability
