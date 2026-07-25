# ============================================================
#  SIMPLE RULE-BASED CHATBOT
# ============================================================


def get_response(user_input):
    """
    This function is the chatbot's 'brain'.

    You hand it ONE line of text (whatever the user typed),
    and it hands back ONE line of text (the chatbot's reply).

    A function is just a named, reusable block of instructions -
    instead of writing the same logic over and over, you write
    it once here and 'call' get_response() whenever you need it.
    """
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! It's nice to hear from you."

    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"

    elif "your name" in user_input:
        return "I'm just a simple chatbot, but you can call me Chatty!"

    elif "thank" in user_input:
        return "You're welcome!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
    
        return "Hmm, I don't understand that yet. Could you try rephrasing?"


def start_chat():
    """
    This function runs the actual back-and-forth conversation.

    It uses a loop - code that repeats itself automatically -
    so we don't have to write "ask, reply, ask, reply..." by
    hand. It just keeps going until the user says bye.
    """

    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' anytime to end our chat.\n")

    while True:
        user_input = input("You: ")

       
        reply = get_response(user_input)

        
        print("Chatbot:", reply)

        
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break



if __name__ == "__main__":
    start_chat()
