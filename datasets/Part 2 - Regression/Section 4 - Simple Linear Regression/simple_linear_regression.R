# Regresión Lineal Simple

# Importar el dataset
dataset = read.csv('Salary_Data.csv')
#dataset = dataset[, 2:3]

# 1. Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores, no es necesario. La librería lo hace
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# 2. Ajustar el modelo de regresión lineal simple con el conjunto de entrenamiento
regressor = lm(formula = Salary ~ YearsExperience, # ~ : En función a. "Salario en función a años de exp.
               data = training_set)

#3. summary(regressor) #Veamos el resultado de la regresión


# 4. Predecir resultados con el conjunto de test
y_pred = predict(regressor, newdata = testing_set)  #Las variables del pred (test) y regressor(train) deben ser del mismo nombre!
y_pred

#5.1. Visualización de los resultados en el conjunto de entrenamiento
#install.packages("ggplot2")
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),#aes: estética, se puede añadir más cosas, ponremos solo ejes 
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience, 
                y = predict(regressor, newdata = training_set)), #Con train para dar el regreson
            colour = "blue") +
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)") +
  xlab("Años de Experiencia") +
  ylab("Sueldo (en $)")

#5.2. Visualización de los resultados en el conjunto de testing
ggplot() + 
  geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary), 
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience,  #el modelo (la recta) es el mismo.
                y = predict(regressor, newdata = training_set)), 
            colour = "blue") +
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Testing)") +
  xlab("Años de Experiencia") +
  ylab("Sueldo (en $)")


