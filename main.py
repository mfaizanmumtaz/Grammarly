from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = PromptTemplate.from_template(
    """Correct Grammar mistakes in the text delimited with ```.\
    step -1 You should be aware of context while correcting grammar mistakes and do not generate extra text.
    step -2 Output format should be only text without any dacoration
    
    --------------

    Text: ```{text}```"""
)

model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)

chain = prompt | model | StrOutputParser()

import streamlit as st


st.set_page_config("Grammarly", page_icon="🅖")

st.title("Grammarly")

st.markdown("Correct grammar mistakes in your text")

text = st.text_area("Enter text")

if st.button("Correct"):

    with st.spinner("Correcting..."):

        st.markdown(chain.invoke({"text":text}))