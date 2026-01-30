# AI Web Scraper & Summarizer (Azure OpenAI + Chainlit)

An **AI-powered, hybrid web scraping and summarization system** that supports both **static HTML** and **JavaScript-rendered websites** using a fallback strategy. The application provides a **conversational UI built with Chainlit** and uses **Azure OpenAI** for high-quality summaries.

---

## ✨ Key Highlights

* 🌐 Scrapes **static HTML websites** using HTTP requests
* ⚡ Automatically falls back to **JavaScript rendering (Playwright)** when needed
* 🤖 Summarizes content using **Azure OpenAI (GPT models)**
* 💬 Interactive **Chainlit UI** with progress animations
* 🛡️ Graceful handling of blocked, JS-heavy, and authenticated websites
* 🧠 Clean, modular, and evaluation-ready architecture

---

## 🧠 Architecture Overview

```
User
 ↓
Chainlit UI (app.py)
 ↓
Async Pipeline Orchestrator
 ↓
[ HTML Fetcher ] ──▶ Validator ──▶ Azure OpenAI
        │
        └─▶ (Fallback) JS Fetcher (Playwright)
```

---

## 📁 Project Structure

```
web-scraper/
│
├── app.py                    # Chainlit UI (async)
│
├── pipeline/
│   └── run_pipeline.py       # Async orchestration logic
│
├── scraper/
│   ├── fetcher.py            # HTTP-based scraper
│   ├── js_fetcher.py         # JavaScript-enabled scraper (Playwright async)
│   ├── cleaner.py            # HTML → readable text
│   └── validator.py          # Content validation & site-aware checks
│
├── summarizer/
│   ├── llm.py                # Azure OpenAI integration
│   └── prompt.py             # Prompt templates
│
├── config.py                 # Azure & environment config
├── .env                      # Secrets (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\\Scripts\\activate   # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Playwright Browser

```bash
python -m playwright install chromium
```

---

### 4️⃣ Configure Azure OpenAI

Create a `.env` file in the project root:

```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

⚠️ Notes:

* Do **not** use quotes
* Restart terminal / IDE after saving

---

## ▶️ Running the Application

### 🚀 Start the Chainlit UI (Recommended)

```bash
python -m chainlit run app.py
```

Open your browser at:

```
http://localhost:8000
```

Paste a webpage URL to receive an AI-generated summary.

---

## 🌍 Supported Website Types

| Website Type | Example             | Supported          |
| ------------ | ------------------- | ------------------ |
| Static HTML  | BBC, Wikipedia      | ✅ Yes              |
| JS-rendered  | Blogs, Recipe sites | ✅ Yes (Playwright) |
| Auth-gated   | Instagram, LinkedIn | ❌ Limited          |

> Platforms requiring login or aggressive bot protection may restrict content access.

---

## 🛡️ Error Handling & UX

* Detects empty / insufficient content
* Automatically escalates to JavaScript rendering
* Explains failures clearly to the user
* Prevents hallucinated summaries

---

## 🧪 Tech Stack

* Python 3.10+
* Chainlit (UI)
* Azure OpenAI (LLMs)
* LangChain
* Requests
* BeautifulSoup4
* Playwright (async)
* python-dotenv

---
