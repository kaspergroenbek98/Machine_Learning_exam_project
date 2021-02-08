import numpy as np

def read_data():
    train = np.loadtxt('data/df_train.csv',skiprows=1,delimiter=',')
    test = np.loadtxt('data/df_test.csv',skiprows=1,delimiter=',')
    
    return train, test