import os
from constants import openai_key
from langchain.llms import OpenAI
import requests
import streamlit as st

def repoaccess(user):
    url = "https://api.github.com/users/{}/repos".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        repositories=response.json()
    else:
        print("Enter valid github username")
    for repository in repositories:
        st.write(repository["name"])


#Api key
os.environ["OPENAI_API_KEY"]=openai_key

#streamlit framework
st.title("Github Analysis Project")
username=st.text_input("Enter the Github Username")

##OpenAI LLMS
#llm=OpenAI(temperature=0.8)


if username:
#   st.write(llm(username))
    repoaccess(username)
    
