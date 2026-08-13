import streamlit as st
from services import researcher


make_report = researcher.make_report
st.title("AI reseach agent")

query = st.text_input("Enter your question", "")

is_clicked = st.button("Search", type="primary")

def make_progress_callback(status):
    def on_progress(message):
        status.update(label=message)

    return on_progress


if is_clicked:
    if query:
        with st.status("Starting research...", expanded=True) as status:
            on_progress = make_progress_callback(status)
            result = make_report(query, on_progress)
            status.update(
                label="Research completed!",
                state="complete"
            )
        st.write(result)
    else:
        st.write("Please eneter your query")

    

    





