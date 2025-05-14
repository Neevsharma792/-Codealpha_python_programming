def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Chatbot: Hello there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just a program, but I'm doing fine. Thanks!")
        elif user_input in ["what's your name", "what is your name"]:
            print("Chatbot: I'm called SimpleBot.")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
