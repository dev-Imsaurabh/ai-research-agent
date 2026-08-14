from dotenv import dotenv_values
from tavily import TavilyClient
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    api_key = st.secrets.get("TAVILY_API_KEY")
    
client = TavilyClient(api_key=api_key)

def search_by_tavily(query:str):
    response = client.search(f"you have to look for news based on the query:{query}", search_depth="advanced", max_results=1)
    return response
