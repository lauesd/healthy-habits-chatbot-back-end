from ai.intents import detect_intent
from ai.rules import get_response


def process_message(message: str) -> dict:
    intent = detect_intent(message)
    reply = get_response(intent)

    return {
        "intent": intent,
        "reply": reply
    }
