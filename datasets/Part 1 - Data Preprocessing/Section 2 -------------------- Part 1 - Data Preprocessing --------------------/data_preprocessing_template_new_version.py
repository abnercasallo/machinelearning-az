#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:11:34 2020

@author: juangabriel
"""


# Plantilla de Pre Procesado

# Cómo importar las librerias en Python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Importar el Data set
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 3].values 

# Tratamiento de los NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose=0)
imputer = imputer.fit(X[:,1:3]) 
X[:, 1:3] = imputer.transform(X[:,1:3])

# Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],  #para crear una columna del valor 
    remainder='passthrough'                        
)

X = np.array(ct.fit_transform(X), dtype=np.float)
labelencoder_y = LabelEncoder()       #solo label, pues tiene solo dos valores y no se requiere crear columnas con "one_hot_encoder"
y = labelencoder_y.fit_transform(y)


# Dividir el data set en conjunto de entrenamiento y en conjunto de testing
from sklearn.model_selection import train_test_split     #Para dividir
#Trabajaremos con un 20% de testing y 80% para entrenamiento (normalmente el testing no debe pasar del 30%)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 0) #El random es al gusto.
#Si cambiamos el random_state los datos de las divisiones cambiarán (en testing esencialmente).


# Escalado de valores (dado que las x tiene un rango muy superior a las y y eso dificulta el cálculo)
#Pues la Y pasaría inadvertida dado que al ser de mucho menor magnitud no se nota su efecto.
# Escalado de variables
from sklearn.preprocessing import StandardScaler  #La función standardsclaler va a ayudarnos a dar escala
sc_X = StandardScaler()                           #Creamos el esalador
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)                   #No fit_tansform pues queremos la misma escala q el train.

#Las dummies (como en este caso las Y) no necesitan ser normalizadas 
#Debes diferenciar la normalización y estandarización (llevarlo a su Z,T,F,etc., estadístico).
