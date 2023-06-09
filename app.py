# Bring in deps
import os 
 
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# App framework
st.title('🥨 Philly GPT 🥨')
prompt = st.text_input('WHAT DO YOU WANT TO KNOW ABOUT?') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='respond to this follwiong prompt how you normally would, but using Philly slang and incorporating both the words "bul", "yahnmean", and "jawn" several times ON SEPERATE OCCASSIONS in the proper context, also include the phrase "keep it a bean" at least once, at some point mention "smashin somebody baby mom", must be at least 2 paragraphs long and be written to sound as if a human wrote it creatively :  {topic}'
)

# Llms
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')

# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.run(prompt)
   

    st.write(title) 

