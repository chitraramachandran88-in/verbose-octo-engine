# 📝 AI Text Summarizer

A simple Streamlit web app that uses OpenAI's GPT model to summarize long text.

---

## 🚀 Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your OpenAI API key**

   Create a file called `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to **GitHub**
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Select your repo and `app.py`
4. Add your `OPENAI_API_KEY` in the app’s **Secrets**

Done! 🎉 You’ll get a public link like  
`https://yourname-text-summarizer.streamlit.app`
