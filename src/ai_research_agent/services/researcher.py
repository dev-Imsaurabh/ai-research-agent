from ai_research_agent.tools import web_search_tool
import time
from dotenv import load_dotenv
import os
import streamlit as st
from ai_research_agent.agent.agents import Agent

load_dotenv()
open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")

if not open_router_api_key:
    open_router_api_key = st.secrets.get("OPEN_ROUTER_API_KEY")

agent = Agent(apikey=open_router_api_key)

tavily_search = web_search_tool.search_by_tavily
query_planner_agent = agent.query_planner_agent
content_extractor_agent = agent.content_extractor_agent
content_validator_agent = agent.content_validator_agent


def researcher(query:str, on_progress, max_attempt = 0):
     on_progress("Understanding question...")
        #  lets call the make_query_agent to frame question absed on user query
     question = query_planner_agent(query)

     
     on_progress("Searching on web...")
        #  then we are calling our web search api
     web_search_content =  tavily_search(query=question)

     on_progress("Gathering relevant information...")
        #  now we will extract relevant infor based on query and summurize by our agent.
     relevant_info_results = content_extractor_agent(query, web_search_content["results"][0]["content"])

     on_progress("Validating output...")
        # now we will validate the content if its matches with query or not and if its matches we print the results otherwise we call the make_resport function again.
     is_valid = content_validator_agent(query, relevant_info_results)
     if (is_valid):
        return relevant_info_results
     else:
        if max_attempt >=3:
            return "Sorry! I am unable to answer your question."
        max_attempt += 1
        on_progress(f"Retrying: Attempt {max_attempt}")
        #keeping 2 second wait time to show agent is retrying
        time.sleep(2)
        return researcher(query, on_progress, max_attempt)
