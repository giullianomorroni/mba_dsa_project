#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

import functools


def calculate_daily(values):
	daily_profit = []

	for idx, _ in enumerate(values):
		if idx == 0:
			continue

		rd = calculate_profitability(values[idx-1], values[idx], values[idx-1])
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
			initial_investment = values[idx]
			continue

		actual_month = values[idx]
		previous_month = values[idx - working_days_month]
		rd = calculate_profitability(initial_investment, actual_month, previous_month)
		monthly_profit.append(rd)


	# Como estamos pulando de 21 em 21 os últimos valores pondem ter ficado de fora
	# Este trecho trata de pegar os resquícios do array
	if count < len(values):
		actual_month = values[len(values)-1]
		previous_month = values[count]
		rd = calculate_profitability(initial_investment, actual_month, previous_month)
		monthly_profit.append(rd)

	return monthly_profit


def calculate_profitability(initial_investiment, actual_value, previous_value, taxes=0):
	liquid_prodit = actual_value - previous_value - taxes
	profitability = liquid_prodit * 100 / initial_investiment
	return profitability
