from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

# Load the preprocessed dataset
df = pd.read_csv('sentiment140_preprocessed.csv')

df.dropna(inplace=True)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Fit the vectorizer on the training data
X_train_vec = vectorizer.fit_transform(X_train)

# Transform the testing data using the fitted vectorizer
X_test_vec = vectorizer.transform(X_test)

# Create a logistic regression model
clf = LogisticRegression(random_state=42, max_iter=1000)

# Train the model on the vectorized training data
clf.fit(X_train_vec, y_train)

# Predict the sentiment for the test set
y_pred = clf.predict(X_test_vec)

# Compute the F1 score
f1 = f1_score(y_test, y_pred, average='binary', pos_label=4)

print('F1 score:', f1)
