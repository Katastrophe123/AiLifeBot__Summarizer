##Lelouch AI Summarizer
# 🤖 AI-Powered Action Item Extractor & Meeting Transcript Summarizer

Using **Hugging Face language models** and their inference API, this project uses **text or PDF transcripts** to extract meeting summaries, action items, and important insights. It has a FastAPI backend driven by LangChain and a React frontend.


---

## Features

- 📄 Paste raw text or upload PDF

AI-generated summaries of meetings

- ✅ Identifies issues, concerns, and next steps

- ⚡ Utilizes HuggingFace models ('meta-llama/Meta-Llama-3-8B-Instruct').

- 💬 Langchain backend + FastAPI

- 🌐 A live loading state in the React frontend

---

## Technology Stack

| Layer | Stack |
|------------|
| Frontend | React + Axios |
| PDF Parser | PyMuPDF (fitz) | 
| Env Mgmt | python-dotenv,.env file | 
| Backend | FastAPI, LangChain |
| AI Model | Hugging Face Inference API |

---
