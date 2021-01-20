#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:43:11 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np    #Para la mate
import matplotlib.pyplot as plt   # Para la visualización
import pandas as pd     #Para bases de datos

#Haremos un modelo con una Y: Sí/No que depende de varias X
#Ese Sí/No está en la última fila del dataset que vamos a crear exportando Data.csv.
# Importar el data set
dataset = pd.read_csv('Data.csv') #Para evitar not. cient: Doble click en el data set de la variable explorer y poner formato de los números "%.0f"
X = dataset.iloc[:, :-1].values   #Variable independiente, todo menos la columna final, la función iloc: localiza elementos filas y columnas del dataframe (i de index y loc de localization)
y = dataset.iloc[:, 3].values     #Variable dependiente

#En R no es necesario crear ese X e Y, podemos trabajar directamente con el dataset.

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split #Solo importamos una parte (una función) de la librería sklearn
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


'''
# Escalado de variables para evitar que las unidades afecten
#Felizmente R y Python ya lo preprocesan
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

