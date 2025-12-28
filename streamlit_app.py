import streamlit as st
import requests

# Set page title and header
st.set_page_config(page_title="AI Customer Support", layout="centered")
st.title("🤖 Agentic AI Customer Support")
st.markdown("---")

# Initialize chat history to persist across sessions [cite: 27]
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
if prompt := st.chat_input("How can I help you today? (e.g., Order status, Refund)"):
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Prepare payload for n8n Webhook [cite: 78, 106]
    n8n_webhook_url = "http://localhost:5678/webhook/customer" # Note: Use your Test URL from the screenshot
    payload = {"message": prompt}

    # 3. Send request to n8n and handle response
    try:
        with st.spinner("Agent is thinking..."):
            response = requests.post(n8n_webhook_url, json=payload)
            
            if response.status_code == 200:
                # Assuming n8n returns a JSON: {"reply": "..."}
                data = response.json()
                answer = data.get("reply", "I received your message but have no specific response.")
                
                # Add assistant response to chat history
                with st.chat_message("assistant"):
                    st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error(f"Error: Received status code {response.status_code}")
    except Exception as e:
        st.error(f"Failed to connect to n8n: {e}")

# Footer for the lab
st.markdown("---")
st.caption("Agentic AI Lab - INPT 2025")