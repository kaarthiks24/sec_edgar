"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI

from load_agent import load_agents
from tools import create_tools
tools = create_tools()
agent=load_agents(tools)

while True:
    query=input("Query>")
    agent.run(query)
    if query=="quit":
        break

# # From here down is all the StreamLit UI.
# st.set_page_config(
#     page_title="LangChain Chatbot Demo",
#     page_icon=":robot:",
#     layout="centered",
#     initial_sidebar_state="auto",
# )
# st.header("LangChain Demo: SEC Filings")
# st.markdown(
#     """
#     This is a demo of a question and answer chatbot for SEC documents using LangChain. 
#     Enter your question in the input field below and click the 'Ask' button to get the answer.
#     """
# )

# if "generated" not in st.session_state:
#     st.session_state["generated"] = []

# if "past" not in st.session_state:
#     st.session_state["past"] = []


# def get_text():
#     input_text = st.text_input("Your query: ", "Hello, how are you?", key="input")
#     return input_text


# user_input = get_text()

# if user_input:
#     output = agent.run(input=user_input)

#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output)

# if st.session_state["generated"]:

#     for i in range(len(st.session_state["generated"])-1,-1,-1):
#         message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
#         message(st.session_state["generated"][i], key=str(i))
