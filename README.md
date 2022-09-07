# review-sentiment-analsyis

This project classifies any textual product or movie review into positive or negative using SVM classifier in both term frequency and inverse document frequency and Naive Bayes, running as a web service powered by Flask.

## Project Objective
The objective statement involves:
  - Building a classifier for polarity detection of product reviews.
  - Training and testing the classifier using a huge set of positive and negative reviews.
  - Performing sentiment analysis and classification - Uncovering the attitude of the author on a particular topic from the written text; alternatively known as “opinion mining” and “subjectivity detection”.
  - Using natural language processing and machine learning techniques to find statistical and/or linguistic patterns in the text that reveal attitudes.

The output sentiment scores **(1** or **-1)** can be used to identify the most positive and negative clauses or sentences with respect to particular movie aspects.

## Upcoming
Deploy to live environment (Heroku, Netlify, Vercel, etc.)

## Requirements
- Python
- PIP (Python Package Manager)

## How to Run
**1.** Clone this Repo <br />
**2.** Install Packages (pip install --upgrade -r requirements.txt) <br />
**3.** Run the SVM Classifier,

```
python app.py
```
or, Naive Bayes with Flask:
```
python main.py
```

## Data Sources
The research paper being referred to is – “Thumbs up? Sentiment Classification using Machine Learning Techniques” by Bo Pang and Lillian Lee and Shivakumar Vaithyanathan.

The training dataset and first testing dataset is at: https://inclass.kaggle.com/c/cs6998/data

The second testing dataset is at: https://www.cs.cornell.edu/people/pabo/movie-review-data

## Sample Comments
- **Positive:** This is a good product/movie 			
- **Negative:** This is not a good product/movie