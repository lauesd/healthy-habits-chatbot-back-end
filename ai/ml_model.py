import joblib

model = joblib.load("ai/intent_model.pkl")
vectorizer = joblib.load("ai/vectorizer.pkl")

def predict_intent(message: str) -> str:
    X = vectorizer.transform([message])
    return model.predict(X)[0]
