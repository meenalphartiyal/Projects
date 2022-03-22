# Combining Tokenization, Stopwords removal, Stemming and Count Vectorization
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'Dan Morgan told himself he would forget Ann Turner.',
    'Sometimes he woke up in the middle of the night thinking of Ann , and then could not get back to sleep .',
    'His plans and dreams had revolved around her so much and for so long that now he felt as if he had nothing .',
    'He found that if he was tired enough at night , he went to sleep simply because he was too exhausted to stay awake.'
]


def remove_stopwords(sentence, stopwords):
    return [w for w in sentence if w not in stopwords]


def myTokenizer(document):
    tokenizer = RegexpTokenizer('[a-zA-Z@.]+')
    sw = set(stopwords.words('english'))
    words = tokenizer.tokenize(document.lower())
    # remove the stopwords
    words = remove_stopwords(words, sw)
    return words


# print(myTokenizer('this is a random text'))
vectorizer = CountVectorizer(tokenizer=myTokenizer)
X = vectorizer.fit_transform(corpus).toarray()
print(f"Length of the set: {len(X[0])}")
print(f"\nMy new vocabulary: {vectorizer.vocabulary_}")
