from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils import llm

SUMMARY_PROMPT = """
You are an AI assistant. Given the transcript below, return:
1. Summary of the meeting
2. Client Pain Points
3. Objections and how they were resolved
4. Follow-up Action Items

Transcript:
{transcript}
"""
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils import model as llm  # use the huggingface Chat model

SUMMARY_PROMPT = """
You are an AI assistant. Given the transcript below, return:
1. Summary of the meeting
2. Client Pain Points
3. Objections and how they were resolved
4. Follow-up Action Items

Transcript:
{transcript}
"""

prompt = PromptTemplate(
    input_variables=["transcript"],
    template=SUMMARY_PROMPT
)

summary_chain = prompt | llm | StrOutputParser()

def get_summary_chain():
    return summary_chain

prompt = PromptTemplate(
    input_variables=["transcript"],
    template=SUMMARY_PROMPT
)

# Chain: Prompt → LLM → Output parser
summary_chain = prompt | llm | StrOutputParser()

def run_summary(text: str) -> str:
    """Runs the summarization synchronously."""
    return summary_chain.invoke({"transcript": text})
