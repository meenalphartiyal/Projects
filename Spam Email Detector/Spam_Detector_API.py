from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from tkinter import *
from tkinter.font import Font

# Machine Learning Section:
# Reading the Dataset File
# The dataset that I used has about 5000 emails including both spam mails
# and ham mails in an excel sheet as a csv (comma separated) file

# Using Pandas Dataframe
df = pd.read_csv('email_dataset.csv', encoding='ISO-8859-1')
data = df.to_numpy()

# Feature Array including all the emails
X = data[:, 1]
# Target Array including the type (Spam/Ham)
y = data[:, 0]

# Initializing functions to that will help in
# 1. Breaking down emails into words using Regular Expression Tokenization
# 2. Removing Stopwords
tokenizer = RegexpTokenizer('\w+')
sw = set(stopwords.words('english'))
ps = PorterStemmer()


# This Function will tokenzise all the emails, removes stopwords,
# stem all the words and then creates a new vocab.
def getStem(review):
    review = review.lower()
    tokens = tokenizer.tokenize(review)
    removed_stopwords = [w for w in tokens if w not in sw]
    stemmed_words = [ps.stem(token) for token in removed_stopwords]
    clean_review = ' '.join(stemmed_words)
    return clean_review


# This function will get me all the emails tokenized,stopwords removed and stemmed as an array
def getDoc(document):
    d = []
    for doc in document:
        d.append(getStem(doc))
    return d


stemmed_doc = getDoc(X)

# Converting the edited document into numbers using Count Vectorizer Function
vectorizer = CountVectorizer()
vc = vectorizer.fit_transform(stemmed_doc)
X = vc.todense()

# Now that I have our dataset as a matrix of frequency of relevant words
# I can divide my dataset into a training set (that will train my machine about spam and ham mail)
# and Testing set (this will be used to test the model created)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17)

# Naive Bayes from sklearn to create Machine Learning model
model = MultinomialNB()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)


# Message (email) from the user
def prepare(msg):
    d = getDoc(msg)
    return vectorizer.transform(d)


# GUI Section
# Initializing the the main gui function
# Title: Spam Email Detector
root = Tk()
root.title("Spam Email Detector")
root.iconbitmap('mail_icon.ico')
root.geometry("1252x726")

# Defining the fonts
# Title Heading Font Style
headingFont = Font(
    family="Georgia",
    size=40,
    weight="bold"
)

# Body Font Style
bodyFont = Font(
    family="Lucida Console",
    size=10
)

# Button Font Style
btnFont = Font(
    family="Lucida Console",
    weight="bold"
)

# Answer Font Style
answerFont = Font(
    family="Georgia",
    size=50,
    weight="bold"
)

# Background Layout
my_img = PhotoImage(file="Background.png")
frame = Label(root, image=my_img)
frame.place(x=0, y=0)

# Heading Label
heading = Label(root, text="Spam Detection", font=headingFont, fg="#DFDFDF", bg="#2B3032")
heading.place(x=85, y=50)

# Message from Creator and Instruction Label
creator_message = f"""With an Accuracy score of {round(score*100, 3)}%,\n
Check if the Email you type is Spam or Not.\n 
This Application is trained to evaluate if an \n
email is spam or not spam (ham).\n 
The model has been trained on a dataset of over \n
5000 emails including both 'Spam' and 'not Spam'\n
Please enter the email below in the text field and \n
then click on Check button."""

info = Label(text=creator_message, width=60, height=18, bg="#404244", fg="#DFDFDF", font=bodyFont, bd=2, relief=SOLID)
info.place(x=65, y=150)

# User Input Text Field for writing email
email = Text(width=58, height=15, fg="#404244", padx=10, pady=10, font=bodyFont, bd=3, relief=SUNKEN)
email.place(x=65, y=420)


# Result Button Command Function
def OnClick():
    email_message = email.get("1.0", "end")
    global res
    global message
    message = [email_message]
    message = prepare(message)

    # Model trained now its time to test our model
    y_pred = model.predict(message)
    if y_pred[0] == 'spam':
        res = "Spam"
    else:
        res = " Ham"
    answer = Label(text=res, bg="#1E2122", fg="#DFDFDF", font=answerFont)
    answer.place(x=830, y=310)


    # Try Agaib Button Command Function
    def again():
        email.delete("1.0", "end")
        answer.destroy()

    # Clicking this button will clear the answer
    # of previous mail and clears to text field for the next mail
    tryAgain_btn = Button(text="TRY AGAIN", width=15, height=2, font=btnFont, command=again)

    # Clicking this button exits from the program
    exit_btn = Button(root, text="EXIT", width=15, height=2, font=btnFont, command=root.quit)

    tryAgain_btn.place(x=840, y=150)
    exit_btn.place(x=840, y=510)


# Clicking on this button shows the result.
check_btn = Button(text="CHECK", width=15, height=2, font=btnFont, relief=SOLID, command=OnClick)
check_btn.place(x=215, y=615)


# status bar
status = Label(root, text="Created By Meenal Phartiyal  ",width=178, bd=1, relief=SUNKEN, anchor=E)
status.place(x=0, y=705)

mainloop()
