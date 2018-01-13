# http://scikit-learn.org/stable/tutorial/basic/tutorial.html#model-persistence

from sklearn import svm
from sklearn import datasets

clf = svm.SVC()

iris = datasets.load_iris()
print iris

X, y = iris.data, iris.target
clf.fit(X, y)


import pickle
s = pickle.dumps(clf)
print s

clf2 = pickle.loads(s)
clf2.predict(X[0:1])

print y[0]