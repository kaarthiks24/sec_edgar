"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI
import langchain_visualizer
from langchain_visualizer import visualize_embeddings
from load_agent import load_agents
from tools import create_tools
tools = create_tools()
agent=load_agents(tools)


# From here down is all the StreamLit UI.
st.set_page_config(
    page_title="FreeForm Discussion Demo",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="auto",
)

header_html = """
<div style="display: flex; align-items: center;">
    <a href="https://en.wikipedia.org/wiki/U.S._Securities_and_Exchange_Commission">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Seal_of_the_United_States_Securities_and_Exchange_Commission.svg/1200px-Seal_of_the_United_States_Securities_and_Exchange_Commission.svg.png" alt="SEC Logo" width="100">
    </a>
    <h1 style="margin-left: 20px;">FreeForm Discussion Demo</h1>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

st.markdown(
    """
    This is a demo of a question and answer chatbot for SEC documents using LangChain. 
    Enter your question in the input field below and click the 'Ask' button to get the answer.
    """
)
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("Your query: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()
import asyncio
if user_input:
    async def search_agent_demo():
        output=agent.run(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
        return output

    
    langchain_visualizer.visualize(search_agent_demo)

    
    

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"])-1,-1,-1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
        message(st.session_state["generated"][i], key=str(i))


