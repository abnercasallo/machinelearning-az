###############################################################
#############Plantilla para el Pre Procesado de Datos##########
###############################################################
#1.IMPORTACIÓN DEL DATA SET
dataset = read.csv('Data.csv')
#dataset = dataset[, 2:3]

#2.CODIFICACIÓN DE VARIABLES CATEGÓRICAS
dataset$Country = factor(dataset$Country,   #El factor no representa un número en sí, sino cateorías
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))     

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0,1))

#3.DIVISIÓN TRAIN Y TEST.
#Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)     #Es la semilla aleatoria, como el "random_state" de Python. Puede ser cualquier número
split = sample.split(dataset$Purchased, SplitRatio = 0.8)  #Ahora elige al grupo train, con valor "TRUE".
training_set = subset(dataset, split == TRUE)              #Elegimos para el grupo train.  
testing_set = subset(dataset, split == FALSE)              #Elegimos para el grupo test.

#4.ESCALADO
#Escalado (normalizando) de valores (dado que las x2 tiene un rango muy superior a las x1 y eso dificulta el cálculo)
#Pues la x1 pasaría inadvertida dado que al ser de mucho menor magnitud no se nota su efecto.
#Las y al ser dummies no es necesario dar el escalado:
#scale solo opera con numéricas, debemos dejar de lado a las columnas con factor.
training_set[,2:3] = scale(training_set[,2:3])   #Para la variable train
testing_set[,2:3] = scale(testing_set[,2:3])     #para la variable test