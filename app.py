import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

st.title("LLM-as-a-Judge")
st.write("Send a prompt to the assistant and view its response.")

prompt = st.text_area("Prompt", placeholder="Enter your prompt")

if st.button("Send", type="primary"):
    if not prompt.strip():
        st.warning("Enter a prompt before sending.")
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("Set OPENAI_API_KEY in your environment or .env file to continue.")
        else:
            try:
                with st.spinner("Waiting for a response..."):
                    response = OpenAI(api_key=api_key).chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                    )
                st.subheader("Response")
                st.write(response.choices[0].message.content)
            except OpenAIError as error:
                st.error(f"The OpenAI request failed: {error}")
