from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

# Set up llama3.2:latest with ollama
#llm = ChatOllama(model="llama3.2:latest")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template=" write a summery for the following poem in 2 sentenses - \n {poem}",
    input_variables=["poem"]
)

loader = TextLoader('poem.txt',encoding='utf-8')

docs = loader.load()

#print(docs)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({"poem": docs[0].page_content})  

print(response)
# without LCEL