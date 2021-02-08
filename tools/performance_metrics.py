# performance_metrics.py

import numpy as np
import pandas as pd

test = np.array([[7,8,9],[1,2,3],[3,2,1]])

# Function that computes a confusion matrix which is used to compute the below functions
def cm_maker(y, ypred, n_classes):
    
    low = [1, 2, 3]
    high = [5, 6, 7]
    cm = np.zeros((n_classes, n_classes))
    
    for i, j in zip(ypred, y):
        
        if i in low:
            i = i - 1
        if i in high:
            i = i - 2
            
        if j in low:
            j = j - 1
        if j in high:
            j = j - 2
            
        cm[int(i), int(j)] += 1
        
    return cm



def LOO_confusion_matrix(guess:int, label: int, size: int) -> np.array:
    cm = np.zeros((size,size))

    if guess <= 3:
        guess -= 1
    else:
        guess -= 2

    if label <= 3:
        label -= 1
    else:
        label -= 2

    cm[guess,label] = 1

    return cm



# precision for multi-classification
def precision(confusion_matrix: np.array) -> list:
    out = []
    n_classes = len(confusion_matrix)
    for i in range(n_classes):
        denominator = sum(confusion_matrix[i,:])
        if denominator == 0:
            out.append(0)
        else:
            out.append(confusion_matrix[i,i]/denominator)
    return out



# recall for multi-classification
def recall(confusion_matrix: np.array) -> list:
    out = []
    n_classes = len(confusion_matrix)
    for i in range(n_classes):
        denominator = sum(confusion_matrix[:,i])
        if denominator == 0:
            out.append(0)
        else:
            out.append(confusion_matrix[i,i]/denominator)
    return out



# f1-score for multi-classification
def f1_score(confusion_matrix: np.array) -> list:
    precision_scores = precision(confusion_matrix)
    recall_scores = recall(confusion_matrix) 
    out = []
    n_classes = len(confusion_matrix)
    for i in range(n_classes):
        out.append(2*(precision_scores[i]*recall_scores[i])/(precision_scores[i]+recall_scores[i]))
    return out