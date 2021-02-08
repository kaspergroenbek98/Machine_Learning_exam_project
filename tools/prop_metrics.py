import numpy as np

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


# Function computes precision score
def preci(cm, c):
    
    if sum(cm[c,:]) == 0:
        return 0
    else:
        return cm[c,c]/sum(cm[c,:])


# Function computes recall score
def recall(cm, c):
    
    return cm[c,c]/sum(cm[:,c])


# Function computes f1-score
def f1(cm, c):
    if (preci(cm,c) + recall(cm,c)) == 0:
        return 0
    else: 
        return 2 * (preci(cm,c) * recall(cm,c)) / (preci(cm,c) + recall(cm,c))
    

# Function computes weighted f1-score
def weighted_f1(cm, n_classes):
    co_su=cm.sum(axis=0)
    n=cm.sum()
    
    weighted_f1_sum = 0
    
    for c in range(n_classes):
        if co_su[c] != 0:
            weighted_f1_sum += f1(cm, c) * co_su[c] / n

    return round(weighted_f1_sum, 3)
        

# Function computes macro f1-score
def macro_f1(cm, n_classes):
    
    f1_sum = 0
    
    for i in range(n_classes):
        f1_sum += f1(cm, i)
    
    return round(f1_sum / n_classes, 3)


# Function to get accuracy
def accuracy(test_y, ypred):
    
    # Count of times where true labels equal predictions
    true_positives = 0
    for i in range(len(test_y)):
        if test_y[i] == ypred[i]:
            true_positives += 1
    
    return true_positives / len(test_y)


# Combines functions above for a coherent performance report
def performance_report(test_y, ypred, n_classes):
    
    class_labels = [1, 2, 3, 5, 6, 7]
    cm = cm_maker(test_y, ypred, n_classes)
    
    print('\nConfusion matrix for prediction:\n', cm)
    print('\n\nAccuracy for prediction:\n', accuracy(test_y, ypred))
    
    print('\n\nMetrics for classes')
    print('_______________________________________________________________________________')
    print('Class\t|\tPrecision\t|\tRecall\t\t|\tF1 Score')
    print('_______________________________________________________________________________')
    
    for i in range(n_classes):
        
        print('\nClass', class_labels[i],'|\t',round(preci(cm, i), 3),'\t\t|\t',round(recall(cm, i), 3),'\t\t|\t',round(f1(cm, i), 3))
    
    print('\n\nWeighted F1 score:\n', weighted_f1(cm, n_classes))
    print('\nMacro F1 score:\n', macro_f1(cm, n_classes))