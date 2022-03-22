from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document',
    'This document is second document',
    'And this is the third document',
    'Is this the first document?'
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print()
print(X.toarray())


