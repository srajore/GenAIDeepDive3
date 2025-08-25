from langchain_openai import AzureOpenAI

from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv(override=True)

llm = AzureOpenAI(deployment_name="gpt-35-turbo-instruct", model="gpt-35-turbo-instruct")

prompt = ChatPromptTemplate.from_template("what is the capital of {country}?")



chain = prompt | llm


response = chain.invoke({"country": "France"})

print(response)

