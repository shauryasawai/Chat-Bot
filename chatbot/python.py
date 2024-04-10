import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m fine, thanks for asking. How about you?']),
    (r'(.*) your name?', ['My name is Chatbot.', 'I am just a simple chatbot.', 'I am Chatbot.']),
    (r'what can you do', ['I can answer your questions and engage in a conversation. Feel free to ask!']),
    (r'what you can do for me?', ['I can answer your questions and engage in a conversation. Feel free to ask!']),
    (r'(.*) (weather|temperature) (.*)', ['Sorry, I am not able to provide weather information at the moment.']),
    (r'(.*) (age|old) (.*)', ['I am just a program, so I do not have an age.']),
    (r'how can I help you', ['You can ask me anything or we can just chat!']),
    (r'what is your purpose', ['My purpose is to assist you in any way I can.']),
    (r'(.*) (thank you|thanks)', ['You\'re welcome!', 'No problem.', 'Anytime!']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'(.*)', ['Sorry, I did not understand that.', 'Could you please rephrase that?', 'I am not sure I follow.']),
]
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I am a simple chatbot. How can I assist you today?")

    