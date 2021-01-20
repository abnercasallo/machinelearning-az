#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:19:21 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado - Datos faltantes

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv') #Para evitar not. cient: Doble click en el data set de la variable explorer y poner formato de los números "%.0f"
X = dataset.iloc[:, :-1].values   #Variable independiente, todo menos la columna final, la función iloc: localiza elementos filas y columnas del dataframe (i de index y loc de localization)
y = dataset.iloc[:, 3].values     #Variable dependiente

#En R no es necesario crear ese X e Y, podemos trabajar directamente con el dataset.
#Nan: not a number.

# Tratamiento de los NAs, dado que eliminar tiene riesgos, replazaremos por la media
from sklearn.impute import SimpleImputer #Solo importamos una parte (una función) de la librería sklearn
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose=0)  #verboe o axis=0 es por q se aplica a columna, para fila es=1.
#aplicamos a la columna 2 y 3.
imputer = imputer.fit(X[:, 1:3]) #fit es una función que general que referirá a la X
X[:, 1:3] = imputer.transform(X[:,1:3])