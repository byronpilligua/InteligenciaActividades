# -*- coding: utf-8 -*-
"""Actividad4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PW_hLrSo-CUWQ02QgQPvUBd3fSG1-Kr4

Predicción de Diabetes con regresión logística

Pasos de este estudio

    Carga de datos
    Desarrollo

1. Carga de datos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('/content/diabetes2.xls')

train.head(3)

"""Variables de interes:

    BMI: índice de masa corporal. Es una métrica o KPI basada en el peso y la altura de cada persona. Un BMI muy alto puede ser indicativo de tener diabetes
    Outcome: si la persona tiene diabetes o no

2. Desarrollo

En esta parte nos interesa explorar los datos y explicar el modelo de regresión logística a este caso de diabetes
2.1 Exploración de datos

Miramos una tabla y una gráfica de los datos que nos interesan
"""

train[['BMI','Outcome']].head()

train[['BMI','Outcome']].plot.scatter(x='BMI',y='Outcome')

"""
2.2 Función logística

Vamos a pintar una función logistica sobre estos 
datos

![imagen.png](data:image/png;base64,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)

Vamos a variar *w,b* a ver que pasa en los datos"""

# pruebas de parametro
w = 0.09
b = -3.6

# despues de hacer el modelos (se explica más adelante)
# intercepto (b): [-3.68596089]
# pendiente (w): [[0.09351691]]

# puntos de la recta
x = np.linspace(0,train['BMI'].max(),100)
y = 1/(1+np.exp(-(w*x+b)))

# grafica de la recta
train.plot.scatter(x='BMI',y='Outcome')
plt.plot(x, y, '-r')
plt.ylim(0,train['Outcome'].max()*1.1)
# plt.grid()
plt.show()

"""
2.3 Optimización de parámetros

Si escogemos esos parametros *w,b* para el modelo, ¿Qué tan buenos son?

Podemos utilizar la siguiente estrategia:

    calcular el valor de la función logística para cada dato
    calcular la función de pérdida (se denota con L o loss)
    calcular el promedio de la pérdida para obtener el costo (se denota con Jo cost)

Queremos los valores *w,b* que resulten en un menor costo

Las ecuaciones para las funciones son

![imagen.png](data:image/png;base64,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)"""

# calculo de las predicciones
train['sigmoid'] = 1/(1+np.exp(-(train['BMI']*w+b)))

# calculo de la funcion de error
train['loss_xi'] = -train['Outcome']*np.log(train['sigmoid'])-(1-train['Outcome'])*np.log(1-train['sigmoid'])
cost_j = train['loss_xi'].mean()
cost_j

"""Esto lo hemos hecho con los parametros que hemos obtenido a ojo por ciento. Ahora vamos a ser más refinados y calcularlo para muchos parametros a la vez y luego de ahi mirar el que tenga menor costo.

Para eso hacemos lo siguiente:

* Construimos un dataframe con valores para *w,b* que varían sobre una cuadricula o grid

* Creamos una función de python que calcule el costo *j* dados parametros *w,b*

* Aplicamos la función sobre el dataframe con los valores *w,b* en la cuadricula

* Podemos ordenar la tabla resultante para obtener los valores *w,b* con el menor costo
* Luego hacemos gráficas para verificar el resultado
"""

# hacemos dataframe para calcular el error en funcion de los parametros w, b

array = np.mgrid[0.05:0.15:0.01, -4:-3:0.01].reshape(2,-1).T
df = pd.DataFrame(data = array, 
                  columns = ['w','b'])

# round para solventar problema con muchos decimales
df['w'] = np.round(df['w'], 6)
df['b'] = np.round(df['b'], 6)

df

def sum_error_df(df):
    train['sigmoid'] = 1/(1+np.exp(-(train['BMI']*df['w']+df['b'])))
    train['loss_xi'] = -train['Outcome']*np.log(train['sigmoid'])-(1-train['Outcome'])*np.log(1-train['sigmoid'])
    j_cost = train['loss_xi'].mean()
    return(j_cost)

df['error'] = df.apply(sum_error_df, axis=1)

df.sort_values(by=['error']).head()

df_3d = df.pivot(index='w', columns='b', values='error')

df_3d.head()

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = df_3d.columns
y = df_3d.index
X,Y = np.meshgrid(x,y)
Z = df_3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

x = df_3d.columns
y = df_3d.index
X,Y = np.meshgrid(x,y)
Z = df_3d
plt.contourf(Y, X, Z, alpha=0.7, cmap=plt.cm.jet)