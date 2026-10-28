import numpy as np
import copy
import math

## Sigmoid 2

def sigmoid2(z):

    # Check whether a single number
    if not isinstance(z, np.ndarray):
        s = 1 / ( 1 + math.exp(-z))
    else:
        # 1-D Array
        s = np.empty_like(z, dtype = float)
        if z.ndim == 1:

            it = 0;
            for x in z:
                e = 1 / ( 1 + math.exp(-x))
                s[it] = e
                it += 1

        # 2-D Matrix
        else:

            for lin in range(0,z.ndim):
                w = z[lin]
                it = 0
                for x in w:
                    e = 1 / ( 1 + math.exp(-x))
                    s[lin,it] = e
                    it += 1 

    return s

###############################################################################
#    PREDICT
###############################################################################

def predict(X, w, b): 
    """
    Predict whether the label is 0 or 1 using learned logistic
    regression parameters w
    
    Args:
      X : (ndarray Shape (m,n)) data, m examples by n features
      w : (ndarray Shape (n,))  values of parameters of the model      
      b : (scalar)              value of bias parameter of the model

    Returns:
      p : (ndarray (m,)) The predictions for X using a threshold at 0.5
    """
    # number of training examples
    m = X.shape   
    p = np.zeros(m)
    
    # Calculate Prediction for the model
    line_it = 0
    for row in X: 
        col_it = 0
        sum_e = 0

        for col in row:
            sum_e = sum_e + col * w[col_it]
            col_it += 1
        sum_e = sum_e + b
                
        e = 1 / ( 1 + math.exp(-sum_e))
        
        if (e>=0.5):
            p[line_it] = 1
        else:
            p[line_it] = 0
        line_it += 1 

        
    ### END CODE HERE ### 
    return p

###############################################################################
#    MAIN
###############################################################################

value = 0

print (f"sigmoid2({value}) = {sigmoid2(value)}")

print ("sigmoid2([ -1, 0, 1, 2]) = " + str(sigmoid2(np.array([-1, 0, 1, 2]))))

# UNIT TESTS
from public_tests import *
sigmoid_test(sigmoid2)


###############################################################################
#    MAIN PREDICT
###############################################################################

np.random.seed(1)
tmp_w = np.random.randn(2)
tmp_b = 0.3    
tmp_X = np.random.randn(4, 2) - 0.5

tmp_p = predict(tmp_X, tmp_w, tmp_b)
print(f'Output of predict: shape {tmp_p.shape}, value {tmp_p}')
