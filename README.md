# Machine Learning project on a Forensic analysis by classification of glass fragments by their chemical composition
Exam project in a 15 ECTS Machine Learning course. **The final report is in a PDF in the repository**

The project studies forensic analysis of glass fragments using various machine learning classification methods, whereas the following are included:
- Quadratic Discriminant Analysis classifier / self-implemented (A generative method that uses class covariance matrices, means and prior probabilities to determine class membership)
- Decision Tree classifier / self-implemented (A discriminative method that uses various split on features to model the decision boundaries of classes)
- Support Vector Machines classifier (Also a discriminative method that models boundaries by maximizing the margin between classes)
- K-Nearest Neighbors classifier (Another discriminative method that predicts class membership by the conditional probability of the obsercations belonging to a class)
- Soft Voting Classifier (An ensemble of models that classsify new observations by predicting the class of the highest combined probability across all models in the ensemble)

The data in the project consists of a training set (149 observations) and a test set (65 observations) with 6 types of glass (classes), whereas each observation consists of 9 features where each is a material of which the glass fragment consists of (in percent).
The issues with the data, to mention a few, are that it is a very small and imbalanced data set - which makes it harder to train models and to determine if classes a well represented in the observations that we have. Also, some of the classes are clustering together, which makes it hard to seperate, thus classification is troublesome in these cases. Lastly, there is some correlation between features in the data set, which makes especially the Quadratic Discriminant Analysis hard to compute, since the covariance matrices won't be linearly independent, and thus the discriminant function cannot be used for classification, since it does not have an inverse, which is included in the formula (pseudo inverse can be used, however there is a better solution).

To preprocess the data, it was chosen in the project to make a feature selection by using dimentionality reduction methods, thus these two were chosen:
- Principal Component Analysis / self-implemented (An unsupervised method that uses the eigenvectors of the model to transform data into a lower dimension of choice, where the principal components is sorted by the explained variance (numerical significance of the eigenvalues compared to eachother). This method seeks to maximize variability in the given data, without looking at classes.)
- Linear Discriminant Analysis (A supervised method that seeks to maximize class variability by maximizing between-class variablity and minimizing within-class variablity, this is done by computing the scatter matrix of the two and then solving the eigenproblem as mentioned above.)

In this repository you will find all of the methods used in the project, whereas the self-implemented methods have been made solely using numpy and the others are based on scikit-learns implementation of the methods.
