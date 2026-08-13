# How to run this project
 - You need to have uv pakcage 
 - Run command in your terminal `$uv sync`
 - You can check env variables keys from .env.example
 - Copy the variables to .env by running command in you terminal `$cp .env.example .env` or you can simply copy/paste
 - Replace the api keys in .env file
 - Finally, you can run the streamlit app by typing command `uv run streamlit run app.py`

# The agent work:

- Searches the web
- Opens relevant pages
- Extracts information
- Compares multiple sources
- Produces a structured report

# Tech used: 
Open router LLM API + tavily web search + streamlit

# Agentic concepts:
tool calling, planning, loops, state.

User question
      ↓
LLM — "What should I research?"
      ↓
Search queries
      ↓
Tavily
      ↓
Search results
      ↓
LLM — "Which sources are useful?"
      ↓
Webpage extraction
      ↓
LLM — "Is there enough information?"
      ↓
   ┌──┴──┐
   No    Yes
   ↓      ↓
Search   Report
again