# AI Web Scraper & Summarizer (Azure OpenAI + Chainlit)

An AI-powered web scraping and summarization application that fetches webpage content, cleans and validates it, and generates concise summaries using **Azure OpenAI**. The project includes a **Chainlit-based UI** for interactive usage.

---

## 🚀 Features

* 🌐 Fetches content from public webpages
* 🧹 Cleans and extracts readable text from HTML
* ✅ Validates extracted content
* 🤖 Summarizes content using **Azure OpenAI (GPT models)**
* 🛡️ Handles blocked websites and network errors gracefully
* 💬 Interactive conversational UI using **Chainlit**

---

## 🧠 Architecture Overview

```
User (UI)
   ↓
Chainlit UI (ui.py)
   ↓
Pipeline Orchestrator
   ↓
[ Fetcher → Cleaner → Validator → Azure OpenAI Summarizer ]
   ↓
Structured Summary Output
```

---

## 📁 Project Structure

```
web-scraper/
│
├── app.py                     # Chainlit UI entry point
├── main.py                   # CLI entry point (optional)
│
├── pipeline/
│   └── run_pipeline.py       # Orchestrates the agent pipeline
│
├── scraper/
│   ├── fetcher.py            # HTTP fetching with headers
│   ├── cleaner.py            # HTML to text processing
│   └── validator.py          # Content validation
│
├── summarizer/
│   ├── llm.py                # Azure OpenAI integration
│   └── prompt.py             # Prompt templates
│
├── config.py                 # Environment & Azure config loader
├── .env                      # Azure credentials (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Azure OpenAI

Create a `.env` file in the project root:

```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

⚠️ **Important**

* Do NOT add quotes
* Restart terminal / IDE after creating `.env`

---

## ▶️ Running the Application

### Option A: Run with UI (Recommended)

```bash
chainlit run app.py
```

Open browser at:

```
http://localhost:8000
```

Paste a webpage URL to receive an AI-generated summary.

---

### Option B: Run via CLI

```bash
python main.py
```

---

### ⚠️ May Be Blocked (Handled Gracefully)

* AllRecipes
* Medium
* LinkedIn

> Some websites deploy bot-detection systems that block automated requests.

---

## 🛡️ Error Handling

* Network timeouts
* Bot-blocked websites (HTTP 403 / 460)
* Empty or insufficient content
* Invalid user input

Errors are reported cleanly in the UI.

---

## 🧪 Technologies Used

* Python 3.10+
* Requests
* BeautifulSoup4
* Azure OpenAI
* LangChain
* Chainlit
* dotenv

---


