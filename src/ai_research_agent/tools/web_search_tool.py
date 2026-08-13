from dotenv import dotenv_values
from tavily import TavilyClient

config = dotenv_values('.env')
api_key = config.get("TAVILY_API_KEY")
client = TavilyClient(api_key=api_key)

def search_by_tavily(query:str):
    response = client.search(f"you have look for news based on the query:{query}", search_depth="advanced", max_results=1)
    return response
