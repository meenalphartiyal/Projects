from nltk.stem import PorterStemmer

ps = PorterStemmer()
print(ps.stem("laughed"))
print(ps.stem("laughing"))
print(ps.stem("laugh"))
