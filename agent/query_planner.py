from openai import OpenAI
from dotenv import dotenv_values


config = dotenv_values('.env')
open_router_api_key = config.get("OPEN_ROUTER_API_KEY")

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