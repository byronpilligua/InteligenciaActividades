# -*- coding: utf-8 -*-
"""Actividad2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sgHFvEE-WjmfCxIdzftDwC3ZN0b9rjZt
"""

import pandas as pd
datos = pd.read_csv('/content/musica.csv')
datos

data = (datos[['name','artists','tempo']])
print('Ordenado por artista')
data.sort_values(by= ['artists'],ascending = True)

data = (datos[['name','artists','tempo']])
print('Ordenado por Tiempo')
data.sort_values(by= ['tempo'],ascending = True)