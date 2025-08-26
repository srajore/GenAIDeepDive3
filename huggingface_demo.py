from langchain_huggingface  import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv(override=True)

#from huggingface_hub import login
#login() # You will be prompted for your HF key, which will then be saved locally

# Basic Example (no streaming) with Mistral-Nemo-Base-2407 model using a third-party provider (Novita).
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b"
)

chat = ChatHuggingFace(llm=llm, verbose=True)

messages = [
    ("system", "You are a helpful assistant"),
    ("human", "What is GenAI?"),
]

result = chat.invoke(messages)

print(result.content)
