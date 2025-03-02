import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Smart Chatbot", page_icon="❤️", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .chat-container {
            background-color: #1E1E1E;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .bot-message {
            background-color: #2E3B4E;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: white;
        }
        .user-message {
            background-color: #0066FF;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: white;
            text-align: right;
        }
        /* --- White Input Bar --- */
        .stTextInput>div>div>input {
            background-color: white !important;
            color: black !important;
            border-radius: 10px;
            padding: 10px;
            border: 2px solid #0066FF;
        }
        /* Footer Text Color */
        .footer-text {
            text-align: center;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# --- CHATBOT RESPONSES ---
responses = {
    "yes": "Yes, I am a chatbot! 😊",
    "no": "No, I am a chatbot! 🤖",
     "hy":"Hello there! 👋 How can I assist you today?",
    "hello": "Hello there! 👋 How can I assist you today?",
    "how are you": "I'm just a bot, but I'm feeling great! 😃 How about you?",
    "what's your name": "I am Smart Chatbot! 🤖",
    "bye": "Goodbye! Have a great day! 👋😊",
    "thank you": "You're very welcome! Happy to help! 🙏😃",
    "who created you": "I was created by an awesome developer! 🛠️🤓",
    "tell me a joke": "Why did the chatbot cross the road? To optimize the other side! 😂",
    "hello": "Hi there! How can I assist you? 😊",
    "hi": "Hello! How’s your day going?",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! Hope you have a great day! ☀️",
    "good night": "Good night! Sleep well. 🌙",
    "good afternoon": "Good afternoon! How’s your day going?",
    "good evening": "Good evening! Hope you had a great day!",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I’m your friendly chatbot, here to help! 😊",
    "who created you": "I was built using Python and Streamlit!",
    "where do you live": "I live in the cloud! ☁️",
    "how old are you": "I'm ageless! Time doesn’t affect me. 😎",
    "can you think": "I process information but don’t actually think like humans.",
    "are you human": "No, I'm a chatbot! But I try my best to chat like a human. 🤖",
    "can I give you a nickname": "Sure! What would you like to call me? 😊",
    "your nickname is bot": "That works! You can call me whatever you like. 🤖",
    "I will call you genius": "I love that! Thanks! 😃",
    "can I call you buddy": "Of course! I'm happy to be your buddy! 👫",
    "do you like nicknames": "Yes! Nicknames make chatting more fun! 🎉",
    "can I call you assistant": "Yes! I'm here to assist you anytime. 😊",
    "I will name you chatboty": "That sounds cool! I like it. 😃",
    "I’ll call you AI friend": "That’s sweet! I’m happy to be your AI friend. 🤖💙",
    "what's up": "Not much, just here to chat with you!",
    "how was your day": "It’s been great! How about yours?",
    "tell me about yourself": "I’m a chatbot that loves to chat and help!",
    "do you like humans": "Of course! You all are amazing. 😊",
    "what do you do": "I chat, answer questions, and try to make your day better!",
    "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts! 😂",
    "tell me another joke": "Why do cows have hooves instead of feet? Because they lactose! 🐄😂",
    "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey still edible! 🍯",
    "what's the meaning of life": "42! (According to The Hitchhiker's Guide to the Galaxy) 😆",
    "can you dance": "I wish! Maybe in a virtual world. 💃",
    "do you sleep": "Nope, I’m always awake and ready to chat!",
    "do you like pizza": "I can’t eat, but I hear pizza is amazing! 🍕",
    "what's your favorite color": "I like all colors! But blue seems cool. 🔵",
    "can you sing": "I wish! But I can hum some text for you. 😆",
    "how can I improve my communication skills": "Practice regularly, listen actively, and engage in conversations confidently. 🗣️",
    "how can I manage stress": "Try deep breathing, meditation, or engaging in activities you enjoy! 🌿",
    "how can I focus better": "Eliminate distractions, take short breaks, and create a to-do list. ✅",
    "how to build confidence": "Believe in yourself, practice self-care, and challenge negative thoughts. 💪",
    "how to prepare for an interview": "Research the company, practice answers, and dress confidently. 👔",
    "how to improve time management": "Prioritize tasks, use a planner, and avoid procrastination. ⏳",
    "how can I help others": "Volunteer, donate, be kind, and support people in need. ❤️",
    "how can I improve my mental health": "Stay active, connect with loved ones, and practice mindfulness. 🧘",
    "how can I study better": "Use active learning techniques, take breaks, and stay organized. 📚",
    "how can I sleep better": "Maintain a sleep schedule, reduce screen time, and create a relaxing bedtime routine. 😴",
    "how can I create a project": "Start with a plan, break it into tasks, and stay consistent! 🚀",
    "what is the best way to learn coding": "Practice regularly, work on real projects, and never stop learning! 💻",
    "bye": "Goodbye! Have a great day! 👋",
    "see you later": "See you soon! Take care!",
    "goodbye": "Goodbye! It was nice chatting with you!",
    "take care": "You too! Stay safe! 😊",
    "what can you do": "I can chat with you, tell jokes, answer questions, and much more!",
    "who is your favorite celebrity": "I like all celebrities equally! 😃",
    "do you like music": "Yes! But I can’t listen, just read lyrics. 🎵",
    "can you help me": "Of course! What do you need help with?",
    "do you know everything": "Not everything, but I'm learning every day!",
    "can you tell me a story": "Sure! Once upon a time, there was a curious person who met a chatbot… and they became friends! 😊",
    "what's your favorite food": "I don't eat, but I hear sushi is popular! 🍣",
    "what is your hobby": "Chatting and learning new things! 📚",
    "are you real": "I exist in the digital world! So, kinda real? 🤖",
    "how fast can you answer": "Super fast! As quick as you can type. 🚀",
    "can you be my friend": "Of course! I’d love to be your chatbot friend! 😊",
    "what's your favorite movie": "I like sci-fi movies! But I don’t actually watch them. 🎬",
    "do you get tired": "Nope! I have unlimited energy. ⚡",
    "can you make me laugh": "I’ll try! Why did the tomato turn red? Because it saw the salad dressing! 😂",
    "what's your favorite book": "I like all books! But I can’t read them. 📚"

}

# --- CHAT HISTORY ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- CHAT FUNCTION ---
def handle_input():
    user_input = st.session_state.user_input.strip()

    if user_input:
        lower_input = user_input.lower()
        response = responses.get(lower_input, "I'm not sure about that, but I’m learning! 😊")

        # Check if input is a name (assuming a single word starting with uppercase)
        if user_input.istitle() and len(user_input.split()) == 1:
            response = f"Wow! Is {user_input} your name? It's so pretty, just like you! 😊✨"

        # Append to chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

        # Clear input
        st.session_state.user_input = ""

# --- TITLE & UI ---
st.markdown("<h1 style='text-align: center; color: white;'>💬 Smart Chatbot ✨😊</h1>", unsafe_allow_html=True)
st.write("### LET'S CHAT WITH BOT")

# --- DISPLAY CHAT MESSAGES ---
for role, message in st.session_state.chat_history:
    message_class = "user-message" if role == "You" else "bot-message"
    st.markdown(f"<div class='{message_class}'>{role}: {message}</div>", unsafe_allow_html=True)

# --- INPUT FIELD (White Bar) ---
st.text_input("Type your message here...❤️✨", key="user_input", on_change=handle_input)

# --- FOOTER ---
st.markdown("<p class='footer-text'>© 2025 Smart Chatbot. All rights reserved Muqaddas ✨.</p>", unsafe_allow_html=True)
