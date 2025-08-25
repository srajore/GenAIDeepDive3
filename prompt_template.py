from langchain_core.prompts import PromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate.from_template(" Tell me key achivements of {name} in 4 bulleted points.")

#chain = prompt | llm    # with LCEL

response = llm.invoke(prompt.format(name="Sharad Rajore"))  # without LCEL
#response = chain.invoke({"name":"Sharad Rajore"})

print(response.content)