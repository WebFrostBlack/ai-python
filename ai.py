# --------------------------- #
#       ©FROSTBLACK           #
#         WEB DEV             #
# --------------------------- #

from keras import *

model = Sequential()

model.add(layers.Dense(units=3, input_shape=[1]))
model.add(layers.Dense(units=100))
model.add(layers.Dense(units=1))

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
output = [3.5, 7, 10.5, 14, 17.5, 21, 24.5, 28, 31.5, 35, 38.5, 42, 45.5, 49, 52.5, 56, 59.5, 63, 66.5, 70] # Datas for train the ai machine

model.compile(loss='mean_squared_error', optimizer='adam') # Configuring the model to use mean squared error as the loss function and the Adam optimizer for training.
model.fit(x=input, y=output, epochs=10000) # Training the model for 10000 iterations/epochs to optimize its performance.

while True:
    x = int(input('Number : '))
    print('Prediction : ' + str(model.predict([x])))
