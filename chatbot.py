# ============================================================
#  SIMPLE RULE-BASED CHATBOT
# ============================================================
# "Rule-based" means this bot has no real intelligence.
# It doesn't learn and it doesn't understand language -
# it just does three things, every single time:
#     1. Listens to what you typed.
#     2. Compares it to a list of phrases it already knows.
#     3. Replies with whatever pre-written answer matches.
#
# Everything below builds that logic, one small piece at a time.
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

    # Make everything lowercase and trim extra spaces, so that
    # "Hello", "HELLO", and "  hello  " are all treated the same.
    # Without this line, "Hello" and "hello" would count as
    # completely different, unmatched strings in Python.
    user_input = user_input.lower().strip()

    # This if / elif / else ladder is the actual decision-maker.
    # Python checks each condition in order, top to bottom, and
    # stops at the very first one that turns out to be true.

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
        # None of our rules matched, so we fall back to a
        # polite, honest reply instead of crashing or guessing.
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
        # input() pauses the program and waits for the user to
        # type something and press Enter.
        user_input = input("You: ")

        # Hand that text to our "brain" function and store
        # whatever reply it decides to give back.
        reply = get_response(user_input)

        # print() is how the chatbot "talks" - it just displays
        # text on the screen.
        print("Chatbot:", reply)

        # If the user said bye/goodbye, break out of the loop.
        # Without this line, the chat would run forever!
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break


# This last part is a common Python habit. It means:
# "only run start_chat() if this file is executed directly" -
# rather than, say, imported into some other file.
if __name__ == "__main__":
    start_chat()
