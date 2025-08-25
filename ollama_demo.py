from langchain_ollama.chat_models import ChatOllama
#from dotenv import load_dotenv

#load_dotenv()

llm = ChatOllama(model="phi:latest")

result = llm.invoke("What is the capital of India?").content

print(result)