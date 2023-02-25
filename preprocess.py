from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

    import nltk
nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()

import nltk
nltk.download('stopwords')


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if not token in stop_words]
    # Stem the tokens
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # Join the stemmed tokens back into a single string
    preprocessed_text = " ".join(stemmed_tokens)
    return preprocessed_text

import pandas as pd

df = pd.read_csv('sentiment140.csv', header=None, names=['sentiment', 'ids', 'date', 'flag', 'user', 'text'], encoding='latin-1')

# Preprocess the text and keep the original target column
df['text'] = df['text'].apply(preprocess_text)

# Save the preprocessed dataset to a new CSV file
df.to_csv('sentiment140_preprocessed.csv', index=False)
