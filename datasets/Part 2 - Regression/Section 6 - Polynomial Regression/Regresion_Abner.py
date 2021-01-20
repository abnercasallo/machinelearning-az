# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:03:47 2020

@author: abner
"""
import os
import numpy as np     #arrays
import matplotlib.pyplot as plt    #visualizacióm
import pandas as pd              #datos

os.chdir('D:/Git Hub-BEST/machinelearning-az/datasets/Part 2 - Regression/Section 6 - Polynomial Regression')

'''Limpieza'''

dataset = pd.read_csv('Position_Salaries.csv')
#print(dataset["Level"])
#type(dataset["Level"])
#Separamos X e Y, no olvidar el .values para q salga como array, sino quedará como dataframe
X=dataset.iloc[:,1:2].values   #OJO,  1 es diferente a 1:2 en Python. En un caso es vector o lista, en el segundo es matriz. Queremos matriz.
Y=dataset.iloc[:,2].values


#Separamos data de entrenamiento y de testeo
from sklearn.model_selection import train_test_split  #función para dividir datasets
#Elegimos un nivel de testeo del 0.2, un random_stat=0, para reproducir la randomización
#cada vez que alguien ponga random_stat=0, el resultado se mantendrá

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


#EL PAQUETE YA ESCALA LAS VARIABLES, NOS PASAMOS ESTA ETAPA DEL PRE PROCESAMIENTO

###1. CONSTRUIMOS UNA REGRESIÓN LINEAL CON Sklearn
from sklearn.linear_model import LinearRegression
#lin_reg = LinearRegression()
lin_reg=LinearRegression()
lin_reg.fit(X_train, Y_train) #Fit es un método usado para LinearRegression

# Visualización de los resultados del Modelo Lineal
plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_train, lin_reg.predict(X_train), color = "blue")
plt.title("Modelo de Regresión Lineal")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

###2. CONSTRUIMOS UNA REGRESIÓN POLINÓMICA (ojo: es lineal, o sea lineal en los coeficientes) CON sklearn
from sklearn.preprocessing import PolynomialFeatures

#Polinomia es esencial crea una variable con una función a la 4. Paso esencial
X_poly_train = PolynomialFeatures(degree = 5).fit_transform(X_train)           #Botará la columna de indepenientes automáticamente
lin_reg_2 = LinearRegression().fit(X_poly_train, Y_train)
#PolynomialFeatures da matriz de términos independientes, las X y las X al exponente


# Visualización de los resultados del Modelo Polinómico
plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_train, lin_reg_2.predict(X_poly_train), color = "blue")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

#EL GRÁFICO QUEDA HORRIBLE PORQUE TIENE VALORES DISCRETOS, DEBEMOS SUAVIZARLO
#Usarmos arrange de numpy para dicho fin
X_grid_train = np.arange(min(X_train), max(X_train), 0.1) #deben ser arrays, por eso es importante usar value al sacar a las X e Y al inicio
X_grid_train = X_grid_train.reshape(len(X_grid_train), 1)
X_poly_grid_train = PolynomialFeatures(degree = 5).fit_transform(X_grid_train)   
#El gri lleva el modelo a términos infinitesimales, sino queda feo la gráfica

plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_grid_train, lin_reg_2.predict(X_poly_grid_train), color = "green")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

#Una visión de ambos casos: suavizado y sin suavizar:
plt.scatter(X_train, Y_train, color = "red")
plt.plot(X_train, lin_reg_2.predict(X_poly_train), color = "blue")
plt.plot(X_grid_train, lin_reg_2.predict(X_poly_grid_train), color = "green")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()


lin_reg.predict([[6.5]])
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


####USAMOS LA DATA DE TESTEO:
X_poly_test = PolynomialFeatures(degree = 5).fit_transform(X_test)           #Botará la columna de indepenientes automáticamente

plt.scatter(X_test, Y_test, color = "red")
plt.plot(X_grid_train, lin_reg_2.predict(X_poly_grid_train), color = "blue") 
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()

#Analizamos la significancia del modelo por OLS, que sería todo lineal
#La constante y análisis sale raro, por eso mejor trabajarlo como polinomio
import statsmodels.api as sm
X_const = sm.add_constant(X) 
regression_OLS = sm.OLS(endog = Y, exog = X_const.tolist()).fit() #fit: ajusta, trabajamos con X_opt
regression_OLS.summary()

#Trabajando con variable exógena en forma polinómica, PERO TOMA POR SEPARADO LOS GRADOS
X_poly_2= PolynomialFeatures(degree = 3).fit_transform(X) #Botará la columna de indepenientes automáticamente más la x y el cuadrado y así...

#X_poly_const = sm.add_constant(X_poly) No séra necesario en este caso
regression_OLS = sm.OLS(endog = Y, exog = X_poly_2.tolist()).fit() #fit: ajusta, trabajamos con X_opt
regression_OLS.summary()











