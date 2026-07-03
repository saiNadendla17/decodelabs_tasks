# ==========================================
# DecodeLabs Artificial Intelligence Project 1
# Rule-Based AI Chatbot
# Developed by: Nadendla Sai Vyshnavi
# ==========================================

print("=" * 55)
print("      WELCOME TO DECODEBOT - AI CHATBOT")
print("=" * 55)
print("Hello! I am DecodeBot.")
print("I can answer basic questions.")
print("Type 'help' to see what I can do.")
print("Type 'exit' anytime to close the chatbot.")
print("=" * 55)

while True:

    user = input("\nYou : ").strip().lower()

    # Exit
    if user == "exit":
        print("\nBot : Thank you for chatting with me.")
        print("Bot : Have a wonderful day!")
        break

    # Greetings
    elif user in ["hi", "hello", "hey"]:
        print("Bot : Hello! Nice to meet you.")

    elif user == "good morning":
        print("Bot : 🌞 Good Morning! Have a wonderful and productive day!")

    elif user == "good afternoon":
        print("Bot : ☀️ Good Afternoon! Hope your day is going great!")

    elif user == "good evening":
        print("Bot : 🌇 Good Evening! Hope you had a fantastic day!")

    elif user == "good night":
        print("Bot : 🌙 Good Night! Sleep well and sweet dreams!")

    # Help Menu
    elif user == "help":
        print("\nI can answer questions like:")
        print("- hi")
        print("- hello")
        print("- good morning")
        print("- good afternoon")
        print("- good evening")
        print("- good night")
        print("- how are you")
        print("- your name")
        print("- who created you")
        print("- what is ai")
        print("- machine learning")
        print("- deep learning")
        print("- chatbot")
        print("- python")
        print("- java")
        print("- college")
        print("- course")
        print("- joke")
        print("- weather")
        print("- time")
        print("- thank you")
        print("- bye")
        print("- exit")

    # Personal Questions
    elif user == "how are you":
        print("Bot : I am doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot : My name is DecodeBot.")

    elif user == "who created you":
        print("Bot : I was created by Nadendla Sai Vyshnavi as part of the DecodeLabs Artificial Intelligence Internship Projects.")

    # AI Questions
    elif user == "what is ai":
        print("Bot : Artificial Intelligence enables computers to perform tasks that normally require human intelligence.")

    elif user == "machine learning":
        print("Bot : Machine Learning is a branch of AI where computers learn from data.")

    elif user == "deep learning":
        print("Bot : Deep Learning uses neural networks to solve complex problems.")

    elif user == "chatbot":
        print("Bot : A chatbot is a software application that simulates human conversation.")

    # Programming
    elif user == "python":
        print("Bot : Python is one of the most popular programming languages for AI.")

    elif user == "java":
        print("Bot : Java is widely used for enterprise software development.")

    # Internship
    elif user == "course":
        print("Bot : This project is part of the DecodeLabs Artificial Intelligence Internship.")

    elif user == "college":
        print("Bot : I hope your internship helps you build an excellent portfolio.")

    # Fun
    elif user == "joke":
        print("Bot : Why did the computer go to the doctor?")
        print("Bot : Because it caught a virus!")

    elif user == "time":
        print("Bot : Sorry! I cannot tell the current time yet.")

    elif user == "weather":
        print("Bot : Sorry! I cannot access live weather information yet.")

    elif user == "thank you":
        print("Bot : You're most welcome! Happy to help.")

    elif user == "bye":
        print("Bot : Goodbye! Have a wonderful day. See you again!")

    # Unknown Input
    else:
        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see the available commands.")

print("\n========== PROGRAM ENDED ==========")