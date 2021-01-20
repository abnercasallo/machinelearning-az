# Regresión Lineal Múltiple
setwd("D:/Git Hub-BEST/machinelearning-az/datasets/Part 2 - Regression/Section 5 - Multiple Linear Regression")
# Importar el dataset
dataset = read.csv('50_Startups.csv')
#dataset = dataset[, 2:3]

# Codificar las variables categóricas
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3))



# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de Regresión Lineal Múltiple con el Conjunto de Entrenamiento
regression = lm(formula = Profit ~ .,  #=El punto asume q las otras variables serán las independientes. Se podría escribir ~R.D.Spend + Administration + Marketing.Spend + State...
                data = training_set)   #Prepararemos al modelo con la data de entrenamiento

summary(regression) #Como se ve, automáticamente R automáticamente usa las 2 dummies y no las 3, para evitar la MULTICOLINEALIDAD.
#***=Altamente significativo, entre 0 y 0.001.
#** entre 0.001 y 0.01
#*  entre 0.01 y 0.05.
#. entre 0.05 y 0.1
#   entre 0.1 y 1. P value mayor al 10%

# Predecir los resultados con el conjunto de testing
y_pred = predict(regression, newdata = testing_set)#usamos el modelo de prediccion con la data de test

# Construir un modelo óptimo con la Eliminación hacia atrás
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, #Dejamos de lado el menos significativo
                data = training_set)  #Gomilla prefiere dataset, pero la verdad confunde, mejor seguir la lógica de siempre
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)  #Podría ser con el training, pero como quiero el ajuste de todo, mejor con todos los datos
summary(regression)      #Yo: pero ya no sería un testing más adelante xd, la nueva data también ha tenido efecto en el modelo xd
                        #Entonces mejor el modelo sigo haciendo con la data training y luego probando con el test.

regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend,
                data = dataset)
summary(regression)


#install.packages("https://cran.r-project.org/src/contrib/Archive/ElemStatLearn/ElemStatLearn_2015.6.26.2.tar.gz",repos=NULL, type="source")
#####FUNCIÓN PARA AUTOMATIZAR LA ELIMINACIÓN HACIA ATRÁS:
backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)
