def get_response(intent: str) -> str:
    if intent == "greeting":
        return "Hello! 👋 How can I help you with your habits today?"
    if intent == "farewell":
        return "Goodbye! Keep taking care of your habits 💪"
    if intent == "help":
        return "I can help you build healthy habits step by step."
    if intent == "habit":
        return "Consistency is key. Start small and stay consistent."

    return "Sorry, I didn't understand that. Can you rephrase?"
