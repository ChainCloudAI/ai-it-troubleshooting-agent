# AI IT Troubleshooting Agent

An AI-powered IT troubleshooting assistant that guides users step-by-step to diagnose and fix technical issues.

This project was built to simulate how real IT support operates. Rather than providing general answers, it follows a structured troubleshooting process and incorporates real system data to make informed decisions.

The system runs on a locally hosted language model using Ollama, allowing it to operate without reliance on external APIs or continuous internet access. This makes it suitable for privacy-sensitive or restricted environments.

Designed to replicate Tier 1–2 IT support workflows in a guided and explainable way, the system focuses on controlled reasoning and practical problem solving.

Built using a local LLM (Llama 3 via Ollama), the system combines structured reasoning, a knowledge base (RAG), and real system diagnostics to support practical IT troubleshooting.

---

## Features

### AI Troubleshooting Agent
- Asks one question at a time
- Follows logical IT workflows
- Adapts based on user responses

### Retrieval-Augmented Knowledge
- Uses a custom knowledge base (`knowledge.txt`)
- Provides structured, consistent troubleshooting steps

### Tool-Based Diagnostics
- Checks real internet connectivity using system commands
- Monitors system performance (CPU, RAM, disk usage)
- Uses real system data to guide troubleshooting decisions

### Iterative Problem Solving
- Continues troubleshooting until an issue is resolved
- Mirrors real IT support workflows

### Chat Interface
- Built with Streamlit
- Clean, dark-themed UI
- Structured, step-by-step user interaction

### Mentor-Style Guidance
- Explains reasoning behind each step
- Guides users through problems clearly
- Emphasizes understanding, not just solutions

---

## Tech Stack

- Python
- Streamlit
- Ollama (Llama 3)
- Retrieval-Augmented Generation (RAG)
- psutil (system diagnostics)

---

## How to Run

### 1. Install dependencies

pip install streamlit psutil

### 2. Install and run Ollama

Download from:  
https://ollama.com  

Then run:

ollama run llama3

### 3. Run the application

streamlit run ui.py

### 4. Open in browser

http://localhost:8501

---

## Project Structure

ai-it-troubleshooting-agent
├── app.py
├── ui.py
├── knowledge.txt
└── .streamlit
    └── config.toml

---

## Example

User input:  
I have no internet

System behavior:  
- Runs connectivity check  
- Determines whether issue is device or network related  
- Guides user step-by-step with targeted questions  
- Provides actionable troubleshooting steps  

---

## Why This Project

- Demonstrates structured AI agent design  
- Implements controlled, step-by-step reasoning  
- Uses real system diagnostics instead of assumptions  
- Integrates a custom knowledge base for consistent outputs  
- Runs locally without external API dependency  
- Simulates real-world IT support workflows  

---

## Future Improvements

- Expand diagnostic tools (network, processes, system services)  
- Enhance retrieval system for more precise knowledge matching  
- Improve UI with visual indicators and system status panels  
- Deploy using a hosted model or containerized backend  

---

## Author

Huy Truong
