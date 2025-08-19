from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="What is genai in 20 words ."
)

print(response.output_text)