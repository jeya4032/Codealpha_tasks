def chatbot():
    print("Hello! I am a simple chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! How are you?")

        elif user == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user == "your name":
            print("Bot: I am Python Chatbot.")

        elif user == "help":
            print("Bot: You can say hello, ask my name, or say bye.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()