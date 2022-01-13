#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

from os import listdir
from os.path import isfile
import pickle
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

files = listdir('../data_original/acoes/')

for file in files:
    paper = file
    file = '../data_original/acoes/' + file

    if not isfile(file) or 'DS_Store' in file:
        continue

    file_handler = open(file, 'rb')
    data = pickle.load(file_handler)
    file_handler.close()

    keys = list(data['prices'].keys())
    keys.reverse()

    moving_average_values = []
    close_values = []

    for key in keys:
        value = data['prices'][key]

        if 'moving_average' not in value:
            moving_average_values.append(value['close'])
            close_values.append(value['close'] + 0.25)
            continue

        moving_average_values.append(value['moving_average'])
        close_values.append(value['close'])

    # Estacionariedade: propriedades estatísticas não mudam ao longo do tempo Exemplo: média, variância, autocorrelação
    #
    # Ruido: tem uma média constante, uma variância constante e não há estrutura de autocorrelação
    #
    # Autocorrelação (ADF) é um cálculo da correlação das observações da série temporal com valores da mesma série, mas em tempos anteriores. Os períodos anteriores são chamados de lags.
    #
    stationary = adfuller(close_values)
    if stationary[0] < -5:
        print('Ação Estacionária', ' p-value:', stationary[1], ' test result:', stationary[0])
    else:
        print('Ação Não Estacionária', ' p-value:', stationary[1], ' test result:', stationary[0])

    mean = np.mean(close_values)

    fig, graph = plt.subplots()
    graph.plot(keys, moving_average_values)
    graph.plot(keys, close_values)
    graph.plot(keys, [mean for x in range(0, len(close_values))])

    graph.plot(keys, [mean+mean/20 for x in range(0, len(close_values))])
    graph.plot(keys, [mean-mean/20 for x in range(0, len(close_values))])

    graph.set_xticks(keys[::15])
    graph.set_xticklabels(keys[::15], rotation=45)
    graph.set_title(paper.upper() + ' ' + keys[0] + ' ' + keys[len(keys)-1])
    plt.show()
    exit(0)

# Padrão sazonal existe quando uma série é influenciada por fatores sazonais
# (ex.: trimestre do ano) e representa um período fixo e conhecido.
# Consequentemente, as séries temporais sazonais às vezes são chamadas de séries
# temporais periódicas.
# Padrão cíclico existe quando os dados exibem subidas e descidas que não são
# de período fixo. A duração dessas flutuações é geralmente de pelo menos 2 anos.
# Se as flutuações não são de período fixo, são cíclicas; se o período for
# imutável e associado a algum aspecto do calendário, o padrão é sazonal.
# Em geral, a duração média dos ciclos é maior do que a duração de um padrão
# sazonal.

# Teste Ljung–Box: determina se algum grupo de autocorrelações de uma série
# temporal é diferente de zero. Em outras palavras, avaliar se as séries de
# observações ao longo do tempo é aleatória e independente.