import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request
import pickle

cv = pickle.load(open('word_list.pkl','rb'))
wordlist = cv.get_feature_names()
clf = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	review = request.form.get('review')

	input_review = transform_review(review)

	sentiment = clf.predict(input_review)[0]

	if sentiment == 1:
		return render_template('index.html', sentiment=1)
	else:
		return render_template('index.html', sentiment=-1)

	

def transform_review(review):
	count_words = []

	for word in wordlist:
		count_words.append(review.count(word))

	input_review = np.array(count_words).reshape(1,3000)

	return input_review
	

if __name__=="__main__":
	app.run()