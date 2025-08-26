from langchain_huggingface  import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv(override=True)

#from huggingface_hub import login
#login() # You will be prompted for your HF key, which will then be saved locally

# Basic Example (no streaming) with Mistral-Nemo-Base-2407 model using a third-party provider (Novita).
llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100},
    model_kwargs={"temperature": 0.7}
   
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)
