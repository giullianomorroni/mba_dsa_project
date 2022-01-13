# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # encoding=utf8

# var = {
# 	"positive_months": 313,
# 	"negative_months": 0,
# 	"months_better_than_index": 147,
# 	"months_worse_than_index": 166,
#     "best_monthly_return": 3.2852,
# 	"worst_monthly_return": 0.1345,
# 	"years": {
# 		"1996": {"accrued": 26.8174, "year": 26.8174, "1": 2.3195, "2": 2.3068, "3": 2.198, "4": 2.0341, "5": 2.0046,
# 		         "6": 1.9406, "7": 1.9133, "8": 1.953, "9": 1.8844, "10": 1.8569, "11": 1.7945, "12": 1.7908},
# 		"1997": {"accrued": 58.0021, "year": 24.5902, "1": 1.7406, "2": 1.6605, "3": 1.6257, "4": 1.6563, "5": 1.5784,
# 		         "6": 1.5919, "7": 1.6059, "8": 1.5808, "9": 1.5811, "10": 1.6817, "11": 2.9848, "12": 2.9151},
# 		"1998": {"accrued": 103.1493, "year": 28.5737, "1": 2.6663, "2": 2.1073, "3": 2.1803, "4": 1.6948, "5": 1.6277,
# 		         "6": 1.5969, "7": 1.694, "8": 1.4726, "9": 2.4926, "10": 2.9253, "11": 2.5756, "12": 2.378},
# 		"1999": {"accrued": 154.1978, "year": 25.1286, "1": 2.1742, "2": 2.3492, "3": 3.2852, "4": 2.2755, "5": 1.9595,
# 		         "6": 1.6348, "7": 1.6226, "8": 1.5464, "9": 1.4678, "10": 1.3745, "11": 1.3725, "12": 1.5825},
# 		"2000": {"accrued": 198.2227, "year": 17.3192, "1": 1.4413, "2": 1.4405, "3": 1.4389, "4": 1.2838, "5": 1.4881,
# 		         "6": 1.3852, "7": 1.3015, "8": 1.395, "9": 1.217, "10": 1.2795, "11": 1.2156, "12": 1.1938},
# 		"2001": {"accrued": 249.7741, "year": 17.2862, "1": 1.2586, "2": 1.0096, "3": 1.25, "4": 1.1804, "5": 1.3344,
# 		         "6": 1.2731, "7": 1.5015, "8": 1.6012, "9": 1.3229, "10": 1.534, "11": 1.3933, "12": 1.3936},
# 		"2002": {"accrued": 316.6077, "year": 19.1077, "1": 1.5319, "2": 1.2475, "3": 1.3699, "4": 1.4829, "5": 1.4037,
# 		         "6": 1.3097, "7": 1.5338, "8": 1.4456, "9": 1.3808, "10": 1.6414, "11": 1.5335, "12": 1.7341},
# 		"2003": {"accrued": 413.4598, "year": 23.2478, "1": 1.9654, "2": 1.8275, "3": 1.7731, "4": 1.866, "5": 1.9594,
# 		         "6": 1.8508, "7": 2.0756, "8": 1.7646, "9": 1.6691, "10": 1.6332, "11": 1.3381, "12": 1.3657},
# 		"2004": {"accrued": 496.5068, "year": 16.174, "1": 1.2606, "2": 1.0796, "3": 1.3744, "4": 1.1747, "5": 1.2249,
# 		         "6": 1.2236, "7": 1.2818, "8": 1.2861, "9": 1.2441, "10": 1.2081, "11": 1.2488, "12": 1.4799},
# 		"2005": {"accrued": 609.8405, "year": 18.9996, "1": 1.3828, "2": 1.2159, "3": 1.522, "4": 1.408, "5": 1.5004,
# 		         "6": 1.5844, "7": 1.5098, "8": 1.6529, "9": 1.4997, "10": 1.4033, "11": 1.3763, "12": 1.4668},
# 		"2006": {"accrued": 716.5093, "year": 15.0271, "1": 1.4256, "2": 1.1401, "3": 1.4183, "4": 1.0754, "5": 1.2782,
# 		         "6": 1.1822, "7": 1.167, "8": 1.2513, "9": 1.0532, "10": 1.0901, "11": 1.0173, "12": 0.9843},
# 		"2007": {"accrued": 812.9864, "year": 11.8158, "1": 1.0784, "2": 0.8698, "3": 1.0486, "4": 0.9406, "5": 1.0221,
# 		         "6": 0.9015, "7": 0.9681, "8": 0.9878, "9": 0.8006, "10": 0.9241, "11": 0.8398, "12": 0.8394},
# 		"2008": {"accrued": 926.0123, "year": 12.3798, "1": 0.9219, "2": 0.795, "3": 0.8385, "4": 0.8978, "5": 0.8712,
# 		         "6": 0.9482, "7": 1.0642, "8": 1.0128, "9": 1.0985, "10": 1.1739, "11": 0.9958, "12": 1.1111},
# 		"2009": {"accrued": 1027.3491, "year": 9.8768, "1": 1.0428, "2": 0.8527, "3": 0.9665, "4": 0.8356, "5": 0.7665,
# 		         "6": 0.7514, "7": 0.7841, "8": 0.6915, "9": 0.6915, "10": 0.6912, "11": 0.659, "12": 0.7239},
# 		"2010": {"accrued": 1137.2767, "year": 9.751, "1": 0.6582, "2": 0.5925, "3": 0.7569, "4": 0.664, "5": 0.7501,
# 		         "6": 0.7908, "7": 0.8592, "8": 0.8863, "9": 0.8446, "10": 0.8057, "11": 0.8056, "12": 0.9272},
# 		"2011": {"accrued": 1280.7422, "year": 11.5953, "1": 0.8606, "2": 0.8424, "3": 0.9189, "4": 0.8388, "5": 0.9853,
# 		         "6": 0.9527, "7": 0.9666, "8": 1.0724, "9": 0.9398, "10": 0.8807, "11": 0.8586, "12": 0.9047},
# 		"2012": {"accrued": 1396.6908, "year": 8.3976, "1": 0.8853, "2": 0.7416, "3": 0.8083, "4": 0.6999, "5": 0.7325,
# 		         "6": 0.6386, "7": 0.6754, "8": 0.6866, "9": 0.5372, "10": 0.6073, "11": 0.5445, "12": 0.5342},
# 		"2013": {"accrued": 1517.3934, "year": 8.0646, "1": 0.5866, "2": 0.4816, "3": 0.5377, "4": 0.6008, "5": 0.5849,
# 		         "6": 0.5919, "7": 0.7088, "8": 0.6958, "9": 0.6991, "10": 0.8034, "11": 0.7105, "12": 0.7804},
# 		"2014": {"accrued": 1692.2984, "year": 10.814, "1": 0.8398, "2": 0.7827, "3": 0.76, "4": 0.8154, "5": 0.8583,
# 		         "6": 0.8174, "7": 0.9404, "8": 0.8595, "9": 0.9006, "10": 0.9448, "11": 0.8379, "12": 0.9558},
# 		"2015": {"accrued": 1929.5836, "year": 13.2392, "1": 0.9293, "2": 0.8185, "3": 1.0361, "4": 0.9483, "5": 0.9838,
# 		         "6": 1.0658, "7": 1.1773, "8": 1.1075, "9": 1.1075, "10": 1.1077, "11": 1.0552, "12": 1.1613},
# 		"2016": {"accrued": 2213.7071, "year": 13.9991, "1": 1.0549, "2": 1.0015, "3": 1.1605, "4": 1.0545, "5": 1.1075,
# 		         "6": 1.1605, "7": 1.1075, "8": 1.2136, "9": 1.1075, "10": 1.0474, "11": 1.0369, "12": 1.1218},
# 		"2017": {"accrued": 2443.3535, "year": 9.9255, "1": 1.0846, "2": 0.8638, "3": 1.0504, "4": 0.7853, "5": 0.9256,
# 		         "6": 0.8081, "7": 0.7972, "8": 0.8015, "9": 0.6377, "10": 0.6431, "11": 0.5674, "12": 0.5377},
# 		"2018": {"accrued": 2606.6713, "year": 6.4214, "1": 0.5834, "2": 0.4649, "3": 0.5316, "4": 0.5175, "5": 0.5175,
# 		         "6": 0.5175, "7": 0.5422, "8": 0.5669, "9": 0.4681, "10": 0.543, "11": 0.4936, "12": 0.4936},
# 		"2019": {"accrued": 2767.9852, "year": 5.9599, "1": 0.543, "2": 0.4936, "3": 0.4688, "4": 0.5183, "5": 0.543,
# 		         "6": 0.4688, "7": 0.5678, "8": 0.5017, "9": 0.4638, "10": 0.4793, "11": 0.3804, "12": 0.3747},
# 		"2020": {"accrued": 2847.079, "year": 2.7578, "1": 0.3766, "2": 0.2937, "3": 0.3384, "4": 0.2849, "5": 0.2358,
# 		         "6": 0.2123, "7": 0.1943, "8": 0.1599, "9": 0.157, "10": 0.157, "11": 0.1495, "12": 0.1644},
# 		"2021": {"accrued": 2977.4465, "year": 4.4236, "1": 0.1495, "2": 0.1345, "3": 0.2011, "4": 0.2078, "5": 0.2703,
# 		         "6": 0.3078, "7": 0.3556, "8": 0.428, "9": 0.442, "10": 0.486, "11": 0.5867, "12": 0.7691},
# 		"2022": {"accrued": 2982.7972, "year": 0.1739, "1": 0.1739}},
#     "timeframe": {
# 	    "last_3_months": {"profitability": 1.89, "volatility": 0.0647, "sharpe_ratio": null},
#          "last_6_months": {"profitability": 3.19, "volatility": 0.1003, "sharpe_ratio": null},
#          "last_12_months": {"profitability": 4.57, "volatility": 0.1363, "sharpe_ratio": null},
#          "last_24_months": {"profitability": 7.4, "volatility": 0.1189, "sharpe_ratio": null},
#          "last_36_months": {"profitability": 13.76, "volatility": 0.1184, "sharpe_ratio": null},
#          "ytd": {"profitability": 0.17, "volatility": null, "sharpe_ratio": null},
#          "mtd": {"profitability": 0.17, "volatility": null, "sharpe_ratio": null},
#          "begin": {"profitability": 2982.8, "volatility": 0.4122, "sharpe_ratio": null}
#     }
# }
#
#
# var2 = {"fund":
# 	        {"nicename":"BRADESCO FI RF DÍVIDA EXTERNA CRÉDITO SOBERANO",
# 		    "cnpj":74326471000120},
# 	"anbima":{"class":"RENDA FIXA - INV. NO EXTERIOR - DÍVIDA EXTERNA"},
# 	    "target_group":"O Fundo destina-se ao público em geral que deseja obter rendimento atrelado à "
# 	                   "percepção internacional do risco associado à economia brasileira",
# 	    "objective":"O Fundo tem por objetivo proporcionar aos seus cotistas rentabilidade através das "
# 	                "oportunidades oferecidas pelos mercados internacionais de dívida externa brasileira "
# 	                "e taxa de juros",
# 	    "investment_policy":"O Fundo pretende atingir o seu objetivo investindo, no mínimo, 80% de seus "
# 	                        "recursos em títulos representativos da dívida externa de responsabilidade "
# 	                        "da União. No máximo, 20% de seus recursos são investidos em títulos de c"
# 	                        "rédito transacionados no mercado internacional. As operações nos mercados "
# 	                        "de derivativos somente poderão ser realizadas com o objetivo de \"hedge\" dos "
# 	                        "ativos integrantes da carteira do Fundo.",
# 	    "administration_fee":{
# 		    "fee_type":"Fixa",
# 		    "fee":0.5,
# 		    "min":0.0,
# 		    "max":0.0},
# 	    "minimum_application_value":100.0,
# 	    "performance_fee":null,
# 	    "fund_perfomance_fee":{
# 		    "fee":null,
# 		    "calc":null,
# 		    "exists":false,
# 		    "information":null,
# 		    "index_reference":null,
# 		    "percent_index_reference":null,
# 		    "coupon":null},
# 	    "closing_quote_period":"Fechamento",
# 	    "day_type_for_redemption":"Dias Úteis",
# 	    "days_for_quote_redemption":1.0,
# 	    "days_for_money_redemption":4.0,
# 	    "permanency_minimum_amount":100.0,
# 	    "bought_quote_conversion_period":1.0,
# 	    "term":{
# 		    "redemption_quotation":1.0,
# 		    "redemption_payment":4.0,
# 		    "subscription_deadline":1.0,
# 		    "subscription_type":"Fechamento",
# 		    "redemption_quotation_type":"Dias Úteis",
# 		    "cancelation_quotation_type":"Fechamento"}
#         }

