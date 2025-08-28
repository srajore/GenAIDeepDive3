# import necessary libraries
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr

# Set up llama3.2:latest with ollama
llm = ChatOllama(model="llama3.2:latest")

# Create a ChatPromptTemplate
prompt = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant . Answer the user's questions to the best of your abilities."),
        ("human", "{question}")
    ]
)

# Create a chain
chain = prompt | llm

#result = chain.invoke({"question": "What is the capital of India?"})

#print(result.content)

# Function to handle user input and generate response

def chatbot(question):
    response= chain.invoke({"question": question})
    return response.content


with gr.Blocks() as demo:
    gr.Markdown("## Zensar ChatBot")
    input_box = gr.Textbox(label="Ask a question", placeholder="Type your question here...")
    output_box = gr.Textbox(label="Answer", placeholder="The answer will appear here...", interactive=False)    
    submit_button = gr.Button("Submit")

    submit_button.click(
        fn=chatbot,
        inputs= input_box,
        outputs= output_box
    )

demo.launch()