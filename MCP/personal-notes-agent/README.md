CREATE DATABASE personal_notes;

USE personal_notes;

CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

### 1. Create Project Folder

```bash
mkdir personal-notes-agent
cd personal-notes-agent
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) C:\personal-notes-agent>
```

#### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install FastAPI

```bash
pip install fastapi
```

Install Uvicorn (FastAPI server):

```bash
pip install uvicorn
```

Or install everything together:

```bash
pip install fastapi uvicorn sqlalchemy pymysql openai python-dotenv streamlit
```

---

### 4. Verify Installation

```bash
pip list
```

You should see:

```text
fastapi
uvicorn
sqlalchemy
pymysql
openai
python-dotenv
```

---

### 5. Create Simple FastAPI App

Create `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working"}
```

Project structure:

```text
personal-notes-agent/
│
├── venv/
└── main.py
```

---

### 6. Run FastAPI

From the folder containing `main.py`:

```bash
uvicorn main:app --reload
```

Explanation:

```text
main      -> main.py
app       -> FastAPI() variable
--reload  -> auto restart on code changes
```

Output:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

### 7. Open in Browser

API:

```text
http://127.0.0.1:8000
```

Response:

```json
{
  "message": "FastAPI is working"
}
```

---

### 8. Open Swagger UI

FastAPI automatically creates API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You will see an interactive UI where you can test APIs without building a frontend.

---

### 9. Run Your Personal Notes Project

If your structure is:

```text
personal-notes-agent/
│
├── app/
│   └── main.py
```

Run:

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

and test:

* `/save`
* `/notes`
* `/chat`

from the Swagger UI.

---

### Common Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Stop FastAPI:

```text
CTRL + C
```

Check installed packages:

```bash
pip list
```

Check Python version:

```bash
python --version
```

For learning FastAPI, start with the simple `main.py` example first, confirm `/docs` works, and then gradually add MySQL, OpenAI, and MCP. This makes debugging much easier.

---

1. Create/Open an OpenAI Account

Go to:

OpenAI Platform

---

(venv) D:\genai-hands-on\MCP\personal-notes-agent>streamlit run frontend\ui.py

(venv) D:\genai-hands-on\MCP\personal-notes-agent>uvicorn backend.main:app --reload

 /d/genai-hands-on/MCP/personal-notes-agent (main) ------- git bash here and activate venv and run below
$ python -m mcp_app.mcp_server


test in frontend ui:

Remember my AWS account is for learning.

What AWS information did I save?

---

```text
Project:
Personal Notes MCP Agent

Tech:
FastAPI
MySQL
GOOGLE API
MCP

Features:
1. Store user memory
2. Retrieve memory
3. Delete memory
4. Tool calling
5. MCP server integration

Flow:

User
 ↓
Streamlit
 ↓
FastAPI /chat
 ↓
detect_action()
 ↓
HTTP Call
 ↓
MCP Server
 ↓
save_note_tool()
 ↓
MySQL
 ↓
MCP Response
 ↓
FastAPI
 ↓
Frontend
```

---

(venv) D:\genai-hands-on\MCP\personal-notes-agent>pip show mcp
Name: mcp
Version: 1.27.2
Summary: Model Context Protocol SDK
Home-page: https://modelcontextprotocol.io
Author: Anthropic, PBC.
Author-email:
License: MIT
Location: D:\genai-hands-on\MCP\personal-notes-agent\venv\Lib\site-packages
Requires: anyio, httpx, httpx-sse, jsonschema, pydantic, pydantic-settings, pyjwt, python-multipart, pywin32, sse-starlette, starlette, typing-extensions, typing-inspection, uvicorn
Required-by: