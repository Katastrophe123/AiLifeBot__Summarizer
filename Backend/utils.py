import os
import tempfile
import fitz  # PyMuPDF
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load .env variables 
load_dotenv()

# Setup LLM via Hugging Face Inference API 
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    temperature=1.5
)

model = ChatHuggingFace(llm=llm)

# Utility to extract text from PDF or TXT
def extract_text_from_file(content: bytes, filename: str) -> str:
    text = ""

    # Handle PDF
    if filename.lower().endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        doc = fitz.open(tmp_path)
        for page in doc:
            text += page.get_text()
        doc.close()
        return text

    # Handle plain text files
    for encoding in ["utf-8", "windows-1252", "latin-1"]:
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to decode file using common encodings.")
