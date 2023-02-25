import pandas as pd
import train_model as tm

# Load the CSV file into a DataFrame
df = pd.read_csv('tweets.csv')

# Print the DataFrame
print(df)

# Extract the text data from the 'text' column
text_data = df['text'].tolist()

# Preprocess the text data (using the same preprocessing steps as before)
preprocessed_data = [tm.preprocess_text(text) for text in text_data]

# Vectorize the preprocessed data using the fitted vectorizer
X_test_vec = tm.vectorizer.transform(preprocessed_data)

# Use the trained model to predict the sentiment for the test data
y_pred = tm.clf.predict(X_test_vec)

print(y_pred)