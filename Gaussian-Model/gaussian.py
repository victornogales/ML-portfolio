import numpy as np
from utils import *

######### estimate_gaussian

def estimate_gaussian(X): 
    """
    Calculates mean and variance of all features 
    in the dataset
    
    Args:
        X (ndarray): (m, n) Data matrix
    
    Returns:
        mu (ndarray): (n,) Mean of all features
        var (ndarray): (n,) Variance of all features
    """

    m, n = X.shape
    
    mu = np.zeros(X.shape[1])
    var = np.zeros(X.shape[1])

    # calculate mu

    for m_idx in range(0,m):
        for n_idx in range(0,n):
            mu[n_idx] += X[m_idx,n_idx]

    for n_idx in range(0,n):
        mu[n_idx] = mu[n_idx] / m
        
    # calculate var

    for m_idx in range(0,m):
        for n_idx in range(0,n):
            var[n_idx] += (X[m_idx,n_idx] - mu[n_idx])**2

    for n_idx in range(0,n):
        var[n_idx] = var[n_idx] / m    
        
    return mu, var


######### select_threshold

def select_threshold(y_val, p_val): 
    """
    Finds the best threshold to use for selecting outliers 
    based on the results from a validation set (p_val) 
    and the ground truth (y_val)
    
    Args:
        y_val (ndarray): Ground truth on validation set
        p_val (ndarray): Results on validation set
        
    Returns:
        epsilon (float): Threshold chosen 
        F1 (float):      F1 score by choosing epsilon as threshold
    """ 

    best_epsilon = 0
    best_F1 = 0
    F1 = 0
    
    step_size = (max(p_val) - min(p_val)) / 1000
    
    for epsilon in np.arange(min(p_val), max(p_val), step_size):
        
        tp = 0
        fp = 0
        fn = 0
        tn = 0

        for rec_idx in range(0,y_val.shape[0]):

            if ( ( y_val[rec_idx] == 1 ) and ( p_val[rec_idx] < epsilon ) ): 
                tp += 1
            if ( ( y_val[rec_idx] == 0 ) and ( p_val[rec_idx] < epsilon ) ): 
                fp += 1
            if ( ( y_val[rec_idx] == 1 ) and ( p_val[rec_idx] >= epsilon ) ): 
                fn += 1
            if ( ( y_val[rec_idx] == 0 ) and ( p_val[rec_idx] >= epsilon ) ): 
                tn += 1
       
        if ( ( tp + fp ) == 0):
            prec = 0
        else:
            prec = ( tp / ( tp + fp) )
        if ( ( tp + fn ) == 0 ):
            rec = 0
        else:
            rec  = ( tp / ( tp + fn) )

        if (( prec == 0 ) or ( rec == 0 )):
            F1 = 0
        else:
            F1 = ( 2 * prec * rec ) / ( prec + rec )
        
        if F1 > best_F1:
            best_F1 = F1
            best_epsilon = epsilon
        
    return best_epsilon, best_F1

######### MAIN


# Load the dataset
X_train, X_val, y_val = load_data()

# Display the first five elements of X_train
print("The first 5 elements of X_train are:\n", X_train[:5])  

# Display the first five elements of X_val
print("The first 5 elements of X_val are\n", X_val[:5])  

# Display the first five elements of y_val
print("The first 5 elements of y_val are\n", y_val[:5])  

# Check dimensions
print ('The shape of X_train is:', X_train.shape)
print ('The shape of X_val is:', X_val.shape)
print ('The shape of y_val is: ', y_val.shape)

# Estimate mean and variance of each feature
mu, var = estimate_gaussian(X_train)              

print("Mean of each feature:", mu)
print("Variance of each feature:", var)
    
# Calculate epsilon
p_val = multivariate_gaussian(X_val, mu, var)
print("p_val: ",p_val)
print("y_val: ", y_val)
epsilon, F1 = select_threshold(y_val, p_val)

print('Best epsilon found using cross-validation: %e' % epsilon)
print('Best F1 on Cross Validation Set: %f' % F1)
