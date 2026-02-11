# 🚀 Workflow Builder Lite

A lightweight AI-powered workflow automation tool that allows users to create modular text-processing workflows using Large Language Models (LLMs).

---
---

## 🚀 Live Demo

🔗 **Deployed Application:**  
https://workflow-builder-lite.onrender.com  

📊 **System Status Page:**  
https://workflow-builder-lite.onrender.com/status  

---



## ✨ Features

### 🔹 Workflow Steps

Create workflows with multiple processing steps:

- Clean Text  
- Summarize  
- Extract Key Points  
- Tag Category  

---

### 🔹 Execution Insights

- Step-by-step execution timeline  
- Token usage tracking per step  
- Success / failure status badges  

---

### 🔹 Run History

- Stores last 5 runs  
- Clickable previous runs  
- Automatically loads previous input and outputs  

---

### 🔹 System Monitoring

Dedicated health status page (`/status`)

- Backend health check  
- Database connectivity check  
- LLM configuration check  

---

### 🔹 User Experience

- Interactive UI (expandable step cards)  
- Spinner animation during execution  
- Clean, modern TailwindCSS design  

---

## 🛠 Tech Stack

- FastAPI – Backend framework  
- SQLAlchemy – ORM  
- SQLite – Database  
- OpenRouter API – LLM provider  
- TailwindCSS – UI styling  
- Jinja2 – Templating engine  

---

## ⚙️ How To Run Locally

### 1️⃣ Clone Repository

```bash
git clone <https://github.com/nileshdeb/workflow-builder-lite>
cd workflow-builder-lite
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 6️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Access Application

Open in browser:

```
http://127.0.0.1:8000
```

Status page:

```
http://127.0.0.1:8000/status
```

---

## ✅ What Is Implemented

- Modular workflow execution engine  
- Structured step return format (content, tokens, status)  
- Persistent run history (last 5 runs)  
- Health monitoring dashboard  
- Input validation  
- Safe environment variable usage  
- Interactive timeline UI  

---



## 📌 Project Structure

```
workflow-builder-lite/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── workflow_engine.py
│   ├── llm_service.py
│
├── templates/
│   ├── index.html
│   ├── status.html
│
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is open-source and available for educational and portfolio purposes.



