# Intent detection
# -------------------------
def detect_intent(message: str) -> str:
    text = message.lower()

    if "hello" in text or "hi" in text:
        return "greeting"
    if "bye" in text or "goodbye" in text:
        return "farewell"
    if "help" in text:
        return "help"
    if "habit" in text:
        return "habit"
    
    return "unknown"
