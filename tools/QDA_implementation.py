import numpy as np

# Function to put the class specific data into designated arrays
def preprocess_QDA(train_x, train_y):
    # Collecting all class labels
    classes = np.unique(train_y)

    # Seperating all class-specific observations onto designated variables and finally collecting them into an array.
    mask = train_y == 1
    class1 = train_x[mask, :]

    mask = train_y == 2
    class2 = train_x[mask, :]

    mask = train_y  == 3
    class3 = train_x[mask, :]

    mask = train_y == 5
    class5 = train_x[mask, :]

    mask = train_y == 6
    class6 = train_x[mask, :]

    mask = train_y == 7
    class7 = train_x[mask, :]
    
    # list of arrays with observations from specific classes
    class_list = [class1, class2, class3, class5, class6, class7]
    
    # Return list with arrays of observations in classes
    return class_list


# Function to get the class parameters: mean, covariance matrix and probability of class
def get_parameters_QDA(class_list, train_x):
    
    # Estimate a mean vector per class
    class_means = np.zeros((len(class_list), train_x.shape[1]))
    for i in range(len(class_list)):
        class_means[i] = class_list[i].mean(axis=0)

    # Estimate a covariance matrix per class
    class_covmats = []
    for i in range(len(class_list)):
        class_covmats.append(np.cov(class_list[i].T))


    # Estimate class probabilities
    class_probs = []
    for i in range(len(class_list)):
        class_probs.append(len(class_list[i]) / len(train_x))
    
    # Return the parameters for each class in designated lists
    return class_means, class_covmats, class_probs


# Discriminant function from slides
# It takes in a specific observation and the parameters of a specific class
def QDA_discriminant_function(x, class_mean, class_covmat, class_prob):
    
    a_k = 2 * np.log(class_prob) - np.log(np.linalg.det(class_covmat)) - class_mean.T @ np.linalg.inv(class_covmat) @ class_mean
    b_k = 2 * class_mean.T @ np.linalg.inv(class_covmat)
    c_k = -np.linalg.inv(class_covmat)
    
    # Returns discriminant function for a specific class on a specific observation
    return a_k + b_k.T @ x + x.T @ c_k @ x


# QDA scoring by finding the class that maximises the dicriminant function for each observation
def QDA_class_scoring(test_x, test_y, class_list, covmat_list, mean_list, prob_list):
    
    classes = np.unique(test_y)
    class_scores = np.zeros((len(test_x), len(class_list)))
    
    for x in range(len(test_x)):
        for k in range(len(class_list)):
            # formula from lectures
            class_scores[x, k] = QDA_discriminant_function(test_x[x,:], mean_list[k], covmat_list[k], prob_list[k])
            
            # formula from sklearn library
            #class_scores[x, k] = log_posterior_sklearn(test_x[x,:], mean_list[k], covmat_list[k], prob_list[k])
    
    # List of classes that maximises the dicsriminant function for each observation
    class_max = []
    for row in class_scores:
        class_max.append(int(classes[np.argmax(row)]))
    
    # returns list with the class that maximised the discriminant function for each observation
    return class_max
