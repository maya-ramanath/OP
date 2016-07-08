'''
Created on 5 July 2016

@author: maya
'''

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.grid_search import GridSearchCV
from sklearn.datasets import load_files
from sklearn.pipeline import Pipeline
import numpy as np


def runClassifiers (dataDir):
    
    data = load_files(dataDir)

    nbClassifier = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('classifier', MultinomialNB())])
    
    parameters = {'vect__ngram_range': [(1,1),(2,2),(3,3),(1,2),(1,3)],
                  'vect__binary': [True, False],
                  'tfidf__use_idf': [True, False],
                  'classifier__alpha': [1e-2, 1e-3]}
    
    gs = GridSearchCV(nbClassifier, parameters, n_jobs=-1, verbose=1)
    gs.fit(data.data, data.target)
    best_parameters = gs.best_estimator_.get_params()
    
    print("Best score: %0.3f" % gs.best_score_)
    for params, mean_score, scores in gs.grid_scores_:
        print("%0.3f (+/-%0.03f) for %r"
              % (mean_score, scores.std() * 2, params))
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
    print("Done")
    
    pass

def runNB ():
    X = np.random.randint(5, size=(6, 100))
    y = np.array([1, 2, 3, 4, 5, 6])
    clf = MultinomialNB();
    clf.fit(X, y)
    print(clf.predict(X[2:3]))

if __name__ == '__main__':
    #runNB()
    runClassifiers('/Users/maya/git/OP/Data/Load')