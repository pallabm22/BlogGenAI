import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_huggingface import HuggingFaceEndpoint
from HuggingFaceAPI import access_key
from langchain import LLMChain

#Function to get response from API
def LLM(input_text,no_words,blog_style):
    repo_id='meta-llama/Llama-2-7b-chat-hf'
    llm=HuggingFaceEndpoint(
        repo_id=repo_id,
        max_length=500,
        temparature=0.7,
        huggingfacehub_api_token=access_key
    )

    template= """" Write a {blog_style} blog about {input_text} within {no_words} words."""

    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"], 
                          template=template
    )

    llm_chain=LLMChain(prompt=prompt,llm=llm)
    response=llm_chain.invoke({
        "blog_style":blog_style,
        "input_text":input_text,
        "no_words":no_words
        })
    return response



st.set_page_config(page_title="Generate Blogs",
                    page_icon='✍️',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs ✍️")

input_text=st.text_input("Enter the Blog Topic")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")


if submit:
    if not input_text or not no_words:
        st.error("please enter a valid text or a valid number of words")
    else:
        with st.spinner("Generating your blog, please wait..."):
            try:
                response=LLM(input_text,int(no_words),blog_style)
                st.write(response)
            except Exception as e:
                st.error(f"An error occured{e}")
