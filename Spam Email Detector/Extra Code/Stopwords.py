from nltk.corpus import stopwords

sw = set(stopwords.words('english'))
text = "i am not a very good cricket player".split()


def remove_stopwords(sentence, stopwords):
    return [w for w in sentence if w not in stopwords]


useful_words = remove_stopwords(text, sw)
print(useful_words)

print(sw)
