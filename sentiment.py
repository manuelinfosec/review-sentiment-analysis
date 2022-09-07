import csv
import sklearn.neighbors
import sklearn.svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation
from sklearn.metrics import classification_report
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import tree
import scipy
from sklearn.feature_selection import SelectKBest, chi2
import os

os.system('clear') 

print("Enter a String to test: ")
data_test=raw_input()


def load_file():
    with open('review.csv') as csv_file:
        reader = csv.reader(csv_file,delimiter=",",quotechar='"')
        reader.next()
        data =[]
        target = []
        for row in reader:
            # skip missing data
            if row[0] and row[1]:
                data.append(row[0])
                target.append(row[1])

        data.append(data_test)
        target.append('positive')
        return data,target

def preprocess(x):

    data,target = load_file()
    count_vectorizer = CountVectorizer(binary='true')
    data = count_vectorizer.fit_transform(data)
    tfidf_data = TfidfTransformer(use_idf=x).fit_transform(data)

    return tfidf_data

def learn_model(data,target):

    data_train = data
    target_train = target

#--------------------------------------------------------------------------------
    
    indptr = data_train.indptr
    indptr1 = indptr.tolist()
    del indptr1[-1]
    indptr2 = np.asarray(indptr1)

    data1 = data_train.data
    data2 = data1.tolist()
    del data2[-1]
    data3 = np.asarray(data2)

    indices1 = data_train.indices
    indices2 = indices1.tolist()
    del indices2[-1]
    indices3 = np.asarray(indices2)

    a = data_train.shape[0] - 1
    b = data_train.shape[1]

    xyz = scipy.sparse.csr_matrix( (data3,indices3,indptr2), shape=(a, b))

    del target_train[-1]

#-------------------------------------------------------------------------
    data_test = data_train.getrow(-1);
    classifier = sklearn.svm.LinearSVC().fit(xyz,target_train)
    predicted = classifier.predict(data_test)
    print(predicted)


def main():
    print ('\n--------------Using tf--------------')
    data,target = load_file()
    tf_idf = preprocess(False)
    learn_model(tf_idf,target)

    print ('\n--------------Using tfidf--------------')
    data,target = load_file()
    tf_idf = preprocess(True)
    learn_model(tf_idf,target)

if __name__ == "__main__":
    main()