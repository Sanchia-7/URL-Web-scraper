from langchain_openai import AzureChatOpenAI
from summarizer.prompt import SUMMARY_PROMPT
from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)
from summarizer.prompt import SUMMARY_PROMPT


llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION,
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    temperature=0.3,
)

def summarize(text: str) -> str:
    prompt = SUMMARY_PROMPT.format(text=text[:4000])
    response = llm.invoke(prompt)
    return response.content
