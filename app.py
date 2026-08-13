import streamlit as st
from tools import web_search_tool
from agent import query_maker_agent, extract_relevant_query, check_content_agent

tavily_search = web_search_tool.search_by_tavily
query_maker = query_maker_agent.query_maker
relevant_query = extract_relevant_query.relevant_query_extractor
check_content = check_content_agent.check_content

def make_report(query:str):
     with st.spinner("Understanding question...", show_time=True):
        #  lets call the make_query_agent to frame question absed on user query
        question = query_maker(query)

     with st.spinner("Searching on web...", show_time=True):
        #  then we are calling our web search api
        web_search_content =  tavily_search(query=question)

     with st.spinner("Gathering relevant information...", show_time=True):
        #  now we will extract relevant infor based on query and summurize by our agent.
        relevant_query_results = relevant_query(query, web_search_content["results"][0]["content"])

     with st.spinner("Validating output...", show_time=True):
        # now we will validate the content if its matches with query or not and if its matches we print the results otherwise we call the make_resport function again.
        is_valid = check_content(query, relevant_query_results)
        if (is_valid):
            st.write(relevant_query_results)
        else:
            with st.spinner("Looping...", show_time=True):
                make_report(query)
     st.write("Job finished")


st.title("AI reseach agent")

query = st.text_input("Enter your question", "")

is_clicked = st.button("Search", type="primary")

if is_clicked:
    if query:
        make_report(query)
    else:
        st.write("Please eneter your query")

    

    





