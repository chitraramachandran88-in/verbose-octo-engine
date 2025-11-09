import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Text Summarizer", page_icon="📝", layout="wide")

st.title("📝 AI Text Summarizer")
st.write("Paste your long text below and get a concise summary powered by OpenAI.")

# User input
text_input = st.text_area("Enter text to summarize", height=250)

if st.button("Summarize"):
    if len(text_input.strip()) == 0:
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating summary..."):
            prompt = f"Summarize the following text in 4-5 concise sentences:\n\n{text_input}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            summary = response.choices[0].message.content
            st.success("✅ Summary generated!")
            st.write(summary)
