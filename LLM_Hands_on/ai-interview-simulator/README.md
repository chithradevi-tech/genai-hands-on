# 🎤 AI Interview Simulator (LLM Project – Free API)

## 📌 Overview

**AI Interview Simulator** is an interactive application that simulates real interview scenarios using a Large Language Model (LLM).

It allows users to:

* Receive interview questions
* Submit answers
* Get AI-based evaluation
* Track performance over time

This project uses a **free LLM API** from **Google AI Studio**, so no billing or credit card is required.

---

## 🎯 Goal

The goal of this project is to:

* Learn **context handling in LLM applications**
* Implement **multi-step prompting**
* Build **evaluation-based AI systems**
* Understand **structured output (JSON parsing)**

---

## 🚀 Features

* 🎯 Generate interview questions (role + level based)
* ✍️ Accept user answers
* 📊 Evaluate answers using LLM
* ⭐ Provide score, feedback, and improvements
* 🧠 Maintain session-based interview history
* 📂 Display previous responses in sidebar

---

## 🏗️ Architecture

```text
User Input (Role, Level)
        ↓
Question Generation (LLM)
        ↓
User Answer
        ↓
Evaluation Prompt
        ↓
LLM Evaluation
        ↓
Structured JSON Output
        ↓
Display Results (Streamlit UI)
```

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* Gemini API (LLM)
* python-dotenv (env management)

---

## 📁 Project Structure

```text
ai-interview-simulator/
│
├── app.py              # Main Streamlit UI
├── llm.py              # LLM integration
├── prompts.py          # Prompt templates
├── config.py           # API configuration
├── requirements.txt
├── .env
└── history.json        # (optional) store interview data
```

---

## ⚙️ Installation Steps

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd ai-interview-simulator
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

#### Activate:

**Windows (CMD):**

```bash
venv\Scripts\activate
```

**PowerShell (if blocked):**

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🔑 Setup Free API Key

Get your API key from **Google AI Studio**

### Steps:

1. Go to: https://aistudio.google.com/app/apikey
2. Click **Create API Key**
3. Copy the key

---

### Create `.env` file

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

👉 The app will open in your browser.

---

## 🧪 Example Workflow

### Step 1: Select Role & Level

* Role: Frontend Developer
* Level: Beginner

---

### Step 2: Generate Question

Example:

```
Explain useState in React.
```

---

### Step 3: Submit Answer

Example:

```
useState is a hook used to manage state in functional components...
```

---

### Step 4: Get Evaluation

```json
{
  "score": 7,
  "feedback": "Good explanation but lacks real-world example",
  "improvement": "Add example and explain re-render behavior"
}
```

---

## 🧠 Key Concepts Learned

* Context management using session state
* Multi-step prompting (question → answer → evaluation)
* Structured JSON output from LLM
* Error handling for invalid responses
* Real-world AI system design

---

## ⚠️ Common Issues & Fixes

### ❌ Invalid JSON Response

**Cause:** LLM returns extra text or markdown

**Fix:**

* Clean response before parsing
* Use strict prompt rules

---

### ❌ API Errors (429 / quota)

**Cause:** Free tier limit exceeded

**Fix:**

* Reduce requests
* Optimize prompt size

---

## 🚀 Future Improvements

* Multi-question interview flow
* Final cumulative score
* Timer for answers
* Domain-specific question bank
* Export interview report (PDF)
* Add React frontend

---

<img width="1905" height="917" alt="Screenshot 2026-04-19 154033" src="https://github.com/user-attachments/assets/1840fd3b-7bbe-49c4-92e1-eed113b27aae" />

<img width="1918" height="998" alt="Screenshot 2026-04-19 154101" src="https://github.com/user-attachments/assets/d0550bcc-264a-4e9f-a7dc-2e3f7492b36d" />

<img width="1906" height="983" alt="Screenshot 2026-04-19 154118" src="https://github.com/user-attachments/assets/fd5bdc07-7a27-44ff-ac3d-741135d35f46" />

<img width="1837" height="952" alt="Screenshot 2026-04-19 154321" src="https://github.com/user-attachments/assets/dbb4af8e-f7e1-446a-a068-59f8f7d64d81" />

<img width="1635" height="717" alt="Screenshot 2026-04-19 154414" src="https://github.com/user-attachments/assets/5d4fe703-6419-43b5-b9a2-8bc8b05e0c68" />







