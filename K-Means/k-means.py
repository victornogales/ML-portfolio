import numpy as np
#from utils import *



######## load_data

def load_data():
    X = np.load("ex7_X.npy")
    return X

######## find_closest_centroids

def find_closest_centroids(X, centroids):
    """
    Computes the centroid memberships for every example
    
    Args:
        X (ndarray): (m, n) Input values      
        centroids (ndarray): (K, n) centroids
    
    Returns:
        idx (array_like): (m,) closest centroids
    
    """

    # Set K
    K = centroids.shape[0]

    # You need to return the following variables correctly
    idx = np.zeros(X.shape[0], dtype=int)
    
    # loop the samples
    for m in range(0,X.shape[0]):

        # loop the centroids
        min_norm = 0;
        min_idx = -1;
        for c in range(0,K):
            norm = np.sqrt((centroids[c,0]-X[m,0])**2+((centroids[c,1]-X[m,1])**2))
            if (min_idx == -1) or (norm < min_norm):
                min_norm = norm
                min_idx = c
        
        idx[m] = min_idx
    
    return idx

######## compute_centroids

def compute_centroids(X, idx, K):
    """
    Returns the new centroids by computing the means of the 
    data points assigned to each centroid.
    
    Args:
        X (ndarray):   (m, n) Data points
        idx (ndarray): (m,) Array containing index of closest centroid for each 
                       example in X. Concretely, idx[i] contains the index of 
                       the centroid closest to example i
        K (int):       number of centroids
    
    Returns:
        centroids (ndarray): (K, n) New centroids computed
    """
    
    # Useful variables
    m, n = X.shape
    
    # You need to return the following variables correctly
    centroids = np.zeros((K, n))
    
    ### START CODE HERE ###
    
    count = np.zeros(K)

    for sample_id in range(0,m):

            print("sample_id: ",sample_id)
            centroids[idx[sample_id],0] += X[sample_id,0]
            centroids[idx[sample_id],1] += X[sample_id,1]
            count[idx[sample_id]] += 1

    for num_centroids in range(0,K):
        centroids[num_centroids,0] = centroids[num_centroids,0] / count[num_centroids]        
        centroids[num_centroids,1] = centroids[num_centroids,1] / count[num_centroids]  
    
    return centroids

######## MAIN


# Load an example dataset that we will be using
X = load_data()

print("First five elements of X are:\n", X[:5]) 
print('The shape of X is:', X.shape)

# Select an initial set of centroids (3 Centroids)
initial_centroids = np.array([[3,3], [6,2], [8,5]])

# Find closest centroids using initial_centroids
idx = find_closest_centroids(X, initial_centroids)

# Print closest centroids for the first three elements
print("First three elements in idx are:", idx[:3])

from public_tests import *

#find_closest_centroids_test(find_closest_centroids)

K = 3
centroids = compute_centroids(X, idx, K)

print("The centroids are:", centroids)

compute_centroids_test(compute_centroids)