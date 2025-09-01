from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

# Set up llama3.2:latest with ollama
#llm = ChatOllama(model="llama3.2:latest")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Answer the following question \n {question} fromthe following text \n {text}",
    input_variables=["question","text"]
)

url ="https://www.amazon.in/Daikin-Inverter-Copper-Filter-MTKM50U/dp/B09R4RYCJ4/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.LpujZ4uISPUK8sa_6yNGVY-3zoi-I7NYK-eHPsE7wGDDe5gR4wiXFNOAqexYtHRw8BdOCXbWsVVka54tE7wmzp0520p0LoTi57Xz1ZJK4iI3ZPHSCIUDbNbvDToPWn5cBnBr6EKEjpSnCFjoXwAHWhPzI2J6sG9SF0vvE9MAHnlqRP0Nc6DJE46MY8aP4LlB5YD38SjTQW2MWIwXacy16fPYNai7GbOv7PczdQemJhrmfwL_Ns1LswvWWRMwWYbtGwYEc8HTE94zsJtixK5-Ox9Gh8BmSQQL_lNyy5Ud6lQ.EvEgxtbvNzmW_uf6FthZW4K_hDnERcl2pIopO_6ijy0&dib_tag=se&pd_rd_r=a014485a-4ee9-45da-b79a-00b583118205&pd_rd_w=liotq&pd_rd_wg=DwAxB&qid=1756742243&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-3&th=1"


loader = WebBaseLoader(
    url
)

docs = loader.load()

#print(docs)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({"question": "What are the key features of this product?", "text": docs[0].page_content})

print(response)
# without LCEL