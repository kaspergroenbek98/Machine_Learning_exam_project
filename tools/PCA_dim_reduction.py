import numpy as np

# Implementation of PCA using numpy
def PCA_dim_reduction(train_file, test_file, n_components):
    
    # Read data
    train = np.loadtxt(train_file, skiprows=1, delimiter=",")
    test = np.loadtxt(test_file, skiprows=1, delimiter=",")

    train_x = train[:,:-1]  
    train_y = train[:,-1]

    test_x = test[:,:-1]
    test_y = test[:,-1]
    
    # Standardize data
    mean = np.mean(train_x, axis=0)
    std = np.std(train_x, axis=0)
    
    train_x = (train_x - mean) / std
    test_x = (test_x - mean) / std
    
    # Get covariance matrix
    covmat = np.cov(train_x.T)
    
    # Get eigenvalues
    eigval, eigvec = np.linalg.eig(covmat)
    
    # Get explained variance (if needed)
    exp_var = []
    for i in range(len(eigval)):
        exp_var.append(eigval[i]/np.sum(eigval))
    exp_var = sorted(exp_var, reverse=True)

    # Pair up eigenvalues and vectors, so the vectors can be ranked by values
    eigenpairs = []
    for i in range(len(eigval)):
        eigenpairs.append((eigval[i]/np.sum(eigval), eigvec[:, i].T))
    eigenpairs = sorted(eigenpairs, reverse=True)
    
    # Put in the vectors from most to least important in a list
    sorted_vectors = []
    for i in range(len(eigenpairs)):
        sorted_vectors.append(eigenpairs[i][1])
    
    # Make new variables to store the transformed data (the n principle coponents)
    new_train_x = np.zeros((len(train_x), n_components))
    new_test_x = np.zeros((len(test_x), n_components))
    
    # Transform the data into n principle components on the new subspace
    for i in range(n_components):
        new_train_x[:,i] = train_x @ sorted_vectors[i]
        new_test_x[:,i] = test_x @ sorted_vectors[i]
    
    # Store transformed data (pc's) in old variables
    train_x = new_train_x
    test_x = new_test_x
    
    # Return the transformed train and test data + class labels
    return train_x, train_y, test_x, test_y


def binary_classification_data(train_file, test_file):    
    # Read in the top 5 Principal Components
    train_x, train_y, test_x, test_y = PCA_dim_reduction(train_file, test_file, 5)

    # Divide test and train data into features and class labels
    window = [1,2,3]

    for i in range(len(train_y)):
        if train_y[i] in window:
            train_y[i] = 1
        else:
            train_y[i] = 2

    for i in range(len(test_y)):
        if test_y[i] in window:
            test_y[i] = 1
        else:
            test_y[i] = 2
    
    return train_x, train_y, test_x, test_y