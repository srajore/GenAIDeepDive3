from langchain_ollama import ChatOllama
#from dotenv import load_dotenv

#load_dotenv()

llm = ChatOllama(model="llama3.2:latest")

result = llm.invoke("What is the capital of India?").content

print(result)