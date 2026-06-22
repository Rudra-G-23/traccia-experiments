from dotenv import load_dotenv
from groq import Groq
from rich import print

load_dotenv()

client = Groq()


def call_model(model):
    chat_completion = model.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain me the quantum computing in one sentence",
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion


if __name__ == "__main__":
    response = call_model(client)
    print(response)
