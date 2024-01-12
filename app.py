from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
def function(string):
    OPENAI_API_KEY=""
    llm=ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])
    chain = prompt | llm 

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"input": string})
def main():
    st.write("ChatGpt")
    input=st.text_input("Enter the Query")
    if input:
        ouput=function(input)
        st.write(ouput)
if __name__=="__main__":
    main()