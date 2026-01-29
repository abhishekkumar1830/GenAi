import os
#here langachai_groq is python package who connects groq api to langchain and provide chatgroq class
#we use longchan_groq becuase groq only provide api not sdk so langchain creates wrapper ChatGroq who will works like sdk
#SDK=it lets we can use api without worrying about how request,authentication and errors are handeled,google gemni models has python sdk
#we use simply built in functions of sdk dont write manually code for api working
#we are using llama model,developed by meta,but it doesnt provide hosting(means server/hardware to run it)
#groq=it is hardware+Ai company,they host models like llama and others so we can run them without worrying about infrastracture
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
#temprature=it used to generate balanced,natural and readable output less tempratures are good more natural
#max_tokes= it tells how long ai response can be
llm=ChatGroq(api_key=os.getenv("Groq_Api"),model="llama-3.3-70b-versatile",temperature=0.7,max_tokens=None)
# print(llm)
prompt=input("Enter what you want to ask :")
#invoke=asked llm model(here llama) to generate response and invoke is method of langchain for all google,openai,chatgroq etc
response=llm.invoke(prompt)
print(response.text)