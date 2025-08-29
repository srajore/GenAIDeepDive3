# import necessary libraries
#from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import gradio as gr
import uuid

load_dotenv(override=True)

# Set up llama3.2:latest with ollama
#llm = ChatOllama(model="llama3.2:latest")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create a ChatPromptTemplate
prompt = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant . Answer the user's questions to the best of your abilities."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ]
)


# Initialize  chat history
store={}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain = RunnableWithMessageHistory(
    runnable= prompt | llm,
    get_session_history = get_session_history,
    input_messages_key="input",
    #history_variable_name="history"
    history_messages_key="history"
)

# Create a chain
#chain = prompt | llm

#result = chain.invoke({"question": "What is the capital of India?"})

#print(result.content)

# Function to handle user input and generate response

def chatbot(user_input, history_state, session_id=str(uuid.uuid4())):
    response= chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
        ).content
    
    if history_state is None:
        history_state = []
    history_state.append((user_input, response))

    return response, history_state, session_id

    


with gr.Blocks() as demo:
    gr.Markdown("## Zensar ChatBot")
    history_state = gr.State(value=None)
    session_id = gr.State(value=str(uuid.uuid4()))
    input_box = gr.Textbox(label="Ask a question", placeholder="Type your question here...")
    output_box = gr.Textbox(label="Answer", placeholder="The answer will appear here...", interactive=False)    
    submit_button = gr.Button("Submit")

    submit_button.click(
        fn=chatbot,
        inputs= [input_box,history_state, session_id],
        outputs= [output_box,history_state, session_id]
    )

demo.launch()