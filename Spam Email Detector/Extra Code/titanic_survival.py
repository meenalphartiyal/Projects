import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17)

print("Dataset Details!")
print(f"Whole dataset : {X.shape, y.shape}")
print(f"Training set  : {X_train.shape, y_train.shape}")
print(f"Testing set   : {X_test.shape, y_test.shape}")

# Building and Evaluating Model with training and testing set
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"\nScore of the model: {model.score(X_test, y_test)}")
print(f"\nProbability of survival for first 10 entries of the dataset\n{model.predict_proba(X_test[:10])}\n\n")

print("\n")

# A person from Pclass = 3, is a male, age is 22, has 1 sibling/spouse aboard, has no parents/children aboard,
# paid $7.25.
print(model.predict([[3, True, 22.0, 1, 0, 7.25]]))



