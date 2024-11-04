import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

template = (
    """You are a really nice guy. Answer the user's question in a friendly tone"""
)

prompt = ChatPromptTemplate.from_template(template)

# Set up the Streamlit framework
st.title("AI Assistant")  # Set the title of the Streamlit app
input_text = st.text_input(
    "Ask your question!"
)  # Create a text input field in the Streamlit app
