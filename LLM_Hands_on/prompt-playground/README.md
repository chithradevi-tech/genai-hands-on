# 🧠 Prompt Playground (Free LLM)

## 📌 Overview

**Prompt Playground** is an interactive web app that helps you understand how **prompt quality affects LLM outputs**.

You can:

* Enter prompts
* Generate multiple responses
* Compare outputs side-by-side
* Control creativity using temperature
* Save and reuse prompts

This project uses a **free LLM API** from **Google AI Studio**, so no billing is required.

---

## 🎯 Goal

The main goal of this project is to:

* Learn **Prompt Engineering**
* Understand **LLM behavior**
* Experiment with **temperature & output variation**
* Improve prompt design skills

---

## 🚀 Features

* ✍️ Input custom prompts
* 🔁 Generate multiple outputs
* 📊 Compare responses side-by-side
* 🎛️ Control temperature (creativity)
* 💾 Save prompts locally
* 📂 View saved prompts from sidebar

---

## 🏗️ Architecture

```id="arch1"
User Input (Streamlit UI)
        ↓
Prompt Processing
        ↓
Gemini API (LLM)
        ↓
Multiple Responses
        ↓
UI Display (Comparison)
```

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* Gemini API (LLM)
* Python-dotenv (env management)

---

## 📁 Project Structure

```id="arch2"
prompt-playground/
│
├── app.py              # Streamlit UI
├── llm.py              # LLM integration
├── config.py           # API config
├── utils.py            # Save/load prompts
├── prompts.json        # Stored prompts
├── .env                # API key
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash id="cmd1"
git clone <your-repo-url>
cd prompt-playground
```

---

### 2️⃣ Create Virtual Environment

```bash id="cmd2"
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash id="cmd3"
python -m pip install -r requirements.txt
```

---

## 🔑 Setup API Key (FREE)

Get API key from **Google AI Studio**

### Steps:

1. Go to: https://aistudio.google.com/app/apikey
2. Click **Create API Key**
3. Copy the key

---

### Create `.env` file

```env id="env1"
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash id="cmd4"
streamlit run app.py
```

👉 The app will open in your browser

---

## 🧪 Example Usage

### 🔹 Example 1

**Input:**

```id="ex1"
Explain React hooks
```

**Output:**

* Output 1 → structured explanation
* Output 2 → more detailed explanation
* Output 3 → simplified version

---

### 🔹 Example 2

**Input:**

```id="ex2"
Write a short story about AI
```

👉 Observe how outputs differ with temperature

---

### 🔹 Example 3

**Input:**

```id="ex3"
Explain Python in 1 sentence
```

👉 Tests prompt clarity and instruction following

---

## 🎛️ Understanding Temperature

| Value | Behavior          |
| ----- | ----------------- |
| 0.0   | Very precise      |
| 0.5   | Balanced          |
| 1.0   | Creative / random |

---

## 🧠 What You Learn

* Prompt quality matters
* Same prompt can produce different outputs
* Temperature affects creativity
* Prompt tuning improves results

---

## 🔍 Where This is Useful

* AI product development
* Chatbot design
* LLM experimentation
* Interview preparation
* Prompt engineering practice

---

## ⚠️ Limitations

* Free API has usage limits
* Responses may vary each time
* No long-term memory

---

## 🚀 Future Improvements

* Add system prompts (role-based)
* Token usage display
* Prompt templates
* Export prompts as JSON
* Model selection dropdown

---

## 🧾 Summary

This project demonstrates:

* How to interact with LLM APIs
* How prompt design impacts output
* How to build an interactive AI tool

---

<img width="1905" height="917" alt="image" src="https://github.com/user-attachments/assets/c7536bf7-86fd-4b1f-b0d9-20cb40ed9180" />


<img width="1905" height="917" alt="Screenshot 2026-04-19 145128" src="https://github.com/user-attachments/assets/6e5d867a-fca3-4d33-a72e-0c3faaed5ade" />


<img width="1905" height="917" alt="Screenshot 2026-04-19 145203" src="https://github.com/user-attachments/assets/99a09915-2eae-47ca-a4da-155c9ac6bc53" />





