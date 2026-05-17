# 📄 Resume Analyzer (LLM Project – Free API)

## 📌 Overview

**Resume Analyzer** is an AI-powered application that analyzes resumes (PDF format) and provides structured insights such as:

* Extracted skills
* Experience summary
* Resume score
* Improvement suggestions

This project uses a **free Large Language Model (LLM)** from **Google AI Studio**, so no credit card or billing is required.

---

## 🎯 Goal

The goal of this project is to:

* Learn **structured output from LLMs (JSON)**
* Understand **prompt engineering for real-world use cases**
* Practice **PDF parsing**
* Implement **data validation and error handling**

---

## 🚀 Features

* 📤 Upload resume (PDF)
* 📄 Extract text from PDF
* 🧠 Analyze using LLM
* 📊 Generate structured JSON output
* ⭐ Score the resume
* 💡 Suggest improvements

---

## 🏗️ Architecture

```id="arch1"
User Upload (PDF)
        ↓
PDF Parsing (PyPDF)
        ↓
Prompt Engineering
        ↓
LLM (Gemini API)
        ↓
Structured JSON Output
        ↓
Display in Streamlit UI
```

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* Gemini API (LLM)
* PyPDF (PDF parsing)
* python-dotenv (environment variables)

---

## 📁 Project Structure

```id="arch2"
resume-analyzer/
│
├── app.py              # Main UI
├── llm.py              # LLM integration
├── parser.py           # PDF text extraction
├── schema.py           # Prompt template
├── config.py           # API config
├── requirements.txt
├── .env
└── sample_resume.pdf
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash id="cmd1"
git clone <your-repo-url>
cd resume-analyzer
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

## 🔑 Setup Free API Key

Get your API key from **Google AI Studio**

### Steps:

1. Visit: https://aistudio.google.com/app/apikey
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

👉 The app will open in your browser.

---

## 🧪 Example Output

```json id="ex1"
{
  "name": "Arjun Mehta",
  "skills": ["Python", "React", "FastAPI"],
  "experience_summary": "3 years of full stack development",
  "score": 85,
  "improvements": [
    "Add quantified achievements",
    "Improve project descriptions"
  ]
}
```

---

## 🧠 What You Learn

* How to extract text from PDFs
* How to design prompts for structured output
* How to parse and validate JSON responses
* How to integrate LLM APIs into applications
* How to handle real-world AI errors

---

## ⚠️ Limitations

* LLM may sometimes return invalid JSON
* Free API has usage limits
* Resume parsing depends on PDF quality

---

## 🚀 Future Improvements

* Add ATS (Applicant Tracking System) scoring
* Add job description matching
* Highlight missing skills
* Generate downloadable report (PDF)
* Add React frontend for better UI

---

<img width="1905" height="917" alt="Screenshot 2026-04-19 152237" src="https://github.com/user-attachments/assets/17892fc8-a5be-45f1-8730-958f821a19b4" />

<img width="1905" height="917" alt="Screenshot 2026-04-19 152136" src="https://github.com/user-attachments/assets/168d5ca8-5d0e-472e-903b-31cf0138a95f" />

<img width="1905" height="917" alt="Screenshot 2026-04-19 152203" src="https://github.com/user-attachments/assets/abd583bb-a527-482d-87e5-c2c7bab652ff" />




