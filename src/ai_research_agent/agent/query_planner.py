from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")

if not open_router_api_key:
    open_router_api_key = st.secrets.get("OPEN_ROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=open_router_api_key)

def query_planner_agent(query:str):
    response = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
             {
            "role": "system",
            "content": """
            You are a query maker agent. Give 3 new queries based on the given input.
            """
        },
            {
                "role":"user",
                "content":query
            }
        ],
    )
    results = response.choices[0].message.content
    return results