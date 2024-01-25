def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"

    elif "how are you" in user_input.lower():
        return "I am just a computer program, but thanks for asking!"

    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day."

    else:
        return "I am sorry, I did not understand that. Can you please clarify?"

def print_block(message):
    border = '+' + '-' * (len(message) + 2) + '+'
    print(border)
    print(f'| {message} |')
    print(border)

if __name__ == "__main__":
    print("Simple Chatbot in Block Console. Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print_block("Goodbye!")
            break

        response = simple_chatbot(user_input)
        print_block(response)
