#  -*- coding: utf-8 -*-
"""
The program needs to produce the result of xnor of 3 values.
To do this, the program uses AND, OR, and NOT functions created using NN.
A random set of wheights, a bias value, and number of times for the nn training will be generated or stated in the beginnig.

OR, AND, and NOT functions' Process:
    - Recieves inputs, creating another set of wheights for it's own use,
    - then starts the training process using the _Think functions (which recives inputs and an expected output):
        - Use sigmoid function to compute the output of the NN, based on the weights (the activation function).
        - Compute the back propagated error rate: 
            -Compute the difference between the predicted output and the expected output recivied. 
        - Based on the value of the error rate, perform minor weight adjustments using the sigmoid derivative formula.
        - Iterate this process the number of times stated.
    - After the wheights had been refined by the training, uses them to compute the final result.
    * The final result is close to 0 or close to 1 because use sigmoid activation function.


THE PROGRAM DOESN'T USES CLASSES.


Signs appendix:
    + => OR
    . => AND
    ⊕ => XOR
    ⊙ => XNOR
    
    
Examples for checking: 
    A    |    B    |    C    |  OUTPUT (A ⊙ B ⊙ C) 
===========================================
    0    |    0    |    0    |    1
    0    |    0    |    1    |    0
    0    |    1    |    0    |    0
    0    |    1    |    1    |    1
    1    |    0    |    0    |    0
    1    |    0    |    1    |    1
    1    |    1    |    0    |    1
    1    |    1    |    1    |    0
    
    
    
@author: Yehonatan Tal       
"""

import random
import numpy as np

bias = 1 #  value of bias
weights = [random.random(),random.random(),random.random()] # weights generated in a list (3 weights in total for 2 neurons and the bias)
times = 1500 # number of times the training will occur


def main():
    #for j in range(8):
        i1,i2,i3 = int(input("enter first value    ")), int(input("enter second value    ")), int(input("enter third value    ")) # three inputs
        XNOR(i1,i2,i3) # xnor of three values
    
    
def XNOR(i1,i2,i3):
    # xnor of three values using the formula: A ⊙ B ⊙ C = (A ⊙ B) ⊕ C
    r = XOR(XNOR2(i1,i2),i3)
    print( "\n{} xnor {} xnor {} is : {} ".format(i1,i2,i3,r),"\n")
    
    
def XNOR2(i1,i2):
    # xnor of two values using the formula: A ⊙ B = A.B + A̅.B̅
    r = OR(AND(i1,i2),AND(NOT(i1),NOT(i2)))
    #print( "\n{} xnor {} is : {} ".format(i1,i2, r,"\n")
    return r

    
def XOR(i1,i2):
    # xor of two values using the formula: A ⊕ B = A.B̅ + A̅.B
    r = OR(AND(i1,NOT(i2)),AND(NOT(i1),i2))
    #print( "\n{} xor {} is : {} ".format(i1,i2, r),"\n")
    return r

   
    
def AND(i1,i2):
    global ANDweights # another set of wheights which will be used for the AND training
    ANDweights = weights 
    for i in range(times): 
        #do the training with 4 suitable examples
        AND_Think(1,1, 1) # True and true
        AND_Think(1,0, 0) # True and false
        AND_Think(0,1, 0) # False and true
        AND_Think(0,0, 0) # False and false
        
    r = sigmoid(i1*ANDweights[0] + i2*ANDweights[1] + bias*ANDweights[2]) # passing the inputs via the neuron to get the output result
    #print( "\n{} and {} is : {} ".format(i1,i2, r),"\n")
    return r
    


def AND_Think(i1, i2, expected_output):
    # train the AND model to make accurate predictions while adjusting the weights
    
    output = sigmoid(i1*ANDweights[0] + i2*ANDweights[1] + bias*ANDweights[2]) # passing the inputs via the current neuron to get an output
   
    error = expected_output - output
    ANDweights[0] += error * i1 * sigmoid_derivative(output)
    ANDweights[1] += error * i2 * sigmoid_derivative(output)
    ANDweights[2] += error * bias * sigmoid_derivative(output)
    
    
   
def OR(i1,i2):
    global ORweights # another set of wheights which will be used for the OR training
    ORweights = weights 
    for i in range(times):
        #do the training with 4 suitable examples
        OR_Think(1,1, 1) # True or true
        OR_Think(1,0, 1) # True or false
        OR_Think(0,1, 1) # False or true
        OR_Think(0,0, 0) # False or false
        
    r = sigmoid(i1*ORweights[0] + i2*ORweights[1] + bias*ORweights[2]) # passing the inputs via the neuron to get the output result
    #print( "\n{} or {} is : {} ".format(i1,i2, r),"\n")
    return r


def OR_Think(i1, i2, expected_output):
    # train the OR model to make accurate predictions while adjusting the weights
    
    output = sigmoid(i1*ORweights[0] + i2*ORweights[1] + bias*ORweights[2]) # passing the inputs via the current neuron to get an output
   
    error = expected_output - output
    ORweights[0] += error * i1 * sigmoid_derivative(output)
    ORweights[1] += error * i2 * sigmoid_derivative(output)
    ORweights[2] += error * bias * sigmoid_derivative(output)



def NOT(i1):
    global NOTweights # another set of wheights which will be used for the NOT training
    NOTweights = weights[:-1]
    for i in range(times):
        #do the training with 4 suitable examples
        NOT_Think(1, 0)
        NOT_Think(0, 1)
        
    r = sigmoid(i1*NOTweights[0] + bias*NOTweights[1]) # passing the inputs via the neuron to get the output result
    #print( "\n not {} is : {} ".format(i1, r),"\n")
    return r


def NOT_Think(i1, expected_output):
    # train the NOT model to make accurate predictions while adjusting the weights
    
    output = sigmoid(i1*NOTweights[0] + bias*NOTweights[1]) # passing the inputs via the current neuron to get an output
     
    error = expected_output - output
    NOTweights[0] += error * i1 
    NOTweights[1] += error * bias 
   


def sigmoid(x):
    # use sigmoid function
    return 1 / (1 + np.exp(-x))
        

def sigmoid_derivative(x):
    # return derivative of sigmoid function
    return x * (1 - x)


if __name__ == '__main__':
    main()