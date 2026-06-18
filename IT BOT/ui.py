import streamlit as st
import ollama
import os
import psutil

# ✅ PAGE CONFIG
st.set_page_config(page_title="IT Mentor", layout="centered")

# ✅ CUSTOM CSS
st.markdown("""
<style>

/* FULL DARK BACKGROUND */
html, body, [class*="css"] {
    background-color: #020617 !important;
}

/* CENTERED APP */
.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 2rem;
}

/* MAIN CARD */
.main-card {
    background-color: #0f172a;
    padding: 32px;
    border-radius: 18px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.45);
}

/* TITLE */
h1 {
    text-align: center;
    color: #e2e8f0;
    margin-bottom: 20px;
}

/* CHAT BUBBLES */
.chat-bubble {
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: #e2e8f0;
    line-height: 1.5;
}

.ai-bubble {
    background-color: #1e293b;
}

.user-bubble {
    background-color: #334155;
}

/* INPUT FIELD */
input {
    background-color: #1e293b !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

/* BUTTON */
button {
    background-color: #3b82f6 !important;
    color: white !important;
    border-radius: 10px !important;
}

button:hover {
    background-color: #2563eb !important;
}

</style>
""", unsafe_allow_html=True)

# ✅ START CARD
st.markdown('<div class="main-card">', unsafe_allow_html=True)

# ✅ TITLE
st.title("🧑‍🏫 IT Troubleshooting Mentor")

# ✅ TOOL: INTERNET CHECK
def check_internet():
    result = os.system("ping -c 1 google.com > /dev/null 2>&1")
    if result == 0:
        return "✅ Internet is working"
    else:
        return "❌ No internet connection detected"

# ✅ TOOL: PERFORMANCE
def check_performance():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    return f"🧠 CPU Usage: {cpu}% | RAM Usage: {memory.percent}%"

# ✅ TOOL: DISK
def check_disk():
    disk = psutil.disk_usage('/')
    return f"💾 Disk Usage: {disk.percent}% used"

# ✅ LOAD KNOWLEDGE
def load_knowledge():
    with open("knowledge.txt", "r") as f:
        return f.read()

knowledge_base = load_knowledge()

# ✅ INITIAL CHAT
if "messages" not in st.session_state:
    st.session_state.messages = [
        "🤖 Hi, I’m your IT troubleshooting mentor.",
        "🤖 I’ll guide you step-by-step and explain what we’re checking.",
        "🤖 What problem are you experiencing?"
    ]

# ✅ DISPLAY CHAT
for msg in st.session_state.messages:
    if msg.startswith("You:"):
        st.markdown(f'<div class="chat-bubble user-bubble">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble ai-bubble">{msg}</div>', unsafe_allow_html=True)

# ✅ INPUT
with st.form(key="chat_form", clear_on_submit=True):

    user_input = st.text_input("You:")
    submit = st.form_submit_button("Send")

    if submit and user_input:

        st.session_state.messages.append(f"You: {user_input}")

        # ✅ INTERNET TOOL
        internet_status = ""
        if "internet" in user_input.lower() or "wifi" in user_input.lower():
            status = check_internet()
            st.session_state.messages.append(status)
            internet_status = status

        # ✅ PERFORMANCE TOOL
        performance_info = ""
        if "slow" in user_input.lower() or "lag" in user_input.lower():
            perf = check_performance()
            disk = check_disk()

            st.session_state.messages.append(perf)
            st.session_state.messages.append(disk)

            performance_info = perf + " | " + disk

        # ✅ BUILD PROMPT
        history = "\n".join(st.session_state.messages)

        prompt = f"""
You are an experienced IT troubleshooting mentor.

PERSONALITY:
- Explain clearly
- Teach step-by-step
- Calm and structured

STYLE:
- First explain what we know
- Then explain why it matters
- Then ask ONE clear question

RULES:
- Ask only ONE question
- Do not ask multiple questions
- Keep responses focused

Internet Status:
{internet_status}

Performance Data:
{performance_info}

- If internet works → device issue  
- If no internet → network issue  
- If CPU/RAM/disk high → performance issue  

Knowledge Base:
{knowledge_base}

Conversation:
{history}
"""

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = response["message"]["content"]
        st.session_state.messages.append(f"🤖 {reply}")

        st.rerun()

# ✅ END CARD
st.markdown('</div>', unsafe_allow_html=True)
