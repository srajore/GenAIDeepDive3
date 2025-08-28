from langchain_huggingface  import ChatHuggingFace,HuggingFacePipeline
#from dotenv import load_dotenv

#load_dotenv(override=True)

#from huggingface_hub import login
#login() # You will be prompted for your HF key, which will then be saved locally

# Basic Example (no streaming) with Mistral-Nemo-Base-2407 model using a third-party provider (Novita).
#llm = HuggingFacePipeline.from_model_id(
#    model_id="HuggingFaceTB/SmolLM3-3B",
#    task="text-generation",
#    pipeline_kwargs={"max_new_tokens": 100},
#    model_kwargs={"temperature": 0.7}
   
#)

llm2 = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm2)

result = model.invoke("What is the capital of India?")

print(result.content)
