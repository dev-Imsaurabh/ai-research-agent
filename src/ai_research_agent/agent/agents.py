from openai import OpenAI
from pydantic import BaseModel

class ResponseStructure(BaseModel):
    is_valid : bool

class Agent:

    def __init__(self, apikey, baseurl = 'https://openrouter.ai/api/v1', model = 'openai/gpt-oss-20b:free'):
        self.client = OpenAI(base_url=baseurl, api_key = apikey)
        self.model = model

    def query_planner_agent(self, query:str):
        response = self.client.chat.completions.create(
                model=self.model,
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

    def content_extractor_agent(self, query:str, content:str):
        response = self.client.chat.completions.create(
                model= self.model,
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

    def content_validator_agent(self, query:str, extracted_content:str):
        response = self.client.chat.completions.parse(
                model=self.model,
                messages=[
                     {
                    "role": "system",
                    "content": """
                    You are a content checker agent.

                    Given a query and content, determine whether the content is relevant to the query.

                    You MUST return exactly one field:
                    - is_valid: True/False

                    Do not return any other fields.
                    Do not return "relevant".
                    Do not return "reason"..
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
