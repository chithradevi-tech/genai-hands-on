# 🤖 Smart Role-Based Chatbot (Streamlit + FastAPI + LLM)

## 📌 Project Overview

This project is a **role-based AI chatbot** that dynamically changes its behavior based on the selected role:

* 👨‍🏫 **Teacher** → Explains concepts clearly with examples
* 🧑‍🤝‍🧑 **Friend** → Casual, friendly conversation
* 🎯 **Interviewer** → Asks questions and evaluates answers

The system is built using a **modern full-stack architecture**:

* **Frontend** → Streamlit (Chat UI)
* **Backend** → FastAPI (API layer)
* **LLM** → OpenAI API (language model)

---

## 🎯 Key Features

* 🔄 Role-based responses (dynamic system prompts)
* 💬 Chat interface with conversation memory
* ⚡ FastAPI backend for scalable API design
* 🧠 LLM-powered intelligent responses
* 🧩 Modular code structure (clean architecture)
* 🔐 Secure API key handling using `.env`

---

## 🏗️ Project Architecture

```
Streamlit (Frontend UI)
        ↓
FastAPI Backend (/chat API)
        ↓
OpenAI LLM (response generation)
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* FastAPI
* OpenAI API
* Requests
* Python-dotenv

---

## 📁 Project Structure

```
smart-chatbot/
│
├── backend/
│   ├── main.py
│   ├── llm.py
│   ├── prompts.py
│   ├── schemas.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation Steps

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd smart-chatbot
```

---

### 2️⃣ Setup Backend (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

python -m pip install -r requirements.txt
```

---

### 3️⃣ Setup Frontend (Streamlit)

```bash
cd ../frontend
python -m venv venv
venv\Scripts\activate

python -m pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root folder:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🔑 How to Create OpenAI API Key

1. Go to: https://platform.openai.com/
2. Sign in / create account
3. Navigate to **API Keys**
4. Click **Create new secret key**
5. Copy and paste into `.env`

👉 Note: You may need to enable billing to use the API.

---

## ▶️ How to Run the Application

### Step 1: Start Backend

```bash
cd backend
uvicorn main:app --reload
```

👉 Runs at: http://127.0.0.1:8000
👉 API Docs: http://127.0.0.1:8000/docs

---

### Step 2: Start Frontend

```bash
cd frontend
streamlit run app.py
```

👉 Opens chat UI in browser

---

## 🧪 Example Usage

### 🧑‍💻 Input (User)

```
Role: Teacher
Message: Explain React hooks
```

### 🤖 Output (AI Response)

```
React hooks are functions that let you use state and lifecycle features in functional components.
For example, useState allows you to manage state inside a component...
```

---

### 🎯 Interviewer Mode

**Input:**

```
Ask me JavaScript interview questions
```

**Output:**

```
1. What is closure in JavaScript?
2. Explain event delegation
3. Difference between var, let, const?
```

---

### 🧑‍🤝‍🧑 Friend Mode

**Input:**

```
I'm feeling nervous about interviews
```

**Output:**

```
Hey, that's totally normal! Interviews can be stressful, but you're preparing well...
```

---

## 🔄 API Request / Response Flow

### 📤 Request (Frontend → Backend)

```json
{
  "role": "Teacher",
  "messages": [
    { "role": "user", "content": "Explain Python decorators" }
  ]
}
```

---

### 📥 Response (Backend → Frontend)

```json
{
  "response": "A decorator in Python is a function that modifies another function..."
}
```

---

## 🧠 Why Use This Model?

We use:

```
gpt-4.1-mini
```

### Reasons:

* ⚡ Fast response time
* 💰 Low cost (budget-friendly)
* 🧠 Good balance of quality + performance
* 🚀 Suitable for real-time apps

---

## ⚠️ Common Issues

| Issue         | Cause               | Fix           |
| ------------- | ------------------- | ------------- |
| 429 Error     | No credits          | Add billing   |
| API key error | Wrong `.env`        | Check key     |
| No response   | Backend not running | Start FastAPI |

---

<img width="1905" height="917" alt="Screenshot 2026-04-19 120400" src="https://github.com/user-attachments/assets/736a5cd0-ab02-4a29-ba4c-96b170203402" />

<img width="1905" height="917" alt="Screenshot 2026-04-19 120415" src="https://github.com/user-attachments/assets/3bdd3eda-3a2f-4a4f-ac2d-9c73f5d17739" />

<img width="1905" height="917" alt="Screenshot 2026-04-19 120436" src="https://github.com/user-attachments/assets/31484261-5599-4f4c-8b38-bd6a554db3a6" />


---


