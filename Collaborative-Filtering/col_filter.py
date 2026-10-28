import numpy as np
import tensorflow as tf
from tensorflow import keras
from recsys_utils import *

######### cofi_cost_func

def cofi_cost_func(X, W, b, Y, R, lambda_):
    """
    Returns the cost for the content-based filtering
    Args:
      X (ndarray (num_movies,num_features)): matrix of item features
      W (ndarray (num_users,num_features)) : matrix of user parameters
      b (ndarray (1, num_users)            : vector of user parameters
      Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
      R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
      lambda_ (float): regularization parameter
    Returns:
      J (float) : Cost
    """
    nm, nu = Y.shape
    J = 0

    nf = X.shape[1]

    for idx_m in range(0,nm):
        
        for idx_n in range(0,nu):
            
            if R[idx_m,idx_n] == 1:

                wx = 0
                for idx_f in range(0,nf):

                    wx = wx + (W[idx_n,idx_f]*X[idx_m,idx_f])

                J = J + (wx + b[0,idx_n] - Y[idx_m,idx_n])**2

    reg_m = 0
    reg_n = 0   

    for idx_n in range(0,nu):
        for idx_f in range(0,nf):
            reg_n = reg_n + (W[idx_n,idx_f])**2

    for idx_m in range(0,nm):
        for idx_f in range(0,nf):
            reg_m = reg_m + (X[idx_m,idx_f])**2    
    
    J = J / 2 + lambda_/2*reg_n + lambda_/2*reg_m 

    return J


######### MAIN

#Load data
X, W, b, num_movies, num_features, num_users = load_precalc_params_small()
Y, R = load_ratings_small()

print("Y", Y.shape, "R", R.shape)
print("X", X.shape)
print("W", W.shape)
print("b", b.shape)
print("num_features", num_features)
print("num_movies",   num_movies)
print("num_users",    num_users)

#  From the matrix, we can compute statistics like average rating.
tsmean =  np.mean(Y[0, R[0, :].astype(bool)])
print(f"Average rating for movie 1 : {tsmean:0.3f} / 5" )

# Reduce the data set size so that this runs faster
num_users_r = 4
num_movies_r = 5 
num_features_r = 3

X_r = X[:num_movies_r, :num_features_r]
W_r = W[:num_users_r,  :num_features_r]
b_r = b[0, :num_users_r].reshape(1,-1)
Y_r = Y[:num_movies_r, :num_users_r]
R_r = R[:num_movies_r, :num_users_r]

# Evaluate cost function
J = cofi_cost_func(X_r, W_r, b_r, Y_r, R_r, 0);
print(f"Cost: {J:0.2f}")

# Evaluate cost function with regularization 
J = cofi_cost_func(X_r, W_r, b_r, Y_r, R_r, 1.5);
print(f"Cost (with regularization): {J:0.2f}")