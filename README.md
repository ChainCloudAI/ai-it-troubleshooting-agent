# 🧑‍🏫 AI IT Troubleshooting Agent

An AI-powered IT troubleshooting assistant that guides users step-by-step to diagnose and fix technical issues.

Built using a local LLM (Llama 3 via Ollama), this agent combines structured reasoning, a knowledge base (RAG), and real system diagnostics for practical IT support.

---

## 🚀 Features

- 🤖 AI Troubleshooting Agent  
  - Asks one question at a time  
  - Follows logical IT workflows  
  - Adapts based on user responses  

- 🧠 Retrieval-Augmented Generation (RAG)  
  - Uses a custom `knowledge.txt`  
  - Provides structured, real-world solutions  

- 🛠️ Tool-Based Diagnostics  
  - Checks real internet connectivity (`ping`)  
  - Uses results to guide decisions  

- 🔄 Iterative Problem Solving  
  - Continues troubleshooting until solved  
  - Mimics real IT support  

- 💬 Chat UI  
  - Built with Streamlit  
  - Clean dark theme  
  - Step-by-step interaction  

- 🎯 Mentor-Style AI  
  - Explains reasoning  
  - Guides clearly  
  - Teaches while solving  

---

## 🧰 Tech Stack

- Python  
- Streamlit  
- Ollama (Llama 3)  
- Custom RAG  

---

## ⚙️ How to Run

### 1. Install dependencies

    pip install streamlit

---

### 2. Install and run Ollama

Download from: https://ollama.com

Then run:

    ollama run llama3

---

### 3. Run the app

    streamlit run ui.py

---

### 4. Open in browser

    http://localhost:8501

---

## 📂 Project Structure

    ai-it-troubleshooting-agent
    ├── app.py
    ├── ui.py
    ├── knowledge.txt
    └── .streamlit
        └── config.toml

---

## 📸 Example

User:
    I have no internet

Assistant:
- Checks connection  
- Detects device vs network issue  
- Guides step-by-step  
- Gives real fixes  

---

## 🔥 Why This Project

- AI agent design  
- Structured reasoning  
- RAG integration  
- Tool usage (real system checks)  
- Full-stack AI app (backend + UI)  

---

## 🚀 Future Improvements

- More tools (CPU, disk, memory)  
- Smarter RAG  
- Deploy online  
- UI improvements  

---

## 👤 Author

Huy Truong
