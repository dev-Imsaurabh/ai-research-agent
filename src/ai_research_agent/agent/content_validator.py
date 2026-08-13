from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import streamlit as st
load_dotenv()
class ResponseStructure(BaseModel):
    is_valid : bool
open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")

if not open_router_api_key:
    open_router_api_key = st.secrets.get("OPEN_ROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=open_router_api_key)

def content_validator_agent(query:str, extracted_content):
    response = client.chat.completions.parse(
        model='openai/gpt-oss-20b',
        messages=[
             {
            "role": "system",
            "content": """
            You are a content checker agent. you are given 'query: some query' and 'content: some content' and based on query you have to check that if the content is relevant and you have output is_valid True/False .
            """
        },
            {
                "role":"user",
                "content": f"query: {query} and content: {extracted_content}"
            }
        ],
        response_format=ResponseStructure
    )
    results = response.choices[0].message.parsed
    return results.is_valid