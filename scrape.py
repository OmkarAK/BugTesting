import streamlit as st
from openpyxl import Workbook
from io import BytesIO

# Initialize the chat history if it's not already in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and subheader
st.subheader("Start here for OA Simple Price and Header Updates")
# st.subheader("Describe your Outline Agreement update request")

# Function to generate a bot response
def response_generator(user_input):
    if "oa" in user_input.lower():
        return "I was not able to find the OA"
    else:
        return "I'm not sure how to respond to that. Can you please provide more details?"

# Function to save chat history to Excel
def save_to_excel(messages):
    # Create a new workbook
    wb = Workbook()
    ws = wb.active
    # ws.title = "Chat History"

    # Add headers
    ws.append(["User Input", "Bot Response"])

    # Add messages
    for message in messages:
        ws.append([message["User"], message["Bot"]])

    # Save the workbook to a BytesIO object
    excel_bytes = BytesIO()
    wb.save(excel_bytes)
    excel_bytes.seek(0)

    return excel_bytes

# Display the chat history
# st.subheader("Chat History")
for message in st.session_state.messages:
    st.markdown(f"{message['User']}")
    st.markdown(f"{message['Bot']}")
    st.write("---")

# Input form
with st.form(key="input_form"):
    user_input = st.text_input(" ", key="user_input", placeholder="Describe your Outline Agreement update request")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Generate bot response
    bot_response = response_generator(user_input)

    # Store the interaction in session state
    st.session_state.messages.append({"User": user_input, "Bot": bot_response})

    # Clear the input field and rerun the script to update the display
    st.rerun()

# Button to download chat history as Excel
col1, col2, col3 = st.columns([1, 1, 1])

# Place the report button in the rightmost column
with col3:
    if st.button("Report"):
        excel_bytes = save_to_excel(st.session_state.messages)
        st.download_button(
            label="Download Excel",
            data=excel_bytes,
            file_name="chat_history.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )