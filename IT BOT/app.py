import ollama
import os

# ✅ TOOL: CHECK INTERNET (WITH EMOJIS)
def check_internet():
    result = os.system("ping -c 1 google.com > /dev/null 2>&1")
    if result == 0:
        return "✅ Internet is working"
    else:
        return "❌ No internet connection detected"


# ✅ LOAD KNOWLEDGE FILE (RAG)
def load_knowledge():
    with open("knowledge.txt", "r") as f:
        return f.read()

knowledge_base = load_knowledge()


print("=== AI IT Troubleshooting Assistant (Smart Agent) ===\n")

issue = input("Describe your problem: ")

state = {
    "issue": issue,
    "answers": []
}

question_count = 0
phase = "questioning"

# ✅ INTERNET CHECK (RUN ONCE)
internet_status = ""

if "internet" in issue.lower() or "wifi" in issue.lower():
    print("\n🔍 Checking internet connection...\n")
    internet_status = check_internet()
    print(internet_status, "\n")


def build_prompt(state, phase, internet_status):
    history = "\n".join(state["answers"])

    return f"""
You are a skilled IT technician.

PHASE: {phase}

IMPORTANT CONTEXT:

Internet check result:
{internet_status}

🚨 HARD RULE (MUST FOLLOW):

- If Internet is working:
    → DO NOT treat this as a network outage
    → Assume this is a DEVICE-SPECIFIC issue
    → Focus on the user's device

- If NO internet:
    → Assume ROUTER / MODEM / NETWORK issue
    → Ask network-related questions

- ALWAYS reference the internet check before reasoning
- DO NOT ignore it

---

KNOWLEDGE BASE:
{knowledge_base}

---

User issue: {state["issue"]}

Conversation:
{history}

---

RULES:

IF PHASE = questioning:
- Ask ONE focused question
- Do not repeat

IF PHASE = diagnosis:
- Provide:
    ✅ Diagnosis
    ✅ Why
    ✅ Step-by-step fix

IF PHASE = followup:
- Continue helping if needed
"""


while True:

    # ✅ FOLLOW-UP CHECK
    if phase == "followup_check":
        print("\n👉 Did that solution fix your problem? (yes/no)\n")
        user_input = input("You: ").lower()

        if user_input in ["yes", "y"]:
            print("\n✅ Glad it’s fixed! Type 'exit' to finish.")
            phase = "end"
        else:
            print("\n🔄 Continuing troubleshooting...\n")
            question_count = 0
            phase = "questioning"

        continue


    # ✅ END STATE
    if phase == "end":
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("\n👋 Ending session.")
            break
        else:
            print("Type 'exit' to finish.")
            continue


    # ✅ AI RESPONSE (WITH TOOL CONTEXT)
    prompt = build_prompt(state, phase, internet_status)

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a logical IT troubleshooting expert."},
            {"role": "user", "content": prompt}
        ]
    )

    reply = response["message"]["content"]
    print("\n🤖", reply)


    # ✅ QUESTIONING PHASE
    if phase == "questioning":
        user_input = input("You: ")
        state["answers"].append(user_input)
        question_count += 1

        # ✅ ANTI-LOOP
        if len(state["answers"]) >= 3:
            last = state["answers"][-3:]
            if len(set(last)) <= 2:
                print("\n⚠️ Enough repeated info → diagnosing...\n")
                phase = "diagnosis"
                continue

        # ✅ MAX QUESTIONS
        if question_count >= 6:
            phase = "diagnosis"


    # ✅ DIAGNOSIS PHASE
    elif phase == "diagnosis":
        print("\n✅ Diagnosis provided.")
        phase = "followup_check"
