#---------------------------------------------------------------------#
# Single-layer Perceptron neural network model learning a OR function
# Author: Artur Amaral
# Initial Date: 26/02/2021
#---------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------
# Model:
# 
# 1 neuron -> It's activation represents the output of the logic function
# 3 inputs, being:
#   - 2 normal inputs -> Logical function inputs
#   - 1 bias input -> Allow the network to differentiate outputs of
#                     different neurons in the case that the input vector is full of zeros
# neuron activation function: 
# If neuron receives a non-negative value, it fires.
#-----------------------------------------------------------------------------------------

#----------------------------------------------------
# Initializing the weights with small random values
#----------------------------------------------------

w = [0.05,-0.02,0.02]

#----------------------------------------------------
# Initializing the input set
#----------------------------------------------------

x = [ [-1,0,0],
      [-1,0,1],
      [-1,1,0],
      [-1,1,1] ]

#----------------------------------------------------
# Initializing the target set and the output variable
#----------------------------------------------------

t = [ 0,
      1,
      1,
      1 ]

y = 0

learningRate = 0.25
numberOfIteractions = 10

for i in range(numberOfIteractions):

    #print("###############")
    #print("Iteraction ", end='')
    #print(i)

    for inputVectorCount in range( len(x) ):

        #print("\tinputVectorCount ", end='')
        #print(inputVectorCount)
        
        neuronValue = 0

        for featureCount in range( len(x[0]) ):

            #print("\t\tFeatureCount ", end='')
            #print(featureCount)
    
            neuronValue += x[inputVectorCount][featureCount]*w[featureCount]     

        if neuronValue >= 0:
            y = 1
        else:
            y = 0
        
        error = y - t[inputVectorCount]
        
#----------------------------------------------------
# Correcting the weigth wuth the learning rule
#----------------------------------------------------

        for weightCount in range( len(w) ):
            w[weightCount] -= learningRate*error*x[inputVectorCount][weightCount]

#----------------------------------------------------
# Printing the calibrated weights
#----------------------------------------------------

print("Network trained!")
print("The weight values are:")
print("w0 = ", end = "")
print(w[0])
print("w1 = ", end = "")
print(w[1])
print("w2 = ", end = "")
print(w[2], end = "\n\n")

print("Recall:", end = "\n")


#--------------------------------------------------------
# Recall: Compute the output with the calculated weigths
#--------------------------------------------------------

for inputVectorCount in range( len(x) ):

    neuronValue = 0

    for featureCount in range( len(x[0]) ):
    
        neuronValue += x[inputVectorCount][featureCount]*w[featureCount]     
    
    print(x[inputVectorCount][1], end = "")
    print(" OR ", end = "")
    print(x[inputVectorCount][2], end = "")
    print(" = ", end = "")
    
    if neuronValue >= 0:
        y = 1
    else:
        y = 0

    print(y, end = "\n")
