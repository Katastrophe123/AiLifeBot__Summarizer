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


##Complete Procedure Explaination
--Hey Everyone , I am Kanishk Singh Parihar from Mits Gwalior and this is my AI meeting Summarizer in which I have used HugginfFace LLM models to run my Idea .
--My idea is to take input from user and by using Langchain create a prompt template that will work effiecient to my LLM model i.e. meta-llama/Meta-Llama-3-8B-Instruct
--It stores output as a stroutput parser and then return me highly usable output as summary.
--Apart from this I have used fastapi for developing my backend work and React for Frontend which is not much developed due to Low submission time.
--Future Works that I can perform are as follow :
----I can use OpenAI text generation model for better output and Whisper API key for including new feture of text generation via Audio Input
----I can create better frontend using React , tailwind and Boostrap CSS which will enhance User Experience
