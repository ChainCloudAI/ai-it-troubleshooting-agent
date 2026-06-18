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
- psutil (for system diagnostics)

---

## How to Run

### 1. Install dependencies
