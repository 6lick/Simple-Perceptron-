import random 
import numpy as np
#begin with random weights


def genInputNeurons():
    inputs = []
    for i in range(0,3):
        x = random.randint(0,1)
        inputs.append(x)
    inputs.append(1)
    return inputs


def sigmoid(x):
    y = 1/(1+np.exp(-x))
    return y

def perceptron(weights):
    inputNodes = genInputNeurons()
    if(inputNodes[0] == 1 and inputNodes[2] == 1):
        signal =  1
    else:
        signal = 0
    tmp = np.dot(inputNodes, weights)
    sig = sigmoid(tmp) 
    error = signal - sig
    #correction 
    corr = error * sigmoid(sig)
    weights = weights + np.dot(sig, corr)
    return weights



weights = []
for i in range(0,3):
    x = float("{0:.2f}".format(random.uniform(-1.0, 1.0)))
    weights.append(x)

#weight for d is always -1
weights.append(-1)

for i in range(0, 8000):
    if i % 250 == 0:
        print("Round " + str(i) + "\n", weights)
    weights = perceptron(weights)


