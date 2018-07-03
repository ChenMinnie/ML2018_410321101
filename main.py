
# coding: utf-8

# In[1]:


from sklearn.datasets import fetch_mldata
import numpy as np #import numpy package
import matplotlib.pyplot as plt #plotting packagescdewq`C
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn import decomposition
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

mnist = fetch_mldata('MNIST original') # Downloading Dataset
mnist.data = mnist.data / 255.0  # Normalization 


# In[3]:


pca = PCA(n_components= 30,copy = False)
X = pca.fit_transform(mnist.data)
Y = mnist.target
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= 0.25, random_state=27)

#Reducing Dimension


# In[4]:


lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit_transform(X, Y)
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= 0.25, random_state=27)

#Reducing Dimension


# In[2]:


#svd = decomposition.TruncatedSVD(n_components= 30, algorithm='arpack')
#X = svd.fit_transform(mnist.data)
#Y = mnist.target
#x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size= 0.25, random_state=27)

#Reducing Dimension


# In[5]:


Log_clf = LogisticRegression()
Log_clf.fit(x_train, y_train)
#print('Score:%f'% Log_clf.score(x_test, y_test))
y_pred = Log_clf.predict(x_test)
print('Logistic Classifier Accuracy:%f'% accuracy_score(y_test, y_pred))

# Classifier and Training, Evaluating


# In[6]:


Tree_clf = DecisionTreeClassifier()
Tree_clf.fit(x_train, y_train)
y_pred = Tree_clf.predict(x_test)
print('DecisionTreeClassifier Accuracy:%f'% accuracy_score(y_test, y_pred))

# Classifier and Training, Evaluating


# In[7]:


svm_clf = svm.SVC()
svm_clf.fit(x_train, y_train)
y_pred = svm_clf.predict(x_test)
print('SVC Accuracy:%f'% accuracy_score(y_test, y_pred))

# Classifier and Training, Evaluating


# In[8]:


mlp_clf = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=20, alpha=0.0001,
                     solver='sgd', verbose=10,  random_state=0,tol=0.000000001,learning_rate_init=.1)
mlp_clf.fit(x_train, y_train)
y_pred = mlp_clf.predict(x_test)
print('MLP Classifier Accuracy:%f'% accuracy_score(y_test, y_pred))

# Classifier and Training, Evaluating

