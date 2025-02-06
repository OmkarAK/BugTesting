import streamlit as st
import random

# Initialize the chat history if it's not already in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and subheader
st.title("Interactive Chatbot with Streamlit")
st.subheader("Describe your requirement:")

# Function to generate a bot response
def response_generator(user_input):
    # Sample complex conditions for generating responses
    if "oa" in user_input.lower():
        return "I was not able to find the OA"
    # elif "help" in user_input.lower() and "problem" in user_input.lower():
    #     return "It sounds like you're facing a problem. Can you please provide more details so I can help you better?"
    # elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
    #     return "You're welcome! If you have any other questions, feel free to ask."
    # elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
    #     return "Goodbye! Have a great day!"
    # elif len(user_input) < 5:
    #     return "Your input is too short. Can you please provide more details?"
    # elif any(word in user_input.lower() for word in ["error", "issue", "bug"]):
    #     return "I'm sorry to hear you're experiencing an error. Can you describe the issue in more detail?"
    else:
        return "I'm not sure how to respond to that. Can you please provide more details?"


# Display the chat history
st.subheader("Chat History")
for message in st.session_state.messages:
    st.markdown(f"{message['User']}")
    st.markdown(f"{message['Bot']}")
    st.write("---")

# Input form
with st.form(key="input_form"):
    user_input = st.text_input("You: ", key="user_input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Generate bot response
    bot_response = response_generator(user_input)

    # Store the interaction in session state
    st.session_state.messages.append({"User": user_input, "Bot": bot_response})

    # Clear the input field and rerun the script to update the display
    st.rerun()
