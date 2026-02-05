from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

texts = [
    "hello", "hi", "hey",
    "bye", "goodbye",
    "help me", "i need help",
    "i want to build a habit", "how to improve habits"
]

labels = [
    "greeting", "greeting", "greeting",
    "farewell", "farewell",
    "help", "help",
    "habit", "habit"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "ai/intent_model.pkl")
joblib.dump(vectorizer, "ai/vectorizer.pkl")