import json
from os import listdir
from os.path import isfile

import requests, pickle, pandas, time

headers = {
	"accept": "application/json, text/javascript, */*",
}

funds = pandas.read_csv('../data_original/tickers/Fundos_Investimentos.csv', delimiter=';')


def __get_profit__(ticker, index):
	profit_url = 'https://api.maisretorno.com/v2/indexes/stats/{0}/relative/{1}/details'.format(ticker, index)
	response = requests.get(url=profit_url, headers=headers)
	if response.status_code != 200:
		print(response.status_code, response.json())
		return {}
	return response.json()


def __get_details__(ticker):
	details_url = 'https://api.maisretorno.com/v2/funds/policies/{0}'.format(ticker)
	response = requests.get(url=details_url, headers=headers)
	if response.status_code != 200:
		print(response.status_code, response.json())
		return {}
	return response.json()


def download_data():
	for idx, value in funds.iterrows():
		try:
			ticker = value['Name']
			index = value['Index']

			details_data = __get_details__(ticker)
			profit_data = __get_profit__(ticker, index)

			details_data['timeframe'] = profit_data['timeframe']

			handler = open('../data_original/fundos/{0}.details'.format(ticker.lower()), 'wb')
			pickle.dump(details_data, handler)
			handler.close()

			time.sleep(5)
		except Exception as e:
			print(e)


def sharpe_calc():
	_dir = '../data_original/fundos/'
	files = listdir(_dir)

	selic_2019 = 4.5
	selic_2020 = 2.0
	market_idx_reference = selic_2019 + selic_2020 / 2

	for file in files:
		original_file = _dir + file
		if not isfile(original_file) or 'DS_Store' in file:
			continue

		file_handler = open(original_file, 'rb')
		data = pickle.load(file_handler)
		file_handler.close()

		# less than two years
		data['less_than_2_yrs'] = False
		if data['timeframe']['last_24_months']['profitability'] is None:
			data['less_than_2_yrs'] = True
			modification_file: str = _dir + file
			handler = open(modification_file, 'wb')
			pickle.dump(data, handler)
			handler.close()
			continue

		accumulated_profitability = data['timeframe']['last_24_months']['profitability']
		yearly_volatility = data['timeframe']['last_24_months']['volatility']

		sharpe = (accumulated_profitability - market_idx_reference) / yearly_volatility
		data['timeframe']['last_24_months']['sharpe_ratio'] = sharpe

		modification_file: str = _dir + file
		handler = open(modification_file, 'wb')
		pickle.dump(data, handler)
		handler.close()
