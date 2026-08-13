from openai import OpenAI
from dotenv import dotenv_values


config = dotenv_values('.env')
open_router_api_key = config.get("OPEN_ROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=open_router_api_key)

def relevant_query_extractor(query:str, content:str):
    response = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
             {
            "role": "system",
            "content": """
            You are an agent which takes the 'query: some query' and 'content: some content' and based on the query you extract the relevant infomration from content and summerize.
            """
        },
            {
                "role":"user",
                "content":f"query: {query} and content:{content}"
            }
        ],
    )
    results = response.choices[0].message.content
    return results