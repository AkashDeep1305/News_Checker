import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
import nltk
from nltk.corpus import stopwords
import string
import pickle

# Download NLTK data
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Preprocessing function with NaN handling
def clean_text(text):
    if not isinstance(text, str):  # Check if text is not a string (NaN or other types)
        text = ""  
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

# Load dataset
df = pd.read_csv("backend/news_headlines.csv")  # Ensure dataset has 'text' and 'label' columns

df["text"] = df["text"].apply(clean_text)

# Convert text to numerical features
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["text"]).toarray()
y = df["label"].values  # 1 for Real, 0 for Fake

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Neural Network Model
model = Sequential([
    Dense(512, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Save Model & Vectorizer
model.save("backend/fake_news_model.h5")
pickle.dump(vectorizer, open("backend/vectorizer.pkl", "wb"))

print("Model and Vectorizer saved successfully!")
