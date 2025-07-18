from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from summary import get_summary_chain
from utils import extract_text_from_file

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the LangChain chain (prompt | llm | output_parser)
summary_chain = get_summary_chain()


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    content = await file.read()

    try:
        # Extract transcript text from uploaded file
        text = extract_text_from_file(content, file.filename)
    except Exception as e:
        return {"error": f"Failed to extract text: {str(e)}"}

    try:
        # Run through LLM chain
        result = await summary_chain.ainvoke({"transcript": text})
        return {"summary": result}
    except Exception as e:
        return {"error": f"Summarization failed: {str(e)}"}
