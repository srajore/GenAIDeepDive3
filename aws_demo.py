from langchain_aws import ChatBedrockConverse

from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatBedrockConverse(
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",
)


result = llm.invoke("What is Agentic AI in 15 words").content

print(result)