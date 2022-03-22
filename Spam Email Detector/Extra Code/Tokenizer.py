from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer

# getting sentences from document
document = "Email spam, also called junk email, " \
           "is unsolicited messages sent in bulk by " \
           "email (spamming). The name comes from " \
           "Spam luncheon meat by way of a Monty " \
           "Python sketch in which Spam is ubiquitous, " \
           "unavoidable, and repetitive. "
sent = sent_tokenize(document)
print(f"Sentence from document: {sent}\n")

# getting words from sentance
sentence = 'This is the first document.'
words = word_tokenize(sentence)
print(f"Words from sentence: {words}\n")

# Tokenization using regex
print("\nTokenization using Regex\n")
tokenizer = RegexpTokenizer('[a-zA-Z@.]+')
useful = tokenizer.tokenize(sentence)
print(useful)
