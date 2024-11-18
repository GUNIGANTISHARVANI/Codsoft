import random
import re
from datetime import datetime

# Define the chatbot function
def chatbot():
    # Memory store to remember user details
    user_name = None
    user_preferences = {}
    print("Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()  # Normalize input (case-insensitive, and remove leading/trailing spaces)

        # Exit condition
        if 'exit' in user_input or 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Greetings
        elif 'hello' in user_input or 'hi' in user_input:
            if user_name:
                print(f"Chatbot: Hello again, {user_name}! How can I assist you today?")
            else:
                print("Chatbot: Hi there! How can I assist you today?")
        
        # Asking how the bot is doing
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great! Thanks for asking. How are you?")
        
        # User asks for the chatbot's name
        elif 'your name' in user_input or 'what is your name' in user_input:
            print("Chatbot: I don't have a personal name, but you can call me Chatbot!")
        
        # User asks for the chatbot's memory
        elif 'remember' in user_input:
            if user_name:
                print(f"Chatbot: I remember your name is {user_name}. I also know your preferences: {user_preferences}.")
            else:
                print("Chatbot: I don't have anything to remember yet. Please tell me your name first!")

        # Asking for the user's name (store it in memory)
        elif 'your name' in user_input or 'what is your name' in user_input:
            if user_name:
                print(f"Chatbot: Your name is {user_name}, right?")
            else:
                print("Chatbot: What is your name?")
                user_name_input = input("You: ")
                user_name = user_name_input
                print(f"Chatbot: Nice to meet you, {user_name}!")

        # Asking about user preferences
        elif 'my preference' in user_input or 'preferences' in user_input:
            if user_preferences:
                print(f"Chatbot: Your current preferences are: {user_preferences}. Would you like to update them?")
            else:
                print("Chatbot: I don't know your preferences yet. What are they?")

        # Handling user preferences (e.g., color, food, etc.)
        elif 'i like' in user_input:
            preference = re.search(r'i like (.*)', user_input)
            if preference:
                preference_value = preference.group(1)
                user_preferences['likes'] = preference_value
                print(f"Chatbot: Got it! You like {preference_value}. I'll remember that!")

        # Compliments
        elif 'you are' in user_input or 'you\'re' in user_input:
            print("Chatbot: Thank you! You're awesome too!")
        
        # Asking for the current time
        elif 'what time is it' in user_input or 'tell me the time' in user_input:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        
        # Asking for the date
        elif 'what date is it' in user_input or 'today\'s date' in user_input:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")
        
        # Asking for a joke
        elif 'tell me a joke' in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my computer I needed a break, and now it won’t stop sending me kit-kats!",
                "Why do programmers prefer dark mode? Because the light attracts bugs!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")

        # Asking for help
        elif 'help' in user_input:
            print("Chatbot: I'm here to assist you. You can ask me things like 'How are you?', 'What's your name?', 'What time is it?', 'I like...', or just say 'bye' to exit.")
        
        # Simple math operations (basic calculations)
        elif 'plus' in user_input or 'add' in user_input:
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) == 2:
                result = int(numbers[0]) + int(numbers[1])
                print(f"Chatbot: {numbers[0]} + {numbers[1]} = {result}")
            else:
                print("Chatbot: Please provide two numbers to add.")
        
        elif 'minus' in user_input or 'subtract' in user_input:
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) == 2:
                result = int(numbers[0]) - int(numbers[1])
                print(f"Chatbot: {numbers[0]} - {numbers[1]} = {result}")
            else:
                print("Chatbot: Please provide two numbers to subtract.")
        
        elif 'multiply' in user_input or 'times' in user_input:
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) == 2:
                result = int(numbers[0]) * int(numbers[1])
                print(f"Chatbot: {numbers[0]} * {numbers[1]} = {result}")
            else:
                print("Chatbot: Please provide two numbers to multiply.")
        
        elif 'divide' in user_input or 'divide by' in user_input:
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) == 2 and int(numbers[1]) != 0:
                result = int(numbers[0]) / int(numbers[1])
                print(f"Chatbot: {numbers[0]} / {numbers[1]} = {result}")
            elif len(numbers) == 2:
                print("Chatbot: Division by zero is not allowed!")
            else:
                print("Chatbot: Please provide two numbers to divide.")

        # Default response for unrecognized input
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you ask something else?")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
