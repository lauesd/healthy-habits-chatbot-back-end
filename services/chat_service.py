from ai.ml_model import predict_intent
from ai.rules import get_response

def process_message(message: str) -> dict:
    intent = predict_intent(message)
    reply = get_response(intent)

    return {
        "intent": intent,
        "reply": reply
    }
