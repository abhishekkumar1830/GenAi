import os
#PromptTemplate-write your questions nicely means,you can customize which kind of response fromat you want from ai 
#memory=who remembers your previous chat
from langchain.prompts import PromptTemplate
#conversationchain-a smart messanger who format your question,see the previous chat in memory,send the ai and update the memory automaticallly it does 3 works alone
#if we dont use promptstemplate, conversationchain used the prebuilt prompt format 
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm=ChatGroq(api_key=os.getenv("Groq_Api"),model="llama-3.3-70b-versatile",temperature=0.7,max_tokens=None)
#giving prompt style according to us
structured_prompt=PromptTemplate(input_variables=["topic"],template="provide brief explanation of {topic} and list its three main concepts.in a single line")
# LCEL:Lang chain Expression Language
# A new way to connect piplines in langchain framework
# we connect structure prompt and llm using pipe operator(|)
#this StrOutputParser() is used to generate clear output so we dont need to write the content
parser=StrOutputParser()
chain=structured_prompt | llm | parser
inputs={"topic":input("Enter the question")}
response=chain.invoke(inputs)
print(response)
