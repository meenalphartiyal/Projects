from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('email_dataset.csv', encoding='ISO-8859-1')
le = LabelEncoder()
data = df.to_numpy()
# print(data)
# print(len(data))

X = data[:, 1]
y = data[:, 0]

# print(X.shape, y.shape)
tokenizer = RegexpTokenizer('\w+')
sw = set(stopwords.words('english'))
ps = PorterStemmer()


def getStem(review):
    review = review.lower()
    tokens = tokenizer.tokenize(review)
    removed_stopwords = [w for w in tokens if w not in sw]
    stemmed_words = [ps.stem(token) for token in removed_stopwords]
    clean_review = ' '.join(stemmed_words)
    return clean_review


def getDoc(document):
    d = []
    for doc in document:
        d.append(getStem(doc))
    return d


stemmed_doc = getDoc(X)
# print(stemmed_doc[:10]

vectorizer = CountVectorizer()
vc = vectorizer.fit_transform(stemmed_doc)
X = vc.todense()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=17)

# Naive Bayes from sklearn
model = MultinomialNB()
model.fit(X_train, y_train)
print(f"Score of my model: {model.score(X_test, y_test)}")


def prepare(message):
    d = getDoc(message)
    return vectorizer.transform(d)


print("Welcome to Spam Email Detector [Created by Meenal Phartiyal]")
print("Please enter your message\n")
message = [input()]

message = prepare(message)
y_pred = model.predict(message)
if y_pred[0] == 'spam':
    print("\nIt is a spam")
else:
    print("\nThe above mail is not a Spam mail.")
