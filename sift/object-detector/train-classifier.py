# Import the required modules
from skimage.feature import local_binary_pattern
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.externals import joblib
import argparse as ap
import glob
import os
from config import *
import numpy as np
import cPickle as pickle
from sklearn import cross_validation, metrics

def getstat(labels, predictions):
	print(   "Accuracy = ", metrics.accuracy_score(labels, predictions),"Precision = ", metrics.precision_score(labels, predictions, pos_label = None, average = 'macro'),"Recall = " ,metrics.recall_score(labels, predictions, pos_label = None, average = 'macro'),"F1 score = " ,metrics.f1_score(labels, predictions, pos_label = None, average = 'macro'))

if __name__ == "__main__":
	X = pickle.load(open('../data/features/feat.p', 'rb'))
	y = pickle.load(open('../data/features/labels.p', 'rb'))
	# print y

	clf = OneVsRestClassifier(LinearSVC(random_state = 0))
	print "Training a Linear SVM Classifier"
	predicted = cross_validation.cross_val_predict(clf, X, y, cv=5, n_jobs = -1)
	getstat(y,predicted)
	# clf.fit(X,y)
	# # If feature directories don't exist, create them
	pickle.dump(clf, open(model_path, 'wb'))
	print "Classifier saved to {}".format(model_path)
